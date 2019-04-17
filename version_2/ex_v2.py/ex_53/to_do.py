

#I don't want to use a class variable b/c 
#the class will create nay number of to do lists 
#the instance deals with one indiviudal to do list

#ask for input outside of the class and feed input into class

#What are the nouns in the prob statement? Those should be attributes

class ToDoList(object):
    

    def __init__(self, task, completed_task='', show_task = ''):
        self.tasks = task
        self.completed_task = completed_task
        self.show_task = show_task

        # self.usertask = self.add_task_to_list(task)
        
    # def add_task_to_list(self, task):
    #     if task == '':
    #         continue
    #     else:
    #         self.tasks.append(task)
    #     print(self.tasks)

task = []
while True:
    user_task = input("Enter a task. Or hit return if finished: ")
    if user_task == '':
        break
    else:
        task.append(user_task)

todo = ToDoList(task, 'cook')


###Create methods: add a new task, and possibly set a method to completed task (ie, delete a task) and showtask // otherwise take these defaults and make them methods 


#create an "add more tasks" method
#create display tasks method
#create get a task method
#create delete a task methodn--> 