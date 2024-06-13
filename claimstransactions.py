import os
import config
#import pymysql

db_host = 'localhost'
db_user = 'root'
db_password = ''  # Replace with your MySQL root password if any
db_name = 'ehr'

# Directory containing CSV files
csv_file = "C:/Users/Nahid/OneDrive/Desktop/Nahid/Synthe_sample_data/claims_transactions.csv"

conn = config.mysql_connecion(db_host,db_name,db_user,db_password)
# conn = pymysql.connect(
#     host=db_host,
#     user=db_user,
#     password=db_password,
#     database=db_name
#     local_infile=1  # Enable local infile option cz I have my file in a random directory instead of XAMPP directory
# )
cursor = conn.cursor()

# Predefined column names array
# columns = 'start_date ,stop_date' ,patient_id' ,
#     'encounter_id' ,
#     'code_',
#     'function_system' ,
#     'allergy_description' ,
#     'allergy_type' ,
#     'category' ,
#     'reaction1' ,
#     'description1' ,
#     'severity1' ,
#     'reaction2' ,
#     'description2',
#     'severity2'"

# Iterate over CSV files and load them into the database

table_name = 'claims_transactions'
    
# Read the first line to get the column names
with open(csv_file, 'r') as f:
   

    # Load CSV data into MySQL table
    load_sql = f"""
    LOAD DATA LOCAL INFILE '{csv_file}'
    INTO TABLE `{table_name}`
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\\n'
    IGNORE 1 ROWS;
    """
    cursor.execute(load_sql)
    conn.commit()


# Close the connection
cursor.close()
conn.close()

print("CSV files have been successfully uploaded to the database.")

