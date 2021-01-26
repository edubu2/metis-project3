/* THIS SCRIPT CREATES THE INSTACART DATABASE FROM SCRATCH */
/* SCRIPT MUST BE RUN FROM JUST OUTSIDE THE 'data/' DIRECTORY */
/* ALL .csv FILES MUST BE STORED IN THE 'data/' DIRECTORY */


CREATE DATABASE instacart;

\connect instacart;

CREATE TABLE aisles(
    aisle_id INT NOT NULL,
    aisle TEXT
);

CREATE TABLE departments(
    department_id INT NOT NULL,
    department TEXT
);

CREATE TABLE orders(
    order_id INT NOT NULL,
    user_id INT,
    eval_set TEXT,
    order_number INT,
    order_dow INT,
    order_hour_of_day INT,
    days_since_prior_order FLOAT
);

CREATE TABLE products(
    product_id INT NOT NULL,
    product_name TEXT NOT NULL,
    aisle_id INT NOT NULL,
    department_id INT NOT NULL
);

\copy aisles FROM 'data/aisles.csv' DELIMITER ',' CSV HEADER;
\copy departments FROM 'data/departments.csv' DELIMITER ',' CSV HEADER;
\copy orders FROM 'data/orders.csv' DELIMITER ',' CSV HEADER;
\copy products FROM 'data/products.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE orders
DROP COLUMN eval_set;
