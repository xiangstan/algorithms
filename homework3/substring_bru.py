# This program users a brute force method to find the total substring of a given string start and end of user's choice
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
    total = 0
    length = len(str)

    for i in range(length) :
        for j in range(i+1, length) :
            if (str[i] == start) and (str[j] == end) :
                total += 1

    #print(str, start, end)
    print(f"\nString '{str}' contains total {total} substring(s) start with a '{start}' and end with a '{end}'.\n")


if __name__ == "__main__":
    main()