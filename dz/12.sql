create database univer;
use univer;

create table class (
  id int primary key auto_increment,
    name varchar(60) default 'Без названия'
    );

create table student (
  id int primary key auto_increment,
  first_name varchar(10) not null,
    last_name varchar(10),
  age tinyint unsigned not null,
    class_id int not null,
    email varchar(30) unique not null,
    phone varchar(30) not null unique,
    
    constraint name_check check (first_name != ''),
    constraint age_check check (age > 0 and age < 120),
    constraint email_check check (email regexp '^[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+'),
    constraint phone_check check (phone regexp '^[0-9]+$'),
    foreign key (class_id) references class (id)
);
select * from student;

select * from class;

INSERT INTO class(name) VALUES ('Что-то новое');
INSERT INTO class (name) VALUES ('Математика');
INSERT INTO class (name) VALUES ('Физика');
INSERT INTO class (name) VALUES ('Гуманитарные науки');
INSERT INTO class (name) VALUES ('Изо');

INSERT INTO student (first_name, last_name, age, class_id, email, phone) VALUES ('Кошкина', 'Машка', '17', '1', 'alo@kot.ru', '375889562325');

