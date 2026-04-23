create database if not exists kitobxona;
use kitobxona;
create table janr (id int auto_increment primary key, name varchar(50));


create table author (id int auto_increment primary key, name varchar(30));

create table book (id int auto_increment primary key, name varchar(30), j_id int, a_id int, quantity int,
foreign key (j_id) references janr(id) on delete cascade on update cascade,
foreign key (a_id) references author(id) on delete cascade on update cascade);



insert into janr(name) values("roman"), ("qissa"), ("doston"),("hikoya"),("Dramma");

insert into author (name) values("Alisher Navoiy"), ("Robert Green"), ("Dostoyevskiy");

insert into book(name, j_id, a_id,quantity) values("Hayrat ul abror", 3, 1, 32);
insert into book(name, j_id, a_id, quantity) values("jinoyat va jazo", 4, 3, 42);
insert into book(name, j_id, a_id, quantity) values("Power", 3, 2,45);
insert into book(name, j_id, a_id, quantity) values("Power", 3, 2,56);
insert into book(name, j_id, a_id, quantity) values("Power", 3, 2,12);
insert into book(name, j_id, a_id, quantity) values("Layli va majnun", 2, 1,23);

select a.name, json_arrayagg(b.name), json_arrayagg(j.name) from book as b 
inner join author as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id group by a.name;

   
+----------------+----------------------------------------+--------------------------------+
| name           | json_arrayagg(b.name)                  | json_arrayagg(j.name)          |
+----------------+----------------------------------------+--------------------------------+
| Alisher Navoiy | ["Layli va majnun", "Hayrat ul abror"] | ["qissa", "doston"]            |
| Dostoyevskiy   | ["jinoyat va jazo"]                    | ["hikoya"]                     |
| Robert Green   | ["Power", "Power", "Power"]            | ["doston", "doston", "doston"] |
+----------------+----------------------------------------+--------------------------------+


-- 1-shart A.Navoiy yozgan janrlar ro'yhati

select a.name,  json_arrayagg(j.name) from book as b 
inner join author as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id group by a.name having a.name="Alisher Navoiy";

+----------------+-----------------------+
| name           | json_arrayagg(j.name) |
+----------------+-----------------------+
| Alisher Navoiy | ["qissa", "doston"]   |
+----------------+-----------------------+

-- 2-shart barchar authorlarning yozgan janrlari

select a.name,  json_arrayagg(j.name) from book as b 
inner join author as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id group by a.name;

+----------------+--------------------------------+
| name           | json_arrayagg(j.name)          |
+----------------+--------------------------------+
| Alisher Navoiy | ["qissa", "doston"]            |
| Dostoyevskiy   | ["hikoya"]                     |
| Robert Green   | ["doston", "doston", "doston"] |
+----------------+--------------------------------+

-- 3-shart barchar author lar janrlar bo'yicha nechtadan kitob yozgan

select a.name,  count(b.name) as kitoblar_soni from book as b 
inner join author as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id group by a.name;

+----------------+---------------+
| name           | kitoblar_soni |
+----------------+---------------+
| Alisher Navoiy |             2 |
| Robert Green   |             3 |
| Dostoyevskiy   |             1 |
+----------------+---------------+


-- bu yerda kitob nomi yodimga kelmagani uchun power 3 marta yozdim uni xato deb 
-- o'ylamang shuning uchun column ni unique qilmadim



4-shart eng kop yozilagan janr 

select j.name,  count(*) as janr from book as b 
inner join author as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id group by j.name order by janr desc limit 1;

+--------+------+
| name   | janr |
+--------+------+
| doston |    4 |
+--------+------+


5-shart har bir author qaysi janrda kop ijod qilgan

select a.name,  count(*) as janrlar from book as b
inner join author as a on b.a_id=a.id
inner join janr as j on b.j_id=j.id group by a.name order by janrlar desc;




6 shart kimning kitobi eng kop sotilgan;
select a.name,  b.name, quantity from book as b inner join author  as a on b.a_id=a.id 
inner join janr as j on b.j_id=j.id order by quantity desc limit 1;

    

+--------------+-------+----------+
| name         | name  | quantity |
+--------------+-------+----------+
| Robert Green | Power |       56 |
+--------------+-------+----------+
 
--   bu yerda power kitobini boshqa qismlari ham bor lekin nomi bir xil














