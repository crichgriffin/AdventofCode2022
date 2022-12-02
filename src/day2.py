# Day 2 - Rock paper scissors
import pandas as pd

input_map=[("A", "X"), ("B", "Y"), ("C", "Z")]
init_score = [("A", 1), ("B", 2), ("C", 3)]
wins = [("A", "B"), ("B", "C"), ("C", "A")]
losses = [("A", "Z"), ("B", "X"), ("C", "Y")]

def rps_score(val1, val2):
    val2 = [x for x, y in input_map if y == val2][0]
    init_score=[y for x, y in init_score if x == val2][0]
    if val1 == val2:
        init_score += 3
    else:
        win_match = [y for x, y in wins if x==val1][0]
        if val2 == win_match:
            init_score +=6
        else:
            init_score += 0
    return init_score


def action_to_take(val1, val2):
    if val2 == "X":
        choice = [y for x, y in losses if x==val1][0]
    elif val2 == "Z":
        choice = [y for x, y in wins if x==val1][0]
    else:
        choice = [y for x, y in input_map if x==val1][0]
    return choice


def part2(val1, val2):   
    return rps_score(val1, action_to_take(val1, val2))


file1 = pd.read_csv('data/day2.txt', sep=' ', header=None)
# part 1
all_scores = file1.apply(lambda x: rps_score(*x), axis=1)
sum(all_scores)
# part 2
all_scores = file1.apply(lambda x: part2(*x), axis=1)
sum(all_scores)
