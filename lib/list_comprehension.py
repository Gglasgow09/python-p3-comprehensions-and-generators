#!/usr/bin/env python3

def return_evens(num_list):
    
    # Use a list comprehension to filter out odd elements and keep even ones.
    even_nums = [num for num in num_list if num % 2 == 0]

    return even_nums


def make_exclamation(sentence_list):
    add_exclamation = [ statement + "!" for statement in sentence_list ]

    return add_exclamation