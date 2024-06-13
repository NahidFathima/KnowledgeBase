import pymysql

# Connect to the database
def mysql_connecion (db_host, db_name, db_user, db_password=""):
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        local_infile=1
    )

    return conn


# db_host='localhost'
# user='root'
# password=''
# db='patientdb'

# # positional Reference
# # conn = mysql_connecion(db_host, user, db, password)
# # conn = mysql_connecion(db_host, user, db)
# # conn = mysql_connecion(db_host, user)
# conn = mysql_connecion(db_host)

# # Named reference
# conn = mysql_connecion(db_host=db_host, db_user=user, db_password=password, db_name=db)
# conn = mysql_connecion(db_host=db_host, db_user=user)
# conn = mysql_connecion(db_name=db, db_host=db_host, db_user=user, db_password=password)
