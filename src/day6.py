

test="mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def get_starting_packet(test, nn=4):
    uniq_letters = []
    for idx, x in enumerate(test):
        if len(uniq_letters) < nn:
            uniq_letters.append(x)
        else:
            if len(test[idx-nn:idx]) == len(set(test[idx-nn:idx])):
                return idx 


# tests
get_starting_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") #5
get_starting_packet("nppdvjthqldpwncqszvftbrmjlhg") #6
get_starting_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") #10
get_starting_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") # 11
get_starting_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", nn=14)

# load data
file1 = open('data/day6.txt', 'r')
line = file1.readlines()[0]
# part1
get_starting_packet(line, nn=4)

get_starting_packet(line, nn=14)
