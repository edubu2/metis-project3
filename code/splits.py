from collections import OrderedDict
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np


def split_users(df, subset=False, test_size=0.2, seed=36):

    rs = np.random.RandomState(seed)

    total_users = df["user_id"].unique()

    if subset:
        assert (
            0 < subset < 1
        ), "Subset must be a float between 0.00 and 0.99. Otherwise, subset=False"
        cutoff = len(total_users) * subset
        total_users = total_users[:cutoff]

    test_users = rs.choice(
        total_users, size=int(total_users.shape[0] * test_size), replace=False
    )

    mask = df["user_id"].isin(test_users)
    df_tr = df[~mask]  # the '~' means NOT (i.e. includes Bool=False)
    df_te = df[mask]

    y_tr, y_te = df_tr["in_cart"], df_te["in_cart"]
    X_tr = df_tr.drop(["product_id", "user_id", "cart", "in_cart", "last_cart"], axis=1)
    X_te = df_te.drop(["product_id", "user_id", "cart", "in_cart", "last_cart"], axis=1)

    print(f"Actual Test Size: {y_te.shape[0] / df.shape[0]:0.4}")

    return X_tr, X_te, y_tr, y_te

