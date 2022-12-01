import pandas as pd
import numpy as np

# Using readlines()
file1 = open('data/day1.txt', 'r')
lines = file1.readlines()
  
data=[]
elf_no = 0
# max_elf_no = 0
max_calories = 0
calories_list = []

for line in lines:
    if len(line.strip())==0:
        elf_no += 1
        print("new_elf found : %i" % elf_no)
        data = []
    else:
        # Strips the newline character
        data.append(int(line.strip()))
        # print(data)
        # print(sum(data))
        calories_list.append(sum(data))
        if sum(data) > max_calories:
            max_calories = sum(data)
            
            # print("new_max calories found: %i" % max_calories)
            # max_elf_no = elf_no


# get the ordered list
calories_list.sort(reverse=True)
# get top elf calories
sum(calories_list[0:1])
# get top 3 elves calories
sum(calories_list[0:3])