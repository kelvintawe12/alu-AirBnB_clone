#!/usr/bin/python3
"""
Console Module
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model2 import BaseModel
from models import storage  # This assumes a storage system managing all objects


# Dictionary of valid classes
CLASSES = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB clone project."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)."""
        print()  # To ensure a new line after EOF is entered
        return True

    def emptyline(self):
        """Override default behavior for empty input lines."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = CLASSES[arg]()  # Create a new instance
        new_instance.save()  # Save to the storage system
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            # Print all instances
            print([str(obj) for obj in instances.values()])
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            # Filter by class name
            print([str(obj) for key, obj in instances.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        # Cast to the appropriate type if possible
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
