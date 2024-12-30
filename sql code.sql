use training;
//Task-1
create table users(user_id int(10) primary key,name varchar(50),email varchar(100));
insert into users values('1','Archana','archana11@gmail.com'),('2','Rachana','rachana22@gmail.com');
select * from users;
Create table orders(order_id int(20) primary key,user_id int(65), foreign key (user_id) references users(user_id),status varchar(35));
insert into orders values ('10','1','completed'),('20','2','pending');
select * from orders;
select u.name AS user_name,(select count(*)from orders o where o.user_id=u.user_id) AS total_orders from users u;
//Task-2
create table student(studentid int(20),studentname varchar(45));
insert into student values ('1','Archana'),('2','Rachana'),('3','Chaithu'),('4','Thrishu'),('5','Madhu');
select * from students;
create table course(courseid int(30),coursename varchar(30));
insert into  course values('111','Cse'),('222','IT'),('333','EEE'),('444','AIML'),('555','DS'); 
select * from course;
create table enrollment(studentid int(30),courseid int(45));
insert into enrollment values('1','111'),('2','222'),('3','333'),('4','444'),('5','555');
select * from enrollment;
select studentname,coursename from student join enrollment on student.studentid=enrollment.studentid join course on enrollment.courseid=course.courseid;
//Task-3
create  table customer(customerId int(20),firstname varchar(50),lastname varchar(50),phone int(100));
insert into customer values('1','Archana','Gudla','111253987'),('2','Rachana','Rudhra','546756987');
select * from customer;
create table sales(saleId int(20),productId int(30),customerId int(40),Quantity int(40), totalamount int(100));
insert into sales values('1','1','1','1','1000'),('2','2','2','2','2000'),('3','3','3','3','3000');
select * from sales;
create table product(product_id int(40),productName varchar(45), price int(45));
insert into product values('1','laptop','1000'),('2','smartphone','3000'),('3','Tab','4000'),('4','smartwatch','6000'),('5','fan','5500');
select * from product;
truncate table product;
select productname,totalamount from sales join product on product.product_id=sales.productid;
//Task-4
create table employees(Employeeid int(35),firstname varchar(50),lastname varchar(50),Department varchar(40),salary int(50),managerId int(40));
insert into employees values('1','archana','aa','cse','25000','11'),('2','rachana','rr','IT','35000','22'),('3','chaithu','cc','EEE','30000','33'),('4','Madhu','mm','AIML','40000','44'),('5','thrishan','tt','DS','50000','55');
select employeeid,firstname,lastname,managerid from employees;
select * from employees;
drop  table employees;  
//Task-5
create table store(productID int(20),productName varchar(50),price int(50),selling int(50));
insert into store values('1','laptop','45000','4'),('2','mobile','55000','1'),('3','Fan','35000','7'),('4','tab','20000','3'),('5','smartwatch','10000','8');
select productid,productname, price,selling from store order by selling Desc limit 5;
select * from store;
drop table store;
//Task-6
create table student(studentId int(40) primary key,studentName varchar(30));
insert into student values(1111,'Archana'),(2222,'Rachana'),(3333,'Madhu'),(4444,'chinnu'),(5555,'Chaithu');
drop table student;
select * from student;
create table course(courseId int(30) primary key,courseName varchar(40));
insert into course values('1','Hr'),('2','Java'),('3','Python'),('4','c++'),('5','devops');
drop table course;
select * from course;
create table grades(gradeId int(30),studentId int(40),studentName varchar(50),courseId int(30),grade int(50),foreign key (studentId) references  student(studentId));
insert into grades values('11','1111','Archana','1','90');
insert into grades values('12','2222','Rachana','2','70');
insert into grades values('13','3333','Madhu','3','78');
insert into grades values('14','4444','chinnu','4','80');
insert into grades values('15','5555','chaithu','5','95');
select * from grades;
drop table grades;
select studentName,(select avg(grade) from grades where grades.studentid=studentId) as average_grade from student;

//Task 7
Create table socialmedia(medianame varchar(20),friends int(10),followers int(10),following int(10));
select * from socialmedia;
drop table socialmedia;
insert into socialmedia values('Bear','11','1000','599');
insert into socialmedia values('shine','22','800','300');
insert into socialmedia values('tinku','60','987','504');
insert into socialmedia values('rosie','78','768','659');
insert into socialmedia values('sweety','89','436','667');
SELECT * FROM socialmedia WHERE friends = (SELECT MAX(friends) FROM socialmedia);

