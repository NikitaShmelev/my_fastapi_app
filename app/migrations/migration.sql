

INSERT INTO Persons
    (FirstName, LastName, adres)
VALUES
    ('Paweł', 'Oleksy', 'Kraków, ul. Mickiewicza 11/6'),
    ('Piotr', 'Dębowski', 'Kraków, ul. Zelona 12/7'),
    ('Eugeniusz', 'Kulik', 'Kraków, Weliczka, ul. Krakowska 7'),
    ('Piotr', 'Dębowski', 'Kraków, ul. Tatrzańska 7/9');

INSERT INTO Books
    (title, author)
VALUES
    ('Analiza matem.', 'Kowalski Jan'),
    ('Rachunek prawdopod.', 'Bałko Łukasz'),
    ('Fizyka dla inż', 'Kalestyński Andrzej'),
    ('C++: wprowadzenie', 'Balcerzak Józef'),
    ('Bazy danych wprowadzenie', 'Wasiak Jan');



CREATE TABLE Persons (
    ID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    PRIMARY KEY (ID)
);
ALTER TABLE persons
ADD adres varchar(255);

CREATE TABLE Books (
    ID int NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    PRIMARY KEY (ID)
);
ALTER TABLE books
ADD author varchar(255);


CREATE TABLE Rentals (
    id int NOT NULL AUTO_INCREMENT,
    retail_date DATE DEFAULT (CURRENT_DATE),
    PersonID int,
    BookID int,
    PRIMARY KEY (id),
    FOREIGN KEY (PersonID) REFERENCES Persons(id),
    FOREIGN KEY (BookId) REFERENCES Books(id)
);


INSERT INTO Rentals
    (PersonID, BookID, retail_date)
VALUES
    (1, 1, '2007-11-07'),
    (2, 2, '2007-12-09'),
    (3, 3, '2007-12-10'),
    (4, 2, '2008-01-04'),
    (2, 3, '2008-01-07');