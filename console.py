import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository  
import repositories.user_repository as user_repository  

task_repository.delete_all()
user_repository.delete_all()

user1 = User('Jenna','Mclowie')
user2 = User('Kirsten','Mclowie')

task1=  Task('Gym','Alex',20,user1,False)
task2 = Task ('Wash Car','Dave',45,user2,True)


user_repository.save(user1)
user_repository.save(user2)
task_repository.save(task1)
task_repository.save(task2)

result = user_repository.select_all()
result = task_repository.select_all()

for task in result:
    print(task.__dict__)

user_repository.tasks(user1)


pdb.set_trace()