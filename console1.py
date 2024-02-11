#!/usr/bin/python3

"""
class HBNBCommand
"""

import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class"""
    prompt = "(hbnb) "

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

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            new_object = globals()[class_name]()
            new_object.save()
            print(new_object.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        key_id = class_name + "." + id
        if key_id not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key_id])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        key_id = class_name + "." + id
        if key_id not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key_id]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        instances = storage.all()
        filtered_inst = [str(instance) for key, instance in instances.items()]
        if not args:
            if filtered_inst:
                print(filtered_inst)
            else:
                print("[]")
            return

        if len(args) == 1:
            class_name = args[0]
            if class_name in globals():
                filtered_inst = [str(instance) for key,
                                 instance in instances.items()
                                 if key.split('.')[0] == class_name]
                if filtered_inst:
                    print(filtered_inst)
                else:
                    print("[]")
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        key_id = class_name + "." + id
        if key_id not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]

        # Retrieve the instance from storage
        instance = storage.all()[key_id]
        # Check if the attribute is valid and can be updated
        if attribute not in ["id", "created_at", "updated_at"]:
            try:
                # Get the attribute type
                attr_type = type(getattr(instance, attribute))
            except AttributeError:
                print("** attribute doesn't exist **")
                return
            # Cast the value to the attribute type
            casted_value = attr_type(value)
            # Update the attribute
            setattr(instance, attribute, casted_value)
            # Save the changes
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
