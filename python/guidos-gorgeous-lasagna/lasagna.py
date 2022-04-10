EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.
    .:param elapsed_bake_time: int baking time already elapsed.
    .:return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time per layer.
    .:param number_of_layers: int number of layers.
    .:return: int time in minutes derived from 'PREPARATION_TIME'.

    Function that takes the actual number of layer of the lasagna and
    return how much time does it take to make them
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return PREPARATION_TIME * number_of_layers + elapsed_bake_time
