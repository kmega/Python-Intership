class Actions:
    def create_new_task(self):
        return Task(str(input("Provide name for the task: ")), str(input("Provide date time for the task: ")), str(input("Provide description for the task: ")))

    def get_data(self):
        with open("database.txt", "r") as f:
            database = f.readlines()

        return database

    def write_data(self, database):
        with open("database.txt", "w") as f:
            for data in database:
                f.write(data)

class Task:
    def __init__(self, name, date_time, description):
        self.name = name
        self.date_time = date_time
        self.description = description

class Interface:
    def __init__(self):
        print("Task listing app. Available commands: -add, -edit, -remove, -list, -exit.")

    def add(self):
        action = Actions()
        new_task = action.create_new_task()

        task = new_task.name + " " + new_task.date_time + " " + new_task.description

        with open("database.txt", "a") as f:
            f.write(task + " " + str(hash(task)) + "\n")

    def edit(self):
        action = Actions()
        new_task = action.create_new_task()
        
        task = new_task.name + " " + new_task.date_time + " " + new_task.description
        hash_tag = int(input("Provide task hash number: "))

        database = action.get_data();

        for i in range(0, len(database)):
            if str(hash_tag) in database[i]: 
                database[i] = task + " " + str(hash(task)) + "\n"
                action.write_data(database)

    def remove(self):
        hash_tag = int(input("Provide task hash number: "))

        action = Actions()
        database = action.get_data();
        
        for i in range(0, len(database)):
            try:
                if str(hash_tag) in database[i]:
                    del database[i]
                    action.write_data(database)
            except:
                continue

    def list(self):
        action = Actions()
        database = action.get_data();

        for data in database:
            print(data)

user_interface = Interface()
user_input = "";

while user_input != "-exit":
    user_input = str(input(""))

    if user_input == "-add":
        print("\n")
        user_interface.add()
    elif user_input == "-edit":
        print("\n")
        user_interface.edit()
    elif user_input == "-remove":
        print("\n")
        user_interface.remove()
    elif user_input == "-list":
        print("\n")
        user_interface.list()
    else:
        print("\n")
        print("Wrong command.")