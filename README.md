# Python
1. В папке EY находятся 2 папки (Q1 и Q2) со скриптами:  
	1.1. В папке Q1 скрипт делает следующее:  
	<ul>
		<li>Генерирует 100 текстовых файлов, каждый из которых содержит 100 000 строк:
		<br><i>случайная дата за последние 5 лет || случайный набор 10 латинских символов || случайный набор 10 русских символов || случайное положительное четное целочисленное число в диапазоне от 1 до 100 000 000 || случайное положительное число с 8 знаками после запятой в диапазоне от 1 до 20;</i></li>
		<li>Объединяет файлы в 1. При объединении есть возможность удалить из всех файлов строки с заданным сочетанием символов, например, «abc», с выводом информации о количестве удаленных строк;</li>
		<li>Создаёт процедуру импорта файлов с таким набором полей в таблицу в СУБД. При импорте выводится ход процесса (сколько строк импортировано, сколько осталось);</li>
		<li>Реализован sql-скрипт, который считает сумму всех целых чисел и медиану всех дробных чисел.</li>
	</ul>
	1.2. В папке Q2 скрипт делает следующее:  
	<ul>
		<li>Анализирует структуру excel-файла;</li>
		<li>Так же с помощью web-интерфейса реализована загрузку данных из excel-файла такого формата в СУБД, просмотр списка загруженных файлов, отображение данных из СУБД по визуальной аналогии с exсel-файлом для каждого из загруженных файлов.</li>
	</ul>
2. В папке NLTK находятся скрипты с использованием библиотеки NLTK.  
	2.1. Папка 1. Используя заготовленный текстовый файл:  
	<ul>
		<li>Прочитать текстовый файл и разбить его на токены;</li>
		<li>Определить токен с наибольшей частотой встречаемости;</li>
		<li>Для каждого токена вывести его корень;</li>
		<li>Для данного слова найти все его позиции в тексте;</li>
		<li>Найти все слова, удовлетворяющие заданному регулярному выражению (например, заканчивающиеся на ow);</li>
		<li>Найти все слова, содержащие заданное подслово;</li>
		<li>Удалить из текста все стоп-слова.</li>
	</ul>
	2.2. Папка 2. Используя текстовый файл с ошибками в словах:  
	<ul>
		<li>Прочитать текстовый файл;</li>
		<li>Удалить из текста все стоп-слова;</li>
		<li>Вычислить частоты слов, включая слова, написанные с ошибками;</li>
		<li>Сформулировать некоторый поисковый запрос как множество из двух-трех ключевых слов. Найти предложение, которое содержит не менее двух из указанных в запросе ключевых слов, возможно записанных с ошибками.</li>
	</ul>
