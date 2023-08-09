# Exemple:
#    Execute Postgres Query
curs_obj.execute("""select "id", "Activity", "Location", "Price" from tabEvents LIMIT 10;""")
#Fetch All Records
result = curs_obj.fetchall()

# IMPORTANT: you may encouter this error, if you make mistake in the query
    
# current transaction is aborted, commands ignored until end of transaction block

# to fixe it, execute a ROLLBACK:
    
curs_obj.execute("ROLLBACK")
