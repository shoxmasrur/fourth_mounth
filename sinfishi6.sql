create database kitoblar;
use kitoblar;
create table kitob (id int auto_increment primary key, kitob_nomi varchar(30), published int 
a_id int, j_id int);
create table author (id int auto_increment primary key, name varchar(30));
create table janr( id int auto_increment primary key, janr_name varchar(30));

insert into kitob