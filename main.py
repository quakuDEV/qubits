"""
textbook:

qubits are represented by alpha and beta, which are complex coefficients 
these are calculated by square rooting the normal probabilities

alpha is for 0
beta is for 1

method:

define qubits: qubits_array
qubits_array = [p(00), p(01), p(10), p(11)..]
adds the probibilities as complex coefficients

get qubits
returns the complex coefficients

read qubits
1) convert qubits array to normal probabilities
2) randomise 0, 1, 2, 3, 4... with each probability
3) make the 0, 1, 2, 3, 4... into binary
"""

import math
from math import *
import random
from random import *

import random

def pick_index(probabilities):
    """
    Selects an index based on the provided array of probabilities.

    :param probabilities: List of probabilities (must sum to 1)
    :return: Selected index
    """
    if not 0.999 < sum(probabilities) < 1.001:
        raise ValueError("Probabilities must sum to 1.")

    # Generate a cumulative distribution
    cumulative = []
    current = 0
    for p in probabilities:
        current += p
        cumulative.append(current)

    # Generate a random number and find the corresponding index
    r = random.random()
    for i, threshold in enumerate(cumulative):
        if r < threshold:
            return i

def number_to_binary(number):
    """
    Converts a given number to its binary representation.

    :param number: An integer to convert to binary.
    :return: A string representing the binary form of the number.
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return bin(number)[2:]


class qubits:
    def __init__(self):
        self.complex_coefficients = []
    def define(self, qubits_array):
        for _ in qubits_array:
            coef = math.sqrt(_)
            self.complex_coefficients.append(coef)
    def get(self):
        return(self.complex_coefficients)
    def read(self):
        probabilities = []
        for _ in self.complex_coefficients:
            probabilities.append(math.pow(_, 2))
        result = pick_index(probabilities)
        bin = number_to_binary(result)
        return bin

test = qubits()
test.define([0.25, 0.25, 0.25, 0.25])
print(test.get())
for i in range(12):
    print(test.read())