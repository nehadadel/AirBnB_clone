#!/usr/bin/python3

"""
class HBNBCommand
"""

import sys
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class"""
    prompt = "(hbnb) "
    classes = {'BaseModel' : BaseModel}
   
    def do_EOF(self, line):
        """EOF exit the program"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line shouldn’t execute anything"""
        return

    def validate_classname(args, check_id=False):
        """
        Runs checks on args to validate classname entry.
        """
        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = line.split()
        if not self.validate_classname(args):
            return

        new_obj = self.classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not self.validate_classname(args, check_id=True):
            return
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
