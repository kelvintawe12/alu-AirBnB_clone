#!/usr/bin/python3
"""
Console Module
This module contains the entry point of the command interpreter.
"""
import cmd


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

    def help_quit(self):
        """Provide help information for the quit command."""
        print("Quit command to exit the program.\n")

    def help_EOF(self):
        """Provide help information for the EOF command."""
        print("Exit the program using EOF (Ctrl+D).\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
