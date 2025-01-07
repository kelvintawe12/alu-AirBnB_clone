import cmd
# !/usr/bin/python3
"""
Console Module
This module contains the entry point of the command interpreter.
"""

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB clone project."""
    prompt = "(hbnb) "

    def do_quit(self, _):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, _):
        """Exit the program using EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()