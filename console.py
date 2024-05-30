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

    def validate_classname(self, args, check_id=False):
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

    def validate_attribute(self, args):
        """
        checks attribute
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        if len(args) > 4:
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
        args = line.split()
        if not self.validate_classname(args, check_id=True):
            return
        obj_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = obj_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
        else:
            print(req_instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = line.split()
        if not self.validate_classname(args, check_id=True):
            return
        obj_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = obj_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        del obj_instances[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()
        objs = storage.all()
        if len(args) == 0:
            print(["{}".format(str(v)) for k, v in objs.items()])
            return
        else:
            if not self.validate_classname(args):
                return
            else:
                print(["{}".format(str(v))
                  for k, v in objs.items() if type(v).__name__ == args[0]])
                return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file). 
        """
        args = line.split()
        if not self.validate_classname(args, check_id=True):
            return
        obj_instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = obj_instances.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        if not self.validate_attribute(args):
            return
        setattr(req_instance, args[2], args[3].strip('"'))
        req_instance.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
