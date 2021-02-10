"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730386298"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortunecookie())
    print("Now, go spread positive vibes!")


# TODO 1: Defdine your fortune_cookie function here.
def fortunecookie():
    fortune: int = randint(1, 4)

    if fortune == 1:
        return "good things are coming your way"
    else:
        if fortune == 2:
            return "yummy food is in your future"
        else:
            if fortune == 3:
                return "good news is close by"
            else:
                return "look forward to tomorrow"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
