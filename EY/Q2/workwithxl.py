import xlrd
import mssql
import datetime

class WorkwithXL:

    date_table = "Date"
    statement_table = "Statement"
    database = "Q2"
    columns_date = ['Period', 'Date_of_creation']
    columns_statement = ['Account', 'Incoming_balance_active',
                         'Incoming_balance_passive', 'Turnover_debit',
                         'Turnover_credit', 'Closing_balance_active',
                         'Closing_balance_passive', 'Fk_Date']
    classes = {'1': "КЛАСС  1  Денежные средства, драгоценные металлы и межбанковские операции",
               '2': "КЛАСС  2  Кредитные и иные активные операции с клиентами",
               '3': "КЛАСС  3  Счета по операциям клиентов",
               '4': "КЛАСС  4  Ценные бумаги",
               '5': "КЛАСС  5  Долгосрочные финансовые вложения в уставные фонды юридических лиц, основные средства и прочее имущество",
               '6': "КЛАСС  6  Прочие активы и прочие пассивы",
               '7': "КЛАСС  7  Собственный капитал банка",
               '8': "КЛАСС  8  Доходы банка",
               '9': "КЛАСС  9  Расходы банка"}
    # Search for a key by value
    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k
    # Uploading excel to the database
    def download_XL_in_DB(self, filenames):
        for i in filenames:
            workbook = xlrd.open_workbook(i)
            worksheet = workbook.sheet_by_index(0)
            db = mssql.Mssql(self.database)
            
            Period = worksheet.cell(2, 0).value
            Period = Period[10:]
            Date_of_creation = datetime.datetime(*xlrd.xldate_as_tuple(
                worksheet.cell(5, 0).value, workbook.datemode))
            
            db.loading_data(self.date_table, self.columns_date,
                            [Period, Date_of_creation], ['0', '1'])
            
            key = 0
            for row_number in range(8, worksheet.nrows):
                row = worksheet.row_values(row_number)
                if self.get_key(self.classes, row[0]):
                    key = self.get_key(self.classes, row[0])
                else:
                    if row[0] == "ПО КЛАССУ": # Encode the total balance lines
                    # of each class
                        del row[0]
                        row.insert(0, key)
                        row.extend([Period])
                        db.loading_data(self.statement_table, self.columns_statement,
                            row, ['7'])
                    else:
                        if row[0] == "БАЛАНС": # Encode the total balance
                            del row[0]
                            row.insert(0, '0')
                            row.extend([Period])
                            db.loading_data(self.statement_table,
                                            self.columns_statement, row, ['7'])
                        else:
                            row.extend([Period])
                            db.loading_data(self.statement_table,
                                            self.columns_statement, row, ['7'])
            
            print("Оборотная ведомость по балансовым счетам\nза период " + Period +
                  "\nпо банку ЗАГРУЖЕНА")
    
    # The function returns the names of all uploaded files.
    # Report period = file name, since the reporting period is unique
    def list_of_downloaded_files(self):
        column = ["Period"]
        db = mssql.Mssql(self.database)
        downloaded_files = []
        for i in db.getting_data(column, self.date_table):
            downloaded_files.append("Оборотная ведомость по балансовым счетам за период " + str(i[0]))
        if len(downloaded_files) == 0:
            downloaded_files.append("Загруженных файлов нет")
        return downloaded_files
    
    # Loading a report from the database 
    def download_the_report(self, period):
        column = self.columns_statement[0:7]
        condition = "Fk_Date = " + "'" + period + "'"
        db = mssql.Mssql(self.database)
        report = []
        for i in db.getting_data(column, self.statement_table, condition):
            row = []
            for indexJ, j in enumerate(i):
                if indexJ > 0:
                    j = j.normalize()
                row.append(str(j))
            report.append(row)
        return report