//task8:
create table employes(Employeeid int(35),firstname varchar(50),lastname varchar(50),DepartmentId int(40),salary int(50),managerId int(40));
insert into employes values('1','archana','aa','100','25000','50');
insert into employes values('2','Rachana','rr','200','55000','20');
insert into employes values('2','Chaithu','cc','300','56000','7');
insert into employes values('3','Madhu','mm','400','63000','8');
insert into employes values('4','Thrush','tt','500',70000,'9');
select * from employes;
where:
select * from employes where salary=63000;
AND:
select * from employees where salary between 25000 and 50000;
OR:
select * from employes where salary=25000 or salary=60000;
Not:
select * from employes where not salary<63000;
AND,OR,NOT:
select * from employes where firstname='archana' and salary=25

drop table employes;
create table Department(Departmentname varchar(50),DepartmentId int(45));
insert into Department values('EEE','1'),('CSE','2'),('MECH','3'),('CIVL','4'),('CCP','5');
select * from department;
drop table department;
select count(employeeid) as total,departmentname from department join employe on employe.departmentId=departments.departmentid group by department.departmentname;

create table product(product_id int(40),productName varchar(45), price int(45),quamtity int(40));
insert into product values('1','laptop','1000','5'),('2','smartphone','3000','4'),('3','Tab','4000','7'),('4','smartwatch','6000',23),('5','fan','5500','10');
select productname,product_id from product where quamtity<10;
select * from product;
drop table product;


//task 10;
drop table customer;
CREATE TABLE customer (CustomerID INT(10) PRIMARY KEY, CustomerName VARCHAR(100));
INSERT INTO customer VALUES (1,'shaiaja'),(2,'sreekar'),(3,'kiran');
select * from customer;
drop table customer;
CREATE TABLE orders (OrderID INT(10) PRIMARY KEY,CustomerID INT(10), TotalAmount DECIMAL(10, 2),FOREIGN KEY (CustomerID) REFERENCES customer(CustomerID)  );
INSERT INTO orders  VALUES ( 101, 1,150.00),  (102,2, 200.00), (103,3, 300.00); 
select * from orders;
drop table orders;

select customername,avg(totalamount) from customer join orders on customer.customerid=orders.customerid group by customername;


//task11:

CREATE TABLE Movies (MovieID INT PRIMARY KEY,Title VARCHAR(255) NOT NULL,ReleaseYear INT,Genre VARCHAR(100));
INSERT INTO Movies (MovieID, Title, ReleaseYear, Genre) VALUES
(1, 'Inception', 2010, 'Sci-Fi'),
(2, 'The Godfather', 1972, 'Crime'),
(3, 'The Dark Knight', 2008, 'Action'),
(4, 'Pulp Fiction', 1994, 'Crime'),
(5, 'The Shawshank Redemption', 1994, 'Drama'),
(6, 'Forrest Gump', 1994, 'Drama');
select * from movies;

CREATE TABLE Ratings (RatingID INT PRIMARY KEY,MovieID INT NOT NULL,UserID INT NOT NULL,Rating DECIMAL(3, 2) CHECK (Rating >= 0 AND Rating <= 10),FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
);
INSERT INTO Ratings (RatingID, MovieID, UserID, Rating) VALUES
(1, 1, 101, 9.5),
(2, 1, 102, 9.0),
(3, 2, 103, 9.8),
(4, 3, 104, 9.7),
(5, 3, 105, 9.6),
(6, 4, 106, 9.4),
(7, 4, 107, 9.2),
(8, 5, 108, 9.9),
(9, 6, 109, 9.1),
(10, 6, 110, 8.9);
select * from Ratings;
SELECT 
    M.MovieID,
    M.Title,
    AVG(R.Rating) AS AverageRating
FROM 
    Movies M
JOIN 
    Ratings R
ON 
    M.MovieID = R.MovieID
GROUP BY 
    M.MovieID, M.Title
ORDER BY 
    AverageRating DESC
LIMIT 5;

