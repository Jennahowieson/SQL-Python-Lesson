import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        # connect to the DB
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        # define a cursor
        cur.execute(sql, values)
        # execute the SQL
        conn.commit()
        # commit
        results = cur.fetchall()
        # fetch the results
        cur.close()           
        # close the connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # print an error
    finally:
        if conn is not None:
            conn.close()
            # close the connection
    return results
    # return the results