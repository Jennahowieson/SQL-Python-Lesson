from db.run_sql import run_sql

from models.user import User
  
def select(id):
    user= None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        user = User(result['first_name'], result['last_name'])
    return user

def select_all():  
    users = [] 

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['last_name'],row['id'])
        users.append(user)
    return users 

def update(user):
    sql= "UPDATE users SET (first_name, last_name) = (%s,%s) WHERE id =%s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

def save(user):
    sql= "INSERT INTO users (first_name, last_name) VALUES (%s,%s) RETURNING *"
    values = [user.first_name, user.last_name]
    results =run_sql(sql,values)
    id = results[0]['id']
    user.id = id
    print(results)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

# Add a function to the user_repository that returns all the task objects for a user

def tasks(user):
    sql= "SELECT * from tasks where user_id = %s"
    values = [user.id]
    results = run_sql(sql,values)
    print (results)