//task12:
CREATE TABLE Invoices (InvoiceID INT PRIMARY KEY,CustomerID INT NOT NULL,InvoiceDate DATE NOT NULL,TotalAmount DECIMAL(10, 2) NOT NULL);

INSERT INTO Invoices (InvoiceID, CustomerID, InvoiceDate, TotalAmount) VALUES
(1, 101, '2024-01-01', 500.00),
(2, 102, '2024-01-05', 300.00),
(3, 103, '2024-01-10', 450.00),
(4, 104, '2024-01-15', 600.00),
(5, 105, '2024-01-20', 250.00);
select * from Invoices ;

CREATE TABLE Payments (PaymentID INT PRIMARY KEY,InvoiceID INT NOT NULL,PaymentDate DATE NOT NULL,AmountPaid DECIMAL(10, 2) NOT NULL,FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
);
INSERT INTO Payments (PaymentID, InvoiceID, PaymentDate, AmountPaid) VALUES
(1, 1, '2024-01-02', 500.00),
(2, 2, '2024-01-06', 150.00),
(3, 5, '2024-01-21', 250.00);
select * from payments;

SELECT 
    I.InvoiceID,I.CustomerID,I.InvoiceDate,I.TotalAmount,COALESCE(SUM(P.AmountPaid), 0) AS TotalPaid,(I.TotalAmount - COALESCE(SUM(P.AmountPaid), 0)) AS UnpaidAmount
FROM 
    Invoices I LEFT JOIN Payments P ON I.InvoiceID = P.InvoiceID GROUP BY I.InvoiceID, I.CustomerID, I.InvoiceDate, I.TotalAmount HAVING (I.TotalAmount - COALESCE(SUM(P.AmountPaid), 0)) > 0
ORDER BY 
    I.InvoiceDate;
    
    //joins:
create database joins
use joins;
create table student(studentid int(20) primary key,firstname varchar(45),lastname varchar(50),Age int(50),mail varchar(65));
insert into student values ('1','Archana','Gudla',21,'archana11@gmail.com'),('2','Rachana','Rudhra',25,'rachana22@gmail.com'),('3','Chaithu','Chandham',19,'chaithu33@gmail.com'),('4','Thrishu','Manthena',17,'thrishu44@gmail.com'),('5','Madhu','Panjala',24,'madhu55@gmail.com');
select * from student;
drop table student;
create table course(courseId int(30) primary key,courseName varchar(40),studentid int(10),foreign key (studentid) references student (studentid));
insert into course values('101','Hr','1'),('102','Java','2'),('103','Python','3'),('104','C++','4'),('105','devops','5');
select * from course;
select firstname,lastname,age,courseName from student inner join course on student.studentId=course.studentId;
select firstname,age,mail,coursename from student left outer join course on student.studentId=course.studentId;
select *from student right join course on student.studentId=course.studentId;
select firstname,age,courseId,courseName from student cross join course;
select * from student self join student;

create database archu;
use archu;
    create table archana(name varchar(40),age int(30),Id int(20) primary key); 
    insert into archana values('Archana','21','1111'),('Rachana','25','2222'); 
    select * from archana;
    drop table archana;
    
    create table employee(name varchar(40),salary int(40),employeeId int(40) primary key,foreign key (employeeId) references archana(ID));
    insert into employee values('Archana','500000','1111'),('Rachana','100000','2222');
    drop table employee;
    create table employes(Employeeid int(60),firstname varchar(50),lastname varchar(50),DepartmentId int(40),salary int(50),managerId int(40));
insert into employes values('1','archana','aa','100','25000','50');
insert into employes values('2','Rachana','rr','200','55000','20');
insert into employes values('2','Chaithu','cc','300','56000','7');
insert into employes values('3','Madhu','mm','400','63000','8');
insert into employes values('4','Thrush','tt','500',70000,'9');
select * from employes;
create table grades(gradeId int(30),studentId int(40),studentName varchar(50),courseId int(30),grade int(50),foreign key (studentId) references  student(studentId));
insert into grades values('11','1111','Archana','1','90');
insert into grades values('12','2222','Rachana','2','70');
insert into grades values('13','3333','Madhu','3','78');
insert into grades values('14','4444','chinnu','4','80');
insert into grades values('15','5555','chaithu','5','95');
select * from grades;
drop table grades;
//contraints:
create table archana(Id int not null,lastname varchar(50) not null,firstname varchar(60) not null,age int(50));
insert into archana(id,lastname,firstname) values('1','archana','gudla'),('2','rachana','gudla');
select * from archana;
//select
    select * from archana;
    SELECT name, age from archana;
