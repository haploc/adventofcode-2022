#!/usr/bin/env python3
"""Advent of Code - Day 03 - Rucksack Reorganization"""
# Item types list, index equals the priorities, 0 is a dummy value so index
# starts at 1
item_types = [
    "0",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]


def get_priority(item):
    """
    Returns the priority of the item type.
    Input: item - list (higher function outputs list)
    """
    try:
        return item_types.index(item[0])
    except ValueError:
        print("invalid input")


def split_compartments(rucksack):
    """Splits the content list into 2 equal compartments"""
    return [rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2:]]


def compare_compartments(compartments):
    """Return common item in 2 lists using list comprehension"""
    return [item for item in compartments[0] if item in compartments[1]]


def compare_rucksacks(sacks):
    """Return common item in 3 lists using list comprehension"""
    return [
        item for item in sacks[0]
        if item in sacks[1]
        and item in sacks[2]
    ]


def split_in_groups_of_3(sacks):
    """Split up list in groups of 3 and return list of groups"""
    return [sacks[i:i+3] for i in range(0, len(sacks), 3)]


# Some tests
# print(get_priority('a'))
# print(get_priority('Z'))
# print(split_compartments('abcdefgABCDEFG'))
# print(compare_compartments([ 'abcdefA', 'ABCDEFG']))
# print(get_priority(compare_compartments([ 'abcdefA', 'ABCDEFG'])))
# print(split_in_groups_of_3(
#   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']
# ))

# Part 1 sample
with open("sample", "r", encoding="utf-8") as file_input:
    rucksacks = file_input.readlines()
    sum_priorities = sum(
        get_priority(compare_compartments(split_compartments(sack)))
        for sack in rucksacks
    )

    print(f"Part 1 - compartments: sample - sum priorities: {sum_priorities}")

# Part 1 puzzle input
with open("input", "r", encoding="utf-8") as file_input:
    rucksacks = file_input.readlines()
    sum_priorities = sum(
        get_priority(compare_compartments(split_compartments(sack)))
        for sack in rucksacks
    )

    print(f"Part 1 - compartments: puzzle - sum priorities: {sum_priorities}")

# Part 2 sample
with open("sample", "r", encoding="utf-8") as file_input:
    rucksacks = file_input.readlines()
    groups = split_in_groups_of_3(rucksacks)
    sum_priorities = sum(get_priority(compare_rucksacks(group)) for group in groups)

    print(f"Part 2 - groups of 3: sample - sum priorities: {sum_priorities}")

# Part 2 puzzle input
with open("input", "r", encoding="utf-8") as file_input:
    rucksacks = file_input.readlines()
    groups = split_in_groups_of_3(rucksacks)
    sum_priorities = sum(get_priority(compare_rucksacks(group)) for group in groups)

    print(f"Part 2 - groups of 3: puzzle - sum priorities: {sum_priorities}")
