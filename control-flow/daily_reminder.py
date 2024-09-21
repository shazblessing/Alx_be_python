from asyncio import Task
from queue import PriorityQueue


def main():
    #Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()


#Process the Task Based on Priority and Time Sensitivity
if PriorityQueue == "high" :

 reminder = f"'{task}' is a high priority task" # type: ignore

if time_bound == "yes": 

            reminder += " that requires immediate attention today!"

else: 
            reminder += ". Consider completing it soon."
           
elif PriorityQueue == "medium":

        reminder = f"'{task}' is a medium priority task" # type: ignore

        if time_bound == "yes": # type: ignore

            reminder += "that should be addressed soon."

        else:
            reminder += ". You can handle it later."

elif PriorityQueue == "low":
        reminder = f"'{task}' is a low priority task" # type: ignore

        if time_bound == "yes": # type: ignore

            reminder += "but should be addressed at your convinience."

        else:

            reminder += ". Consider completing it when you have free time."
else:

reminder = "Invalid priority level. Please enter high, medium, or low."

#Provide a customized reminder
print("/nReminder:", reminder)

if __name__ == "__main__":
    main()
