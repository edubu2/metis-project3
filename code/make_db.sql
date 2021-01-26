/* THIS SCRIPT CREATES THE INSTACART DATABASE FROM SCRATCH */
/* SCRIPT MUST BE RUN FROM JUST OUTSIDE THE 'data/' DIRECTORY */
/* ALL .csv FILES MUST BE STORED IN THE 'data/' DIRECTORY */


CREATE DATABASE instacart;

\connect instacart;

CREATE TABLE aisles(
    aisle_id INT NOT NULL,
    aisle TEXT NOT NULL
);

CREATE TABLE departments(
    department_id INT NOT NULL,
    department TEXT NOT NULL
);

CREATE TABLE orders(
    order_id INT NOT NULL,
    user_id INT,
    eval_set TEXT,
    order_number INT NOT NULL,
    order_dow INT NOT NULL,
    order_hour_of_day INT NOT NULL,
    days_since_prior_order FLOAT
);

CREATE TABLE prior_orders(
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    add_to_cart_order INT NOT NULL,
    reordered INT
);

CREATE TABLE train_orders(
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    add_to_cart_order INT NOT NULL,
    reordered INT
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
\copy train_orders FROM 'data/order_products__train.csv' DELIMITER ',' CSV HEADER;
\copy prior_orders FROM 'data/order_products__prior.csv' DELIMITER ',' CSV HEADER;