//where
select * from archana where age=19;
select * from archana where lastname='archana';
//AND
select * from employes where managerid between 20 and 50;
//OR
select * from employes where salary=25000 or salary=50000;
//Not
select * from employes where Not salary<100000;   
//And, OR, Not
select * from employes where firstname='archana' and(salary=25000 or employeeid=1); 
//order By
select * from  employes order By  salary desc;
select * from  employes order by employeeid asc;
select * from employes order by departmentId asc;
select * from employes order by firstname asc;
//insert into
 insert into employes values('1','archana','aa','100','25000','50');
select * from employes;
//null
select firstname from employes where firstname is null;
select salary from employes where salary is null;
//not null
select firstname from employes where firstname is not null
select lastname from employes where lastname is not null;
//update
update employes set firstname='sairam' where employeeid='1';
select  emlosalary=55000, where firdtname=
select * from employes; altercreate
//
create table newemployees(name varchar (40) not null, designation varchar (50) not null,work_data date, working_hours int(50));
insert into newemployees values('chinnu','JE','2024-11-08','10');
insert into newemployees values('Rachana','SE','2024-05-27','8');
insert into newemployees values('madhu','Trainee','2023-12-18','10');
insert into newemployees values('chaith','SD','2024-12-05','8');
insert into newemployees values('niru','DE','2024-12-06','10');
select * from newemployees;
drop table newemployees;

create databse triggers;
use triggers;
drop database triggers;
create table newjoineer(emp_id int(10),emp_name varchar(40),emp_age int(20),emp_designation varchar(40));
insert into newjoineer values('100','Archana','21','SSD'),('200','Rachana','-1','SE'),('300','Chaithu','18','DE'),('400','sairam','24','JSE'),('400','Madhu','22','AE');
select * from newjoineer;
DELIMITER //
CREATE TRIGGER age_verify
BEFORE INSERT ON newjoineer
FOR EACH ROW
BEGIN
    IF new.emp_age < 0 THEN
        SET new.emp_age = 0;
    END IF;
END //
DELIMITER ;
insert into newjoineer values('100','Archana','21','SSD'),('200','Rachana','-1','SE'),('300','Chaithu','18','DE'),('400','sairam','24','JSE'),('400','Madhu','22','AE');
select * from newjoineer;
drop table newjoineer;

Task 05/12/2024
create database indexs
use indexs
CREATE TABLE collage (clg_id INT,clg_name VARCHAR(20),emp_name VARCHAR(50),emp_id INT,emp_age INT);
insert into collage values('1','SMIC','Archana','11','21','00');
insert into collage values('2','SMIC','Rachana','22','18','01');
insert into collage values('3','SMIC','Chaithu','33','16','02');
insert into collage values('4','SMIC','sairam','44','19','03');
insert into collage values('5','SMIC','tharun','55','25','04');
insert into collage values('6','SMIC','varun','66','18','05');
insert into collage values('7','SMIC','Rohith','77','23','06');
insert into collage values('8','SMIC','thrish','88','30','07');
select * from collage
drop table collage;
DELIMITER //
CREATE TRIGGER emp_id;
BEFORE INSERT ON collage
FOR EACH ROW
BEGIN
    IF new.emp_id < 0 THEN
        SET new.emp_id = 0;
    END IF;
END //
DELIMITER//
select * from  employes order by employeeid asc;
ALTER TABLE collage
ADD Clg_code int(10);
select * from collage;
insert into collage values('1','SMIC','Archana','11','21','123');
insert into collage values('2','SMIC','Rachana','22','18','456');
insert into collage values('3','SMIC','Chaithu','33','16','789');
insert into collage values('4','SMIC','sairam','44','19','101');
insert into collage values('5','SMIC','tharun','55','25','102');
insert into collage values('6','SMIC','varun','66','18','103');
insert into collage values('7','SMIC','Rohith','77','23','104');
insert into collage values('8','SMIC','thrish','88','30','105');
select * from collage;





