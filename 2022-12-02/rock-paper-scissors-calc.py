#!/usr/bin/env python3

score = 0

WIN = 6
DRAW = 3
LOSS = 0
ROCK = 1
PAPER = 2
SCISSORS = 3


def rps(letter):
    """rps - rock paper scissors
    return the value of rock, paper and scissors respectively
    """
    if letter in ["A", "X"]:
        return ROCK
    if letter in ["B", "Y"]:
        return PAPER
    if letter in ["C", "Z"]:
        return SCISSORS


def wdl(letter):
    """wdl - win-draw-lose
    return values
    """
    if letter in ["X"]:
        return LOSS
    if letter in ["Y"]:
        return DRAW
    if letter in ["Z"]:
        return WIN


def analyze_play(opponent, player):
    """Analyze the game and return the score"""
    if rps(opponent) == rps(player):
        return DRAW + rps(player)
    elif rps(player) == ROCK:
        return WIN + ROCK if rps(opponent) == SCISSORS else LOSS + ROCK
    elif rps(player) == PAPER:
        return WIN + PAPER if rps(opponent) == ROCK else LOSS + PAPER
    elif rps(player) == SCISSORS:
        return WIN + SCISSORS if rps(opponent) == PAPER else LOSS + SCISSORS


def win_draw_lose(opponent, player):
    """Analyze the game and return the score"""
    if wdl(player) == DRAW:
        return DRAW + rps(opponent)
    elif wdl(player) == WIN:
        if rps(opponent) == ROCK:
            return WIN + PAPER
        elif rps(opponent) == PAPER:
            return WIN + SCISSORS
        else:
            return WIN + ROCK
    elif wdl(player) == LOSS:
        if rps(opponent) == ROCK:
            return LOSS + SCISSORS
        elif rps(opponent) == PAPER:
            return LOSS + ROCK
        else:
            return LOSS + PAPER


with open("input", "r") as input:
    pt1_total_score = 0
    pt2_total_score = 0
    plays = input.readlines()
    for play in plays:
        opp, player = play.split()
        pt1_total_score += analyze_play(opp, player)
        pt2_total_score += win_draw_lose(opp, player)

    print(f"Part 1 - total score: {pt1_total_score}")
    print(f"Part 2 - total score: {pt2_total_score}")
