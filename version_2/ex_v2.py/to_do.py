
#Why am I getting an empty list when I add to the class variable? Tried making and attribute to hold the list, but it doesn't save the input
#Should make ask_for_task a class method?
#Not clearn what I should put as attributes

class ToDo(object):
    tasks = []

    def __init__(self):
        self.counter = 1

    def ask_for_task(self):
        while True:
            todo_list = input("Enter a task. Or hit return if finished: ")
            if todo_list == "":
                break
            else:
                self.__class__.tasks.append(todo_list)
                
        print(f"here's the todo list {self.__class__.tasks}")


todo = ToDo()
print(todo.ask_for_task())
print(todo.__class__.tasks)





#ORiginal
#  def ask_for_task(self):

#         while True:
#             self.task = input("Enter a task. Or hit return if finished: ")
#             if self.task == '':
#                 break
#             else:
#                 self.to_do_list.append(self.task)
         
#         print(f"here's the todo list {self.to_do_list}")

