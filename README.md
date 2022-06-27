
# Data pipeline Movielens 20M dataset 
The dataset is avaiable at the follwing link:

https://files.grouplens.org/datasets/movielens/ml-20m.zip

The main aim of the project is to develop a data ingestion pipeline to load movielens dataset into a database by following the ETL approach.
In addition, a datawarehouse model for the dataset has been proposed. In last step, an API service is developed to retrieve the movie information based
on the year range, genre and the ratings. Hence, the project can be sub-catagorized into 4 different task. 

### 1. Data extraction and transformation
### 2. Loading data into a database
### 3. Datawarehouse model 
### 4. API service to execute queries agains the database

The detailed documentation has been provided in each folder for each task either as markdown cells or python comments. 
The solution to each of these tasks is proided in the accompanying folder.


# Used Technologiess:
Python (pandas), jupyter notebook, Flask and Sqlite

# Methodology

The data is loaded into pandas dataframe, transformed and loaded into as table into a sqlite database. An additional database is created to aggregate data, so that a single table is queried
for creating API service. This can be be found in Task_1_2 folder with additional documentation as markdown

The API service was created using Flask and a python script containing the Flask app. This can be found in Task_4 folder with additional documentation in script files.

# Running API service 
To run the API service, the notebook in folder Task_1_2 need to be run first. This is becuae the code in the notebook generate the database used for querying the database in Flask app.
Afterwards run the app.py script from Task_4 folder.





