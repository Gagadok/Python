USE [Q1]
GO

declare @the_sum_of_the_integers BIGINT;
SELECT @the_sum_of_the_integers = SUM (CAST (integer AS BIGINT)) FROM [dbo].[Information]
PRINT 'Cумму всех целых чисел: ' + CONVERT(VARCHAR, @the_sum_of_the_integers);
GO

declare @median DECIMAL (18, 10);
declare @number_of_rows INT;
SELECT @number_of_rows = IDENT_CURRENT ('Information');
SELECT real FROM [dbo].[Information] ORDER BY real
IF @number_of_rows % 2 = 0
	SELECT @median = AVG (real) FROM
	(SELECT row_number() OVER (order by real) AS n, * FROM [dbo].[Information]) x
	WHERE n = @number_of_rows / 2 OR n = @number_of_rows / 2 + 1
ELSE
	SELECT @median = real FROM
	(SELECT row_number() OVER (order by real) AS n, * FROM [dbo].[Information]) x
	WHERE n = (@number_of_rows + 1) / 2
PRINT 'Медиана всех дробных чисел: ' + CONVERT(VARCHAR, @median);
GO