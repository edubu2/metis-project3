# Metis Data Science Bootcamp | Project 3 | Classification

(in progress)


## Objective

### Identifying which items should be highlighted to the user in Instacart's 'Buy it Again' feature

**By Elliot Wilens, Metis Data Scientist**

Timeline: 2 weeks

This project idea stemmed from a Kaggle Competition in 2018. More information can be found at [kaggle.com](https://www.kaggle.com/c/instacart-market-basket-analysis/overview), but here's a brief synopsis:


*Currently Instacart uses transactional data to develop models that predict which products a user will buy again, try for the first time, or add to their cart next during a session.*

DISCLAIMER: I am in no way affiliated with Instacart and did not make any Kaggle submissions, since the competition ended a couple years ago.

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

These are important to keep in mind, as my focus for the project is to help Instacart maximize conversion rates with these features. 
___
## Tech Stack

- PostgreSQL
- Google Cloud Platform VM (Serving Jupyter Notebook & Database in compute engine)
  - not required for local reproduction
  - two VMs used:
    - for analysis & feature engineering
      - machine type: N2 10vCPU, 64GB memory 
    - for training models & parameter optimization (grid search CV)
      - machine type: N2, 16 vCPU, 64GB memory 
- Tableau for EDA (Exploratory Data Analysis)
- FileZilla (to move files too large for Git to/from GCP VM)
- Python3 Libraries:
    - pyscopg2
    - scikit-learn
    - StatsModels
    - multiprocessing
    - pickle
    - pandas & numpy
    - matplotlib & seaborn

- Classification Algorithms:
    - RandomForest
	- XGBoost
	- Logistic Regression
- Modeling techniques
  - Grid Search for parameter optimization
  - K-Fold (5) cross-validation for model comparison
  - Precision/Recall curves for probability threshold determination
  - Confusion matrices to evaluate metrics and K-Fold
  - F-beta (beta=2) scoring instead of F-1 due to class imbalance and prioritization of recall
___
## Steps to Reproduce Locally
1. Fork & clone this repository to your local Github repo/machine
2. Ensure all technologies in the [Tech Stack](#tech-stack) section are installed on your machine
3. From your terminal (located in the root directory of the repo), use the `psql -f code/db_create.sql` command to create and populate the 'instacart' database on your machine.
4. Create an empty directory named `pickle` within the `metis-project3/code/` directory.
5. Create an empty directory named `models` within the same directory as above
6. Create a `code/database.ini` file containing your Postgres username and password. Make sure this filename remains in the .gitignore file to keep this information hidden from the public. Here's what it should look like (replace 'username' and 'password' with your Postgres username & password).

    ![db_setup_file.png](etc/db_setup_file.png)

___
## Feature Engineering

I looked at Kaggle-winning projects to get an idea of what features did and did not work. Thank you Kaggle!

There are three different types of features that I used:
* product features
    * total unit sales
    * total unit reorders
    * unit reorder percentage
* user features
  * average order size
  * average time between orders
  * time since last order
  * last cart
* **user_product features**
  * streak
    * how many times in a row did the user purchase this product?
    * also captures 'negative streaks'
      * example: if user *x* purchased product *y* three orders ago, but has not purcased since, streak = -2
  * last five purchases
    * of User *x*'s last five orders, how many times did they buy product *y*?
  * last five purchase ratio
    * the above value divided by 5
    * thank you to [Kazuki Onodera](https://medium.com/kaggle-blog/instacart-market-basket-analysis-feda2700cded) for finding this. Without it, the 'last five purchases' feature did not yield much predictive value for the model

There were 32 features in total. The above are the ones that provided the most impact on the model (based on F-2 scores from running the model with & without them)

___
## Model Selection

___
## Metric Selection

___
## Model Evaluation

___
## Data Source

**Kaggle Competition (2018): [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data)**

Data originally sourced from “The Instacart Online Grocery Shopping Dataset 2017”, Accessed by Kaggle from [instacart.com](https://www.instacart.com/datasets/grocery-shopping-2017)
