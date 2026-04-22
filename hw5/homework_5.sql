create database if not exists products;

use products;

CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    sale_date DATE
);
INSERT INTO sales VALUES (1, 'Laptop', 'Electronics', 800, 2, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 'Electronics', 600, 3, '2025-01-01');
INSERT INTO sales VALUES (3, 'TV', 'Electronics', 900, 1, '2025-01-02');
INSERT INTO sales VALUES (4, 'Headphones', 'Electronics', 150, 5, '2025-01-03');

INSERT INTO sales VALUES (5, 'Table', 'Furniture', 300, 1, '2025-01-01');
INSERT INTO sales VALUES (6, 'Chair', 'Furniture', 100, 4, '2025-01-02');
INSERT INTO sales VALUES (7, 'Sofa', 'Furniture', 1200, 1, '2025-01-03');
INSERT INTO sales VALUES (8, 'Bed', 'Furniture', 900, 1, '2025-01-04');

INSERT INTO sales VALUES (9, 'T-shirt', 'Clothing', 40, 6, '2025-01-01');
INSERT INTO sales VALUES (10, 'Jeans', 'Clothing', 70, 3, '2025-01-02');
INSERT INTO sales VALUES (11, 'Jacket', 'Clothing', 120, 2, '2025-01-03');
INSERT INTO sales VALUES (12, 'Shoes', 'Clothing', 90, 4, '2025-01-04');

INSERT INTO sales VALUES (13, 'Apple', 'Food', 2, 20, '2025-01-01');
INSERT INTO sales VALUES (14, 'Bread', 'Food', 3, 15, '2025-01-02');
INSERT INTO sales VALUES (15, 'Milk', 'Food', 4, 10, '2025-01-03');
INSERT INTO sales VALUES (16, 'Cheese', 'Food', 8, 5, '2025-01-04');

INSERT INTO sales VALUES (17, 'Notebook', 'Stationery', 5, 10, '2025-01-01');
INSERT INTO sales VALUES (18, 'Pen', 'Stationery', 2, 25, '2025-01-02');
INSERT INTO sales VALUES (19, 'Marker', 'Stationery', 4, 12, '2025-01-03');
INSERT INTO sales VALUES (20, 'Folder', 'Stationery', 6, 8, '2025-01-04');

+----+--------------+-------------+-------+----------+------------+
| id | product_name | category    | price | quantity | sale_date  |
+----+--------------+-------------+-------+----------+------------+
|  1 | Laptop       | Electronics |   800 |        2 | 2025-01-01 |
|  2 | Phone        | Electronics |   600 |        3 | 2025-01-01 |
|  3 | TV           | Electronics |   900 |        1 | 2025-01-02 |
|  4 | Headphones   | Electronics |   150 |        5 | 2025-01-03 |
|  5 | Table        | Furniture   |   300 |        1 | 2025-01-01 |
|  6 | Chair        | Furniture   |   100 |        4 | 2025-01-02 |
|  7 | Sofa         | Furniture   |  1200 |        1 | 2025-01-03 |
|  8 | Bed          | Furniture   |   900 |        1 | 2025-01-04 |
|  9 | T-shirt      | Clothing    |    40 |        6 | 2025-01-01 |
| 10 | Jeans        | Clothing    |    70 |        3 | 2025-01-02 |
| 11 | Jacket       | Clothing    |   120 |        2 | 2025-01-03 |
| 12 | Shoes        | Clothing    |    90 |        4 | 2025-01-04 |
| 13 | Apple        | Food        |     2 |       20 | 2025-01-01 |
| 14 | Bread        | Food        |     3 |       15 | 2025-01-02 |
| 15 | Milk         | Food        |     4 |       10 | 2025-01-03 |
| 16 | Cheese       | Food        |     8 |        5 | 2025-01-04 |
| 17 | Notebook     | Stationery  |     5 |       10 | 2025-01-01 |
| 18 | Pen          | Stationery  |     2 |       25 | 2025-01-02 |
| 19 | Marker       | Stationery  |     4 |       12 | 2025-01-03 |
| 20 | Folder       | Stationery  |     6 |        8 | 2025-01-04 |
+----+--------------+-------------+-------+----------+------------+





