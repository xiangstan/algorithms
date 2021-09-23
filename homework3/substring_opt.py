# This program users an optimal method to find the total substring of a given string start and end of user's choice
# Example: CABAAXBYA contains 4 substrings start with a A and end with a B
# 
# Author: Xiang Shan Tan
#

import sys

if len(sys.argv) < 4 :
    print("\nUsage: python substring_opt.py [A string of Characters] [Start character] [End character]\n")
    sys.exit()

input = sys.argv

def main() :
    str = input[1].upper()
    start = input[2].upper()
    end = input[3].upper()
    count = 0
    total = 0

    for i in str :
        if i == start :
            count += 1
        if i == end :
            total += count

    #print(str, start, end)
    print(f"\nString '{str}' contains total {total} substring(s) start with a '{start}' and end with a '{end}'.\n")


if __name__ == "__main__":
    main()