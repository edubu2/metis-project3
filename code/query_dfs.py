import numpy as np
import pandas as pd
import psycopg2

from db_config import get_db_params


def create_dfs(subset=False):
    """
    Takes: subset (int, optional, default False): num_users from 1000

    Returns: four dataFrames (tuple):
        1. df_orders
        2. df_train
        3. df_prior
        4. df_prod (products)
    """

    def establish_conn():
        params = get_db_params()
        conn = psycopg2.connect(**params)

        return conn

    def get_orders(conn):
        """ Creates df_orders. """

        query = """
                    SELECT *
                    FROM orders;
                """

        df_orders = pd.read_sql_query(query, conn)

        return df_orders

    def get_train(conn):
        """ Creates df_train. """

        q = """
                SELECT train_orders.order_id, train_orders.product_id,
                    train_orders.add_to_cart_order, train_orders.reordered,
                    map.user_id, map.eval_set, map.order_number,
                    map.order_dow, map.order_hour_of_day, map.days_since_prior_order
                FROM train_orders
                LEFT JOIN
                    (
                        SELECT * FROM orders
                    ) AS map
                ON train_orders.order_id = map.order_id
            """

        df_train = pd.read_sql_query(q, conn)

        return df_train

    def get_prior(conn):
        """Creates df_prior. """

        q = """
                SELECT prior_orders.order_id, prior_orders.product_id,
                    prior_orders.add_to_cart_order, prior_orders.reordered,
                    map.user_id, map.eval_set, map.order_number,
                    map.order_dow, map.order_hour_of_day, map.days_since_prior_order
                FROM prior_orders
                LEFT JOIN
                    (
                        SELECT * FROM orders
                    ) AS map
                ON prior_orders.order_id = map.order_id
            """

        df_prior = pd.read_sql_query(q, conn)

        return df_prior

    def get_prod_detail(conn):
        """Creates df_prod. """

        q = "SELECT * FROM product_detail"
        df_prod = pd.read_sql_query(q, conn, index_col="product_id")
        return df_prod

    def main():
        conn = establish_conn()
        df_orders = get_orders(conn)
        df_train = get_train(conn)
        df_prior = get_prior(conn)
        df_prod_detail = get_prod_detail(conn)

        return df_orders, df_train, df_prior, df_prod_detail

    df_orders, df_train, df_prior, df_prod_detail = main()
    return df_orders, df_train, df_prior, df_prod_detail


if __name__ == "__main__":
    create_dfs()
