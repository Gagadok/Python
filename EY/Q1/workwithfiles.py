# Working with files and uploading a file to the database

import shutil
import os
import mssql

class Workwithfiles:

    the_merged_file = "all.txt"    

    # Creating a file
    def file_creation(self, path, file_name):
        # If the required directory exists, we check the existence of the
        # file and create it if it does not exist. if there is - just
        # overwrite the information in it. If the directory does not exist,
        # create both a directory and a file
        if os.path.isdir(path):
            if os.path.exists(path + '/' + file_name):
                f = open(path + '/' + file_name, 'w')
                print("Файл " + path + '/' + file_name + " существует. Перезапись")
            else:
                print("Создание файла " + path + '/' + file_name)
                f = open(path + '/' + file_name, 'w')
        else:
            print("Создание папки " + path)
            os.mkdir(path)
            print("Создание файла " + path + '/' + file_name)
            f = open(path + '/' + file_name, 'w')
        return f
    
    # Deleting lines in a file with found characters "symbols"
    def deleting_rows_in_all_files(self, path, symbols):
        file_list = os.listdir(path)
        number_of_deleted_rows = 0
        # If there is a shared file with all the lines, ignore it
        for i in file_list:
            if self.the_merged_file == i:
                continue
            else:
                with open(path + '/' + i, 'r+') as file:
                    print("Обрабатывается файл " + i)
                    # We calculate the file size in order to monitor
                    # the progress of file processing
                    file_size = os.stat(path + '/' + i).st_size
                    current_offset = file.tell() # The current position of the pointer
                    while True:
                        line = file.readline()
                        if not line: # EOF
                            break
                        if line.find(symbols) == -1:
                            # If the line does not need to be deleted,
                            # write it to position "current_offset".
                            # Memorize the position of the read line to continue reading
                            unread_offset = file.tell()
                            file.seek(current_offset)
                            file.write(line)
                            current_offset = file.tell()
                            file.seek(unread_offset)
                        else:
                            number_of_deleted_rows += 1
                        # Trying to calculate the % processing of the file.
                        # Since % is not whole and i do not want to litter
                        # the console - i display a message only about the end of processing
                        if (file.tell() * 100 / file_size) % 20 == 0:
                            print("Файл " + i + " обработан")
                    # Crop the part of the file that contains the lines to delete
                    file.truncate(current_offset)
        return number_of_deleted_rows
    
    # File merges
    def merge_the_files(self, path):
        file_list = os.listdir(path)
        destination = open(path + '/' + self.the_merged_file, 'wb')
        for i in file_list:
            # If there is a shared file with all the lines, ignore it
            if self.the_merged_file == i:
                continue
            else:
                # Copy the bytes
                shutil.copyfileobj(open(path + '/' + i, 'rb'), destination)
        destination.close()
        print("Объединение файлов завершено")
    
    # Counting the number of rows
    def count_lines(self, filename, chunk_size=1<<13):
        with open(filename) as file:
            return sum(chunk.count('\n') # Number of rows = number '\n'
                       for chunk in iter(lambda: file.read(chunk_size), ''))    
    
    # Uploading a merged file to the database
    def upload_the_merged_file_to_the_database(self, path):
        number_of_rows = self.count_lines(path + '/' + self.the_merged_file)
        table = "Information"
        columns = ['date', 'latin_characters', 'russian_characters',
                   'integer', 'real']
        db = mssql.Mssql("Q1")
        # Clearing the table
        db.to_clear_the_table(table)
        with open(path + '/' + self.the_merged_file, 'r') as file:
            # Use "enumerate" to track % download
            for index, line in enumerate(file):
                values = line.split('||')
                db.loading_data(table, columns, values)
                if index % 10000 == 0:
                    print("Импортировано " + str(index) + " строк из " +
                          str(number_of_rows) + " (" +
                          str(round(index * 100 / number_of_rows, 2)) + "%)")
            print("Импортирование завершено")
            
#-----------------------------------------------

_inst = Workwithfiles()
file_creation = _inst.file_creation
deleting_rows_in_all_files = _inst.deleting_rows_in_all_files
merge_the_files = _inst.merge_the_files
upload_the_merged_file_to_the_database = _inst.upload_the_merged_file_to_the_database