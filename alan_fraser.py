tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# MVP
# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks

def uncompleted_tasks(list, Boolean):
    for task in tasks:
        if task["completed"] == Boolean:
            print(task.values())

finished_uncompleted_tasks = uncompleted_tasks(tasks, False)
print(finished_uncompleted_tasks)

# # Print a list of completed tasks

def completed_tasks(list, Boolean):
    for task in tasks:
        if task["completed"] == Boolean:
            print(task.values())

finished_completed_tasks = completed_tasks(tasks, True)
print(finished_completed_tasks)

# Print a list of all task descriptions

def all_tasks_descriptions(list):
    for task in tasks:
            print(task["description"])

finished_tasks = all_tasks_descriptions(tasks)
print(finished_tasks)

# Print a list of tasks where time_taken is at least a given time

def given_time(list):
    for time in tasks:
        if time["time_taken"] > 10:
            print(time)

finished_time = given_time(tasks)
print(finished_time)

# Print any task with a given description

def given_description(lists, description_name):
    for activity in tasks:
        if activity["description"] == description_name:
            print(activity)

finished_given_description = given_description(tasks, "Clean Windows")
print(finished_given_description)