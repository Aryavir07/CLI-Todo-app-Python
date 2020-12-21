from commands import commands_dict # imports from __init__ file
from os import system, name 
import os
from time import sleep 
def CLEAR():
    os.system('cls' if os.name=='nt' else 'clear')


def parse(cmd):

    if cmd != '' :
        cmd_list = cmd.split()
        cmd_type = cmd_list[0]

        if cmd_type == './todo' and len(cmd_list[1:]) != 0:
            cmd_name = cmd_list[1]
            if (cmd_name in ['add', 'del', 'done']):
                return cmd_name, cmd_list[2:]
            elif (cmd_name in ['ls', 'help', 'report']):
                return cmd_name, []
            elif (cmd_name not in ['add', 'del', 'done','ls', 'help', 'report']):
                print("Please enter valid input!")
                return main()
        elif  cmd_type == './todo' and len(cmd_list[1:]) ==0:
            return './todo', [] 
    else:
        return './todo', []

       
def main():
    try:
        command = input('$ ')
        cmndList = command.split(" ")
        if cmndList[0] == 'clear':
            sleep(1)
            return CLEAR(),main()
        if cmndList[0]!='./todo' and cmndList[0]!='' and cmndList[0] != 'exit':
            print("Invalid input!")
            return main()
        

        if command == 'exit':
            return
        else:

            command_name, command_args = parse(command)
            
            if command_name == 'del':
                commands_dict['Delete'](int(command_args[0]))
                return main()
            elif command_name == 'done':
                commands_dict['done'](int(command_args[0]))
            else:
                commands_dict[command_name](command_args)
            return main()

    except EOFError as e:
        print(end = "")
if __name__ == "__main__":
    main()