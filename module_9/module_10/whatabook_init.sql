ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;



CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

    
INSERT INTO store(locale)
    VALUES('Chucky Cheese Dr, Squeaker Town, AZ 78915');

    
INSERT INTO book(book_name, author, details)
    VALUES('A Game of Thrones', 'George R.R. Martin', 'The first book of the Game of Thrones Series');

INSERT INTO book(book_name, author, details)
    VALUES('A Clash of Kings', 'George R.R. Martin', 'The second book of the Game of Thrones Series');

INSERT INTO book(book_name, author, details)
    VALUES('A Storm of Swords', 'George R.R. Martin', "The third book of the Game of Thrones Series");

INSERT INTO book(book_name, author, details)
    VALUES('A Feast for Crows', 'George R.R. Martin', "The fourth book of the Game of Thrones Series");

INSERT INTO book(book_name, author, details)
    VALUES('A Dance with Dragons', 'George R.R. Martin', " The fifth book of the Game of Thrones Series");

INSERT INTO book(book_name, author, details)
    VALUES('The Winds of Winter', 'George R.R. Martin', "The sixth book of the Game of Thrones Series");

INSERT INTO book(book_name, author, details)
    VALUES('A Dream of Spring', 'George R.R. Martin', "The seventh book of the Game of Thrones Series");

INSERT INTO book(book_name, author)
    VALUES('The Help', 'Kathryn Stockett');

INSERT INTO book(book_name, author)
    VALUES('Where the Crawdads Sing', 'Delia Owens');

    # adding the users to the database
INSERT INTO user(first_name, last_name) 
    VALUES('Indiana', 'Jones');

INSERT INTO user(first_name, last_name)
    VALUES('Tywin', 'Lannister');

INSERT INTO user(first_name, last_name)
    VALUES('Harry', 'Potter');

    
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Indiana'), 
        (SELECT book_id FROM book WHERE book_name = 'The Winds of Winter')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Tywin'),
        (SELECT book_id FROM book WHERE book_name = 'The Help')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'),
        (SELECT book_id FROM book WHERE book_name = 'A Dance with Dragons')
    )