create database task;
use task;
CREATE TABLE suppliers (supplier_ID INT(100) PRIMARY KEY,supplier_name VARCHAR(50) NOT NULL);
insert into suppliers values('1','Flipcart'),('2','amazon'),('3','Dmart'),('4','blinkit'),('5','Ajio'),('6','meeshow'),('7','BigBasket'),('8','Zepto');
select * from suppliers;

CREATE TABLE categories (category_ID INT(100)  PRIMARY KEY,category_name varchar(50) NOT NULL);
insert into categories values('11','Electronics'),('22','Clothing'),('33','Kitchen Essentials'),('44','Food'),('55','cosmetics'),('66','jewelry'),('77','Fruits and Vegetables'),('88','groceries');
select * from categories;
drop table categories;

CREATE TABLE Products (
    Product_ID INT(100) PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Supplier_ID INT(100),
    Category_ID INT(100),
    QuantityPerUnit int(100),
    UnitPrice INT(100),
    UnitsInStock INT(100),
    UnitsOnOrder INT(100),
    ReorderLevel INT(100),
    Discontinued BOOLEAN NOT NULL DEFAULT 0,
    foreign key (Supplier_id) references suppliers(Supplier_ID),
    foreign key (category_ID) references categories(category_ID));
    select * from products;
  
INSERT INTO products VALUES 
 ('111', 'Earbuds', '1', '11', '1', '50', '20', '40', '1', 0),
 ('222', 'Kurthi', '2', '22', '2', '12', '30', '50', '3', 1),
 ('333', 'Non-stick pan', '3', '33', '30', '1000', '40', '60', '4', 0),
 ('444', 'Biriyani', '4', '44', '4', '80', '50', '55', '1', 0),
 ('555', 'Lipstick', '5', '55', '5', '13', '52', '35', '2', 1),
 ('666', 'ear rings', '6', '66', '6', '76', '39', '16', '5', 1),
 ('777', 'Tamatos', '7', '77', '7', '70', '12', '22', '1', 0),
 ('670', 'burger', '8', '88', '10', '55', '11', '63', '12', 1),
 ('121', 'dosa', '8', '88', '1', '15', '4', '17', '9', 1),
 ('453', 'fastfood', '8', '88', '18', '55', '2', '7', '6', 0),
 ('879', 'bangles', '6', '66', '30', '20', '59', '10', '7', 1),
 ('675', 'mandi', '8', '88', '8', '97', '94', '37', '6', 0);

1.Write a MySQL query to get Product list (id, name, unit price) where products cost between $15 and 25 rupees.
SELECT product_id, product_name, unitprice FROM products WHERE unitprice BETWEEN 15 AND 25;

2.Write a MySQL query to get Product list (name, unit price) of above average price.
SELECT product_name, unitprice FROM products WHERE unitprice > (SELECT AVG(unitprice) FROM products);

3.Write a MySQL query to get Product list (name, unit price) of ten most expensive products.
SELECT product_name, unitprice FROM products ORDER BY unitprice DESC LIMIT 10;

4.Write a MySQL query to count current and discontinued products.
SELECT Discontinued, COUNT(*) AS product_count FROM products GROUP BY Discontinued;

5.Write a MySQL query to get Product list (name, units on order , units in stock) of stock is less than the quantity on order.
SELECT product_name, UnitsOnOrder, UnitsInStock FROM products WHERE UnitsInStock < UnitsOnOrder;

Task 1;
6.Write a mysql query to get Product name and quantity/unit.
SELECT product_name, quantityperunit FROM products;

7.Write a MySQL query to get current Product list (Product ID and name).
SELECT product_id, product_name FROM products order by product_id;

8.Write a MySQL query to get discontinued Product list (Product ID and name).
SELECT product_id, product_name FROM products WHERE Discontinued = '0' order by product_id;


9.Write a MySQL query to get most expense and least expensive Product list (name and unit price).
select product_name,unitprice from products where unitprice=(select max(unitprice) from products) or unitprice=(select min(unitprice) from products);

10.Write a MySQL query to get Product list (id, name, unit price) where current products cost less than 20 rupees.
SELECT product_id, product_name, unitprice FROM products WHERE Discontinued = 'Discontinued' AND unitprice < 20;

drop table products;
drop table suppliers;
drop table categories;

select product_id from products order by product_id asc;
