CREATE DATABASE shop;

USE shop;

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON shop . * TO 'admin'@'localhost';

CREATE USER 'viewer'@'localhost' IDENTIFIED BY 'password';

GRANT SELECT ON shop . * TO 'admin'@'localhost';

create table categories
(   
    categories_id int PRIMARY KEY AUTO_INCREMENT,
    cat_name varchar(128) not NULL
);


insert into categories(cat_name)
    values
        ('Sensors'),
        ('Modules'),
        ('Displays'),
        ('Drones'),
        ('RC components')

create table product
(
    product_id int PRIMARY KEY AUTO_INCREMENT,
    prod_cat varchar(128) not NULL,
    prod_name text not NULL,
    prod_price real not NULL,   
    fk_categories_id integer references categories(categories_id) not NULL
)

insert into     
    product(prod_cat, prod_name, prod_price, fk_categories_id)
    values
        ('Sensors', 'IR camera', 920.0, 1),
        ('Modules', 'RFID', 100, 2),
        ('Displays', 'NEO Pixel', 75, 3),
        ('Drones', 'LiPo 3S', 440, 4),
        ('RC components', 'DAC', 120.0, 5),
        ('Sensors', 'Temp sensor', 100, 1),
        ('Modules', 'FM Radio', 35, 2),
        ('Displays', 'TFT LCD', 265, 3),
        ('Drones', 'ESC controler', 100, 4),
        ('RC components', 'UF Led', 50.0, 5),
        ('Sensors', 'Humidity sensor', 100, 1),
        ('Modules', 'Clock generator', 205, 2),
        ('Displays', 'OLED I2C', 125, 3),
        ('Drones', 'XT60 connector', 60, 4),
        ('RC components', 'Capacitor', 0.65, 5)

update product 
    set prod_price = 350.00 
    where product_id = 1

update product 
    set prod_price = prod_price * 1.1

delete from product 
    where product_id = 2

select * from product 
    order by prod_name

select * from product 
    order by prod_price desc

select * from product 
    order by prod_price desc limit 3

select * from product 
    order by prod_price limit 3

select * from product 
    order by prod_price desc limit 3 offset 3

select prod_name 
    from product 
        where prod_price = (select max(prod_price) from product)

select prod_name 
    from product 
        where prod_price = (select min(prod_price) from product)

select count(*) 
    from product 

select sum(prod_price)/count(*) as mean
    from product 
    
CREATE VIEW  the_cheapest AS select * from product order by prod_price desc limit 3