import pandas as pd
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Fetch data into DataFrames
def fetch_table_data(table_name):
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, connection)
    return df

# Fetch data from two tables
table1_name = 'table1'
table2_name = 'table2'
df1 = fetch_table_data(table1_name)
df2 = fetch_table_data(table2_name)

# Check if the number of rows is the same
if len(df1) != len(df2):
    print("Number of rows in tables are different")
else:
    print("Number of rows in tables are the same")

# Check if the columns are the same
if list(df1.columns) != list(df2.columns):
    print("Columns in tables are different")
else:
    print("Columns in tables are the same")

# Check if data is the same
if df1.equals(df2):
    print("Data in tables are identical")
else:
    print("Data in tables are different")

# Close the database connection
connection.close()