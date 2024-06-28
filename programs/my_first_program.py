from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))

    # Calculate the average of the three input integers
    sum_ints = my_int1 + my_int2 + my_int3
    average = sum_ints / 3

    # Square the average
    squared_average = average * average

    # Compute the difference between the square of average and each original integer squared
    diff1 = squared_average - (my_int1 * my_int1)
    diff2 = squared_average - (my_int2 * my_int2)
    diff3 = squared_average - (my_int3 * my_int3)

    # Outputs
    return [
        Output(squared_average, "squared_average_output", party1),
        Output(diff1, "diff1_output", party1),
        Output(diff2, "diff2_output", party1),
        Output(diff3, "diff3_output", party1)
    ]
