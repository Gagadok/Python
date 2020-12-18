import data
import workwithfiles

path = 'files'

for i in range(100):
    f = workwithfiles.file_creation(path, str(i) + '.txt')
    print("Заполнение файла " + str(i) + ".txt")
    for j in range(100000):
        # Using the methods from the "date.py" file, we generate strings
        f.write(str(data.random_date(5).strftime("%d.%m.%Y")) +
                '||' + str(data.random_Latin_characters(10)) +
                '||' + str(data.random_Russian_characters(10)) +
                '||' + str(data.random_even_number(1, 100000000)) +
                '||' + str(data.random_real_number(1, 20, 8)) + '\n')
        # After generating every 10000 lines, we output information about the % of execution
        if j % 10000 == 0:
            print("Файл " + str(i) + ".txt заполнен на " +
                  str((j * 100) / 100000) + "%")
    print("Файл " + str(i) + ".txt заполнен")
    f.close()

t = True
while t:
    print ("\nВыберите вариант")
    print ("1 - Объединение файлов в один")
    print ("2 - Импорт данный в БД")
    print ("0 - Выйти")
    choice = input()
    
    if int(choice) < 0 or int(choice) > 2:
        print ("Выберите еще раз")
        continue
    
    if int (choice) == 0:
        print ("Выход")
        break
    
    if int (choice) == 1:
        print ("Удалить из всех файлов строки с заданным сочетанием символов?")
        print ("1 - Да")
        print ("2 - Нет")
        while t:
            choice2 = input()
    
            if int(choice2) < 0 or int(choice2) > 2:
                print ("Выберите еще раз")
                continue
            
            if int (choice2) == 1:
                print ("Введите сочетание символов: ")
                symbols = input()
                print("Количество удалённых строк: " + 
                      str(workwithfiles.deleting_rows_in_all_files(path, symbols)))
            break
        
        workwithfiles.merge_the_files(path)
        
    if int (choice) == 2:
        workwithfiles.upload_the_merged_file_to_the_database(path)