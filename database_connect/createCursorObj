import psycopg2

# Connect to Postgre Database Via Python

def connectDB(host="numidia_app.us-east-1.rds.amazonaws.com", database= "advMakersDB"):
    
    con = psycopg2.connect(
        database= database,
        user="postgress",
        password="admin007",
        host=host,
        port=543
    )
    # The cursor() method assists us in executing the Postgres commands from Python
    curs_obj = con.cursor()
    return curs_obj

  
