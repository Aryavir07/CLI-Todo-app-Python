import commands.lists
import commands.app


# mapping command names to dict

"""
./todo                 # Show Usage
./todo add 'todo item" # Add a new todo
./todo ls              # Show remaining todos
./todo del NUMBER      # Delete a todo
./todo done NUMBER     # Complete a todo
./todo help            # Show Usage
./todo report          # Statistics

"""

commands_dict = {
    'add': lists.add,
    'ls':lists.ls,
    'Delete': lists.Delete,
    'done':lists.done,
    'help':lists.help,
    'report':lists.report,
    './todo':lists.help

}

                        