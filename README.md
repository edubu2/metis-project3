# Metis Data Science Bootcamp | Project 3 | Classification

(in progress)


## Objective

### Predicting whether an Instacart customer will purchase an item again in the future using Logistic Regression

**By Elliot Wilens, Metis Data Scientist**

Timeline: 2 weeks

This project idea stemmed from a Kaggle Competition in 2018. More information can be found at [kaggle.com](https://www.kaggle.com/c/instacart-market-basket-analysis/overview), but here's a brief synopsis:


*Currently Instacart uses transactional data to develop models that predict which products a user will buy again, try for the first time, or add to their cart next during a session.*


Project instructions (Metis students only) [here](https://github.com/thisismetis/onl_ds5/blob/main/curriculum/project-03/project-03-introduction/project_03.md).

Download the dataset [here](https://www.kaggle.com/c/instacart-market-basket-analysis/data).

Data dictionary [here](https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b).

___
## Applications

This model has two use-cases for Instacart:

1.  **"Buy it again" recommendations in the application**

    ![Buy it Again](etc/buy_again.png)

2.  **"Frequently bought with..." recommendations while shopping for certain products**

    ![Frequently bought with](etc/freq_bought_with.png)

___
## Tech Stack

- Google Cloud Platform VM (Serving Jupyter Notebook & Database in compute engine)
  - not required for local reproduction
- FileZilla (to move files too large for Git to/from GCP VM)
- PostgreSQL
- Python3 Libraries:
    - SQLAlchemy & psycopg2
    - scipy
    - scikit-learn
    - StatsModels
    - pickle
    - pandas & numpy
    - matplotlib & seaborn

- Algorithms:
	- XGBoost
	- Logistic Regression
	- ROC/ AOC (to compare algorithms and probability thresholds)
___
## Steps to Reproduce Locally
1. Fork & clone this repository to your local Github repo/machine
2. Ensure all technologies in the [Tech Stack](#tech-stack) section are installed on your machine
3. From your terminal (located in the root directory of the repo), use the `psql -f code/db_create.sql` command to create and populate the 'instacart' database on your machine.
4. Create a `code/database.ini` file containing your Postgres username and password. Make sure this filename remains in the .gitignore file to keep this information hidden from the public. Here's what it should look like (replace 'username' and 'password' with your Postgres username & password).

    ![db_setup_file.png](etc/db_setup_file.png)
___
## Data Source

**Kaggle Competition (2018): [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data)**

Data originally sourced from “The Instacart Online Grocery Shopping Dataset 2017”, Accessed by Kaggle from [instacart.com](https://www.instacart.com/datasets/grocery-shopping-2017)
