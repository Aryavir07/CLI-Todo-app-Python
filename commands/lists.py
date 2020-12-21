"""
./todo                 # Show Usage
./todo add 'todo item" # Add a new todo
./todo ls              # Show remaining todos
./todo del NUMBER      # Delete a todo
./todo done NUMBER     # Complete a todo
./todo help            # Show Usage
./todo report          # Statistics

"""

from datetime import datetime
import sys

# sys.stdout.buffer.write(string_variable.encode('utf8'))

#-------------------------- ADD-------------------------

def add(args):
    if len(args) == 0:
        errormsg = "Error: Missing todo string. Nothing added!"
        error = sys.stdout.buffer.write(errormsg) 
        return
    final_item = ''
    for x in args:
        final_item = final_item + " " + x

    # adding to todo file
    file1 = open("todo.txt","r+")
    file1.write(final_item + '\n') 
    file1.close()
    print("Added todo:"+ final_item)

#-------------------------------------------------------

def ls(args):
    fl = open('todo.txt', 'r')
    fn = fl.read().split("\n")
    itemList = []
    for x in fn:
        itemList.insert(0,x)

    itemList = itemList[1:]
    for x in range(len(itemList)):
        print("[" + str(len(itemList)-x) +"]", end = ""),
        print(itemList[x])
    fl.close()




# -----------------DELETE--------------------------

def Delete(number):
    a_file = open("todo.txt", 'r')
    a_file.lstrip(" ")
    lines = a_file.readlines()
    a_file.close()
    if int(len(lines)) < number:
         print("Error: todo #"+str(number)+" does not exist. Nothing deleted." ,sep ='')
         return


    del lines[number]

    new_file = open("todo.txt", "w+")

    for line in lines:
        new_file.write(line)
    new_file.close()
    print("Deleted todo #"+str(number),sep ='')

#---------------------------------------------------



def done(number):
    num = int(number)
    a_file = open("todo.txt", 'r')
    lines = a_file.readlines()
    if int(len(lines)) < number:
        print("Error: todo #"+str(number)+" does not exist.",sep ='')
        return
    selection = lines[num]
    Delete(num)
    with open('done.txt', 'a') as f:
        f.write(selection)

    print("Marked todo #"+str(number)+" as done." ,sep ='')
    a_file.close()

   


# ----------------- HELP----------------------------
def help(args):
    # printList = ["Usage :-",
    # "$ ./todo add \"todo item\" # Add a new todo",
    # "$ ./todo ls               # Show remaining todos",
    # "$ ./todo del NUMBER       # Delete a todo",
    # "$ ./todo done NUMBER      # Complete a todo",
    # "$ ./todo help             # Show usage",
    # "$ ./todo report           # Statistics",
    # ]

    v = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics \n$ exit                    # To exit from Todo.py\n$ clear                   # To clear screen\n"

    # sys.stdout.write(varible.encode('utf8'))
    
    print(v)



   
   




#-----------------------------------------------------


def report(args):
    a_file = open("todo.txt", 'r')
    lines = a_file.readlines()
    b_file = open("done.txt", 'r')
    linesDone = b_file.readlines()
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),
    "Pending :", len(lines), "Completed :", len(linesDone)
    )
    return

