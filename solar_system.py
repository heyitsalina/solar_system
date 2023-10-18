"""This is a toy repository intended for git + GitHub introductory sessions.
Good thing in those courses is, most people know one thing or two about our solar system.
"""
import random
from planets import mars


# Global constants
SPARKLING_CHARS = "*+.°^><o°~\'" + 100 * " "  # more spaces means more cosmic emptyness


def sparkle(width: int = 60, num_sparkle_lines: int = 2):
    """
    Prints random sparkling characters for a cosmic ascii view.

    Parameters
    ----------
    width (int): 
        The number of characters in each line of sparkle. Default is 60.
    num_sparkle_lines (int): 
        The number of lines of sparkle to be printed. Default is 2.
    """
    for _ in range(num_sparkle_lines):
        line = "".join(random.choice(SPARKLING_CHARS) for _ in range(width))
        print(line)


if __name__ == "__main__":
    sparkle(num_sparkle_lines=3)
    print(f"{8 * '<>'} Welcome to our solar system {8 * '<>'}")
    sparkle(num_sparkle_lines=3)
    print(f"{mars.NAME.upper()}:")
    print(mars.DESCRIPTION)
    sparkle()
