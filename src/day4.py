import pandas as pd


def part1(start1, stop1, start2, stop2):
    score=False
    range1=set(range(start1, stop1 +1))
    range2=set(range(start2, stop2 +1))
    i_len = len(range1.intersection(range2))
    if i_len == len(range1) or i_len == len(range2):
        score=True 
    return score


def part2(start1, stop1, start2, stop2):
    score=False
    range1=set(range(start1, stop1 +1))
    range2=set(range(start2, stop2 +1))
    if len(range1.intersection(range2)) > 0:
        score=True
    return score



df = pd.read_csv("data/day4.txt", sep=",", header=None)
df[['e1_start', 'e1_stop']] = df[0].str.split("-", expand=True)
df[['e2_start', 'e2_stop']] = df[1].str.split("-", expand=True)
df = df.drop(columns=[0,1])
df = df.astype(int)

# part 1
df['contain2'] = df[['e1_start', 'e1_stop', 'e2_start', 'e2_stop']].apply(lambda x: part1(*x), axis=1)
df['contain2'].sum()
# part 2
df['overlap2'] = df[['e1_start', 'e1_stop', 'e2_start', 'e2_stop']].apply(lambda x: part2(*x), axis=1)
df['overlap2'].sum()