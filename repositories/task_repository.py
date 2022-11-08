from db.run_sql import run_sql

from models.task import Task
import repositories.user_repository as user_repository
  
def select(id):
    tasks= None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        task = Task(result['description'], result['assignee'], result['duration'],user,result['user'],result['completed'])
    return task

def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task(row['description'], row['assignee'], row['duration'],user, row['completed'], row['id'] )
        tasks.append(task)
    return tasks

def update(task):
    sql= "UPDATE tasks SET (description, assignee, duration, user_id, completed) = (%s,%s,%s,%s,%s) WHERE id =%s"
    values = [task.description, task.assignee, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)

def save(task):
    # Create a string that is an SQL statement. Insert a row and return that row.
    sql_string = """INSERT INTO tasks (description, assignee, duration, user_id, completed) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *"""
    # Create list of the actual values to insert
    values = [task.description, task.assignee, task.duration, task.user.id, task.completed]
    
    # Pass the SQL string and the actual values to the run file
    results = run_sql(sql_string, values)

    #  Gather up the PRIMARY KEY that was assigned to the new row
    id = results[0]['id']
    
    # Add the id to the task object 
    task.id = id 

    # Return the task
    return task

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)