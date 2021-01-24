USE [Q2]
GO

CREATE TABLE Date(
  Period NCHAR(26) NOT NULL,
  Date_of_creation DATETIME NOT NULL
  PRIMARY KEY (Period)
);

CREATE TABLE Statement(
  Statement_ID INT identity (0,1) NOT NULL,
  Account INT NOT NULL,
  Incoming_balance_active DECIMAL (26, 10) NOT NULL,
  Incoming_balance_passive DECIMAL (26, 10) NOT NULL,
  Turnover_debit DECIMAL (26, 10) NOT NULL,
  Turnover_credit DECIMAL (26, 10) NOT NULL,
  Closing_balance_active DECIMAL (26, 10) NOT NULL,
  Closing_balance_passive DECIMAL (26, 10) NOT NULL,
  PRIMARY KEY (Statement_ID),
  Fk_Date NCHAR(26),
  FOREIGN KEY (Fk_Date) REFERENCES Date(Period)
);