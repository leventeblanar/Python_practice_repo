"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Return the remaining baking time in minutes.

    Parameters:
        elapsed_bake_time: The number of minutes already spent baking.

    Returns:
        The number of minutes remaining from EXPECTED_BAKE_TIME.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Return the preparation time for the given number of layers in minutes.

    Parameters:
        number of layers: the number of lasagna layers

    Returns:
        the total preparation time in minutes
    """
    return PREPARATION_TIME * number_of_layers


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Return the total time spent preparing and baking the lasagna.

        Parameters:
            number_of_layers: The number of lasagna layers.
            elapsed_bake_time: The number of minutes already spent baking.

        Returns:
            The combined preparation and elapsed baking time in minutes.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)