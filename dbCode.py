import pymysql
import pymysql.cursors
import creds 

def get_conn():
    """establishes and returns a connection to the MySQL RDS database
    using credentials from my creds.py. uses DictCursor to return 
     query results as dictionaries!!!! """
    
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, args=()):
    """executes an sql query using a conneciton to my rds database
    closes the connection after running the query and returns the results 
    in a list of dictionaries """

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            return cur.fetchall()
    finally:
        conn.close()

def get_top_listings():
    query1 = "SELECT title, price FROM Listings LIMIT 10;"
    top_listings = execute_query(query1)
    return top_listings