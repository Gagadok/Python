CREATE TABLE Information(
  ID INT identity (0,1) NOT NULL,
  date DATE NOT NULL,
  latin_characters CHAR (10) NOT NULL,
  russian_characters NCHAR (10) NOT NULL,
  integer int NOT NULL,
  real DECIMAL (18, 10) NOT NULL, 
  PRIMARY KEY (ID)
);