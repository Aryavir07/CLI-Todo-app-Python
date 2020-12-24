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
        print(errormsg)
        return

    finalString = ''
    for x in args:
        finalString = finalString + x + ' '
    f1 = open('todo.txt', 'a')
    f1.write('%s\n'%(finalString))
    print("Added: "+ finalString)
    return
    """
    Complete assignment 
    Learn Django 
    Submit assignment 
    Read research paper 

    """

    
    
#-------------------------------------------------------

def ls(args):
    fl = open('todo.txt', 'r')
    fn = fl.read().split("\n")
    itemList = []
    for x in fn:
        itemList.insert(0,x)

    itemList = itemList[0:]
    for x in range(len(itemList)):
        if itemList[x] == '':
            continue
        else:
            print("[" + str(len(itemList)-x) +"]", end = " "),
            print(itemList[x])
    fl.close()
    return




# -----------------DELETE--------------------------

def Delete(number):
    a_file = open("todo.txt", 'r')
    lines = a_file.readlines()
    a_file.close()
    if int(len(lines)) < number or number == 0:
         print("Error: todo #"+str(number)+" does not exist. Nothing deleted." ,sep ='')
         return
    del lines[number-1]
    new_file = open("todo.txt", "w+")

    for line in lines:
        new_file.write(line)
    new_file.close()
    print("Deleted todo #"+str(number),sep ='')
    return

#---------------------------------------------------



def done(number):
    num = int(number)
    a_file = open("todo.txt", 'r')
    lines = a_file.readlines()
    if int(len(lines)) < number or number == 0:
        print("Error: todo #"+str(number)+" does not exist.",sep ='')
        return
    selection = lines[num-1]
    Delete(num)
    with open('done.txt', 'a') as f:
        f.write(selection)

    print("Marked todo #"+str(number)+" as done." ,sep ='')
    a_file.close()
    return

   


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

    v = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics \n$ exit                    # To exit from Todo.py\n"

    # sys.stdout.write(varible.encode('utf8'))
    
    print(v)
    return



   
   




#-----------------------------------------------------


def report(args):
    a_file = open("todo.txt", 'r')
    lines = a_file.readlines()
    b_file = open("done.txt", 'r')
    linesDone = b_file.readlines()
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),"[ "
    "Pending :", len(lines), "Completed :", len(linesDone),"]"
    )
    return

