# Table Summary

Here is my understanding of the data structure.

* `orders`
    * one row per order (index = order_id)
    * does not contain information about reorders
    * `eval_set` indicates whether the order is in the `train`/`test`/`prior`
        * the `test` set is data reserved for the testing of our final model
        * the `prior` and `train` eval_sets are defined below
    * columns:
        * `order_id`: order identifier
        * `user_id`: customer identifier
        * `eval_set`: which evaluation set this order belongs in (see `SET` described below)
        * `order_number`: the order sequence number for this user (1 = first, n = nth)
        * `order_dow`: the day of the week the order was placed on
        * `order_hour_of_day`: the hour of the day the order was placed on
        * `days_since_prior`: days since the last order, capped at 30 (with NAs for `order_number` = 1)

* `prior_orders`
    * information about orders prior to that users most recent order (~3.2M orders)
    * contains one row per item per order & whether or not each item is a 'reorder'
        * reorder: 1 if products has been ordered by this user in the past, 0 otherwise
    * columns:
        * `order_id`: foreign key
        * `product_id`: foreign key
        * `add_to_cart_order`: order in which each product was added to cart
        * `reordered`: 1 if this product has been ordered by this user in the past, 0 otherwise
        
    
* `train_orders`
    * training data supplied to participants of Kaggle competition
    * this table represents the users' most recent orders
    * contains one row per item per order & whether or not each item is a 'reorder'(for training data)
    * none of the rows in `train_orders` will be found in `prior_orders`
    * columns:
        * `order_id`: foreign key
        * `product_id`: foreign key
        * `add_to_cart_order`: order in which each product was added to cart
        * `reordered`: 1 if this product has been ordered by this user in the past, 0 otherwise
        
* `prod_detail`
    * this table is a combination of `products.csv`, `aisles.csv`, and `departments.csv`
        * created via SQL script (see `db_create.sql`)
    * contains all product details for each product