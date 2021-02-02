import numpy as np
import pandas as pd
from joblib import Parallel, delayed
import multiprocessing
from datetime import datetime

"""
Calculates (user, product) order_streak for the last n orders.

- positive streaks: user has ordered this product in x consecutive orders.
- negative streaks: user has NOT ordered this product in x consecutive orders.

Returns: Nothing. Saves the 'order_streaks.csv' file in the '../data/' directory.
"""

PRIOR_FP = "../data/order_products__prior.csv"
ORDERS_FP = "../data/orders.csv"
OUT_FP = "../data/order_streaks_2.csv"


def load_input_data():
    """
        Loads CSV files into dtype-optimized DataFrames.

        Returns: df_prior, df_orders.
    """

    df_prior = pd.read_csv(
        PRIOR_FP,
        dtype={
            "order_id": np.int32,
            "product_id": np.uint16,
            "add_to_cart_order": np.int16,
            "reordered": np.int8,
        },
    )

    df_orders = pd.read_csv(
        ORDERS_FP,
        dtype={
            "order_id": np.int32,
            "user_id": np.int64,
            "order_number": np.int16,
            "order_dow": np.int8,
            "order_hour_of_day": np.int8,
            "days_since_prior_order": np.float32,
        },
    )
    return df_prior, df_orders


def apply_parallel(df_groups, _func):
    nthreads = multiprocessing.cpu_count() >> 1
    print(f"num threads used for multiprocessing: {nthreads}")
    # process each group object on
    res = Parallel(n_jobs=nthreads)(delayed(_func)(grp.copy()) for _, grp in df_groups)
    return pd.concat(res)


def add_order_streak(df):
    tmp = df.copy()
    tmp.user_id = 1

    user_prod = tmp.pivot(index="product_id", columns="order_number").fillna(-1)
    user_prod.columns = user_prod.columns.droplevel(0)

    x = np.abs(user_prod.diff(axis=1).fillna(2)).values[:, ::-1]
    df.set_index("product_id", inplace=True)
    df["order_streak"] = np.multiply(np.argmax(x, axis=1) + 1, user_prod.iloc[:, -1])
    df.reset_index(drop=False, inplace=True)
    return df


def main():
    df_prior, df_orders = load_input_data()

    # get the last 6 orders for each user (counting df_prior streak up to 5, but df_orders contains 1 train order)
    df_orders = df_orders.groupby(["user_id"]).tail(6)

    df_prior = df_orders.merge(df_prior, on="order_id")
    streak_cols = ["user_id", "product_id", "order_number"]
    user_groups = df_prior[streak_cols].groupby("user_id")
    df = apply_parallel(user_groups, add_order_streak)

    df = df.drop(columns="order_number").drop_duplicates().reset_index(drop=True)
    final_cols = ["user_id", "product_id", "order_streak"]
    df[final_cols].to_csv(OUT_FP, index=False)


if __name__ == "__main__":
    main()
