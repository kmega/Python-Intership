class Task:
    def __init__(self, name, date_time, description):
        self.name = name
        self.date_time = date_time
        self.description = description

class Interface:
    def __init__(self):
        print("Task listing app. Available commands: -add, -edit, -remove, -list, -exit.")

    def add(self):
        task = Task(str(input("Provide name for the task.")), str(input("Provide date time for the task.")), str(input("Provide description for the task.")))
        f = open("database.txt", "w")
        f.write(task.name + " " + task.date_time + " " + task.description)
        f.close()

    def edit(self):
        print("")
        
    def remove(self):
        print("")

    def list(self):
        print("")

user_interface = Interface()
user_input = "";

while user_input != "-exit":
    user_input = str(input(""))

    if user_input == "-add":
        user_interface.add()
    elif user_input == "-edit":
        user_interface.edit()
    elif user_interface == "-remove":
        user_interface.remove()
    elif user_interface.list == "-list":
        user_interface.list()