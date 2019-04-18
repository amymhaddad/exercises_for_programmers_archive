

#I don't want to use a class variable b/c 
#the class will create nay number of to do lists 
#the instance deals with one indiviudal to do list

#ask for input outside of the class and feed input into class
#What are the nouns in the prob statement? Those should be attributes


def get_tasks():
    task_list = []
    while True:
        user_task = input("Enter a task. Or hit return if finished: ")
        if user_task == '':
            break
        else:
            task_list.append(user_task)
            
    return task_list

copy = get_tasks()

to_dos = 'tasks.py'
with open(to_dos, 'w') as f_object:
    for task in copy:
        f_object.write(task)
        f_object.write('\n')


class ToDoList(object):
    
    def __init__(self, file, new_task = ''):
        self.file = file
        self.new_task = new_task 
        
    def add_new_task(self):
        with open(self.file, 'w') as f_object:
            f_object.write(self.new_task)
    
    def show_tasks(self):
        with open(self.file) as f_object:
            tasks = f_object.readlines()
        print(tasks)

t1 = ToDoList(to_dos, 'sleep')
print(t1.show_tasks())


#Find a way to perm store tasks so I don't have to go through the input prompt
#Create method to delete a task
