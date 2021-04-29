1. В папке EY находятся 2 папки (Q1 и Q2) со скриптами:
<br />1.1. В папке Q1 скрипт делает следующее:
<br />- Генерирует 100 текстовых файлов, каждый из которых содержит 100 000 строк:
<br />случайная дата за последние 5 лет || случайный набор 10 латинских символов || случайный набор 10 русских символов || случайное положительное четное целочисленное число в диапазоне от 1 до 100 000 000 || случайное положительное число с 8 знаками после запятой в диапазоне от 1 до 20;
<br />- Объединяет файлы в 1. При объединении есть возможность удалить из всех файлов строки с заданным сочетанием символов, например, «abc», с выводом информации о количестве удаленных строк;
<br />- Создаёт процедуру импорта файлов с таким набором полей в таблицу в СУБД. При импорте выводится ход процесса (сколько строк импортировано, сколько осталось);
<br />- Реализован sql-скрипт, который считает сумму всех целых чисел и медиану всех дробных чисел.
<br />1.2. В папке Q2 скрипт делает следующее:
<br />- Анализирует структуру excel-файла;
<br />- Так же с помощью web-интерфейса реализована загрузку данных из excel-файла такого формата в СУБД, просмотр списка загруженных файлов, отображение данных из СУБД по визуальной аналогии с exсel-файлом для каждого из загруженных файлов.
<br />2. В папке NLTK находятся скрипты с использованием библиотеки NLTK.
<br />2.1. Папка 1. Используя заготовленный текстовый файл:
<br />- Прочитать текстовый файл и разбить его на токены;
<br />- Определить токен с наибольшей частотой встречаемости;
<br />- Для каждого токена вывести его корень;
<br />- Для данного слова найти все его позиции в тексте;
<br />- Найти все слова, удовлетворяющие заданному регулярному выражению (например, заканчивающиеся на ow);
<br />- Найти все слова, содержащие заданное подслово;
<br />- Удалить из текста все стоп-слова.
<br />2.2. Папка 2. Используя текстовый файл с ошибками в словах:
<br />- Прочитать текстовый файл;
<br />- Удалить из текста все стоп-слова;
<br />- Вычислить частоты слов, включая слова, написанные с ошибками;
<br />- Сформулировать некоторый поисковый запрос как множество из двух-трех ключевых слов. Найти предложение, которое содержит не менее двух из указанных в запросе ключевых слов, возможно записанных с ошибками.