sqlite3 shop.db

n/a

n/a

n/a

n/a

create table categories
(   
    categories_id int PRIMARY KEY,
    cat_name varchar(128) not NULL
);


insert into categories(categories_id, cat_name)
    values
        (1, 'Sensors'),
        (2, 'Modules'),
        (3, 'Displays'),
        (4, 'Drones'),
        (5, 'RC components')

create table product
(
    product_id int PRIMARY KEY,
    prod_cat varchar(128) not NULL,
    prod_name text not NULL,
    prod_price real not NULL,   
    fk_categories_id integer references categories(categories_id) not NULL
)

insert into     
    product(product_id, prod_cat, prod_name, prod_price, fk_categories_id)
    values
        (1, 'Sensors', 'IR camera', 920.0, 1),
        (2, 'Modules', 'RFID', 100, 2),
        (3, 'Displays', 'NEO Pixel', 75, 3),
        (4, 'Drones', 'LiPo 3S', 440, 4),
        (5, 'RC components', 'DAC', 120.0, 5),
        (6, 'Sensors', 'Temp sensor', 100, 1),
        (7, 'Modules', 'FM Radio', 35, 2),
        (8, 'Displays', 'TFT LCD', 265, 3),
        (9, 'Drones', 'ESC controler', 100, 4),
        (10, 'RC components', 'UF Led', 50.0, 5),
        (11,'Sensors', 'Humidity sensor', 100, 1),
        (12, 'Modules', 'Clock generator', 205, 2),
        (13, 'Displays', 'OLED I2C', 125, 3),
        (14, 'Drones', 'XT60 connector', 60, 4),
        (15, 'RC components', 'Capacitor', 0.65, 5)

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