-- 1- shart   Har bir kategoriya boyicha nechta mahsulot sotilganini toping.

select category, count(*) as sotilgan_mahsulotlar from sales group by category;

+-------------+----------------------+
| category    | sotilgan_mahsulotlar |
+-------------+----------------------+
| Electronics |                    4 |
| Furniture   |                    4 |
| Clothing    |                    4 |
| Food        |                    4 |
| Stationery  |                    4 |
+-------------+----------------------+



-- 2- shart.  Har bir kategoriya boyicha jami sotuv summasini chiqaring.

select category, sum(price) as jami_summa from sales group by category;

+-------------+------------+
| category    | jami_summa |
+-------------+------------+
| Electronics |       2450 |
| Furniture   |       2500 |
| Clothing    |        320 |
| Food        |         17 |
| Stationery  |         17 |
+-------------+------------+


-- 3- shart. Har bir kategoriya boyicha ortacha narxni hisoblang.

select category, avg(price) as ortacha_qiymat from sales group by category;

+-------------+----------------+
| category    | ortacha_qiymat |
+-------------+----------------+
| Electronics |       612.5000 |
| Furniture   |       625.0000 |
| Clothing    |        80.0000 |
| Food        |         4.2500 |
| Stationery  |         4.2500 |
+-------------+----------------+

4- shart  Har bir kun boyicha jami tushumni toping.

select sale_date, sum(price) as kunlik_foyda from sales group by sale_date;

+------------+--------------+
| sale_date  | kunlik_foyda |
+------------+--------------+
| 2025-01-01 |         1747 |
| 2025-01-02 |         1075 |
| 2025-01-03 |         1478 |
| 2025-01-04 |         1004 |
+------------+--------------+


5- shart Faqat Electronics kategoriyasidagi mahsulotlar boyicha umumiy tushumni hisoblang.

select product_name, sum(price) as jami_summa from sales where category="Electronics" group by product_name;

+--------------+------------+
| product_name | jami_summa |
+--------------+------------+
| Laptop       |        800 |
| Phone        |        600 |
| TV           |        900 |
| Headphones   |        150 |
+--------------+------------+

6- shart Jami sotuv summasi 2000 dan katta bolgan kategoriyalarni chiqaring.

select category, sum(price) as jami_summa from sales group by category having sum(price)>2000;

+-------------+------------+
| category    | jami_summa |
+-------------+------------+
| Electronics |       2450 |
| Furniture   |       2500 |
+-------------+------------+

7-shart Ortacha narxi 100 dan yuqori bolgan kategoriyalarni toping.

select category, avg(price) as ortacha_narx from sales group by category having avg(price)>100;

+-------------+--------------+
| category    | ortacha_narx |
+-------------+--------------+
| Electronics |     612.5000 |
| Furniture   |     625.0000 |
+-------------+--------------+


8-shart 2025-01-01 sanasida nechta mahsulot sotilganini aniqlang.

select sale_date,  count(*) as soni from sales group by sale_date ;

+------------+------+
| sale_date  | soni |
+------------+------+
| 2025-01-01 |    6 |
| 2025-01-02 |    5 |
| 2025-01-03 |    5 |
| 2025-01-04 |    4 |
+------------+------+


9-shart Eng kop miqdorda (quantity) sotilgan kategoriyani toping.

select category, sum(quantity) as eng_kop_miqdor from sales group by category order by sum(quantity) desc limit 1;

+------------+----------------+
| category   | eng_kop_miqdor |
+------------+----------------+
| Stationery |             55 |
+------------+----------------+

10-shart 3 martadan kop sotilgan (quantity > 3) mahsulotlar boyicha kategoriyalar kesimida jami tushumni chiqaring.

select category, sum(price) as jami_tushum  from sales where quantity>3 group by category;


+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |         150 |
| Furniture   |         100 |
| Clothing    |         130 |
| Food        |          17 |
| Stationery  |          17 |
+-------------+-------------+