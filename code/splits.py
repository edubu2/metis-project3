from collections import OrderedDict
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np


def split_users(df, subset=False, test_size=0.2, seed=54):

    rs = np.random.RandomState(seed)

    sample_users = df["user_id"].unique()

    if subset:
        assert (
            0 < subset < 1
        ), "Subset must be a float between 0.00 and 0.99. Otherwise, subset=False"
        cutoff = round(len(sample_users) * subset)
        sample_users = sample_users[:cutoff]

    test_users = rs.choice(
        sample_users, size=int(sample_users.shape[0] * test_size), replace=False
    )

    mask = (~df["user_id"].isin(test_users)) & (df["user_id"].isin(sample_users))
    df_tr = df[mask]  # the '~' means NOT (i.e. includes Bool=False)
    mask = (df["user_id"].isin(test_users)) & (df["user_id"].isin(sample_users))
    df_te = df[mask]

    y_tr, y_te = df_tr["in_cart"], df_te["in_cart"]
    X_tr = df_tr.drop(["product_id", "user_id", "cart", "in_cart", "last_cart"], axis=1)
    X_te = df_te.drop(["product_id", "user_id", "cart", "in_cart", "last_cart"], axis=1)

    print(
        f"""
    X_train sample size: {len(X_tr)}
    X_test sample size: {len(X_te)}"""
    )

    return X_tr, X_te, y_tr, y_te

