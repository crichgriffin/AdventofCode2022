import pandas as pd

all_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

file1 = open('data/day3.txt', 'r')
lines = file1.readlines()
rucksacks = [l.strip() for l in lines]



rucksack="jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"

def get_gift_score(rucksack):
    max_size = len(rucksack)
    comp1 = rucksack[0:int(max_size/2)]
    comp2 = rucksack[int(max_size/2): max_size]
    match_item = list(set(comp1).intersection(comp2))[0]
    score = all_letters.index(match_item) +1 
    return score

sum([get_gift_score(x) for x in rucksacks])

# part 2
def get_priority(rucksacks):
    test_sets = [set(x) for x in rucksacks]
    u = list(set.intersection(*test_sets))[0]
    score = all_letters.index(u) + 1
    return score

rucksacks

start_idx = list(range(0,300, 3))
sum([get_priority(rucksacks[idx:idx+3]) for idx in start_idx])