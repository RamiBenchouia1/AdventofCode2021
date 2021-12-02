import os
import sys

def openFile(fileToRead):
    #open/read the file and append each number to an empty list
    with open(os.path.join(sys.path[0], fileToRead),'r') as f:
        stringArr = [line.strip() for line in f.readlines()]

    numArray = [int(strng) for strng in stringArr]
    return numArray


def answer(array):
    counter = 0
    for int in range(len(array)-3):
        first = array[int]
        second = array[int+1]
        third = array[int+2]

        block1sum = first+second+third

        altfirst = array[int+1]
        altsecond = array[int+2]
        altthird = array[int+3]

        block2sum = altfirst+altsecond+altthird

        if block2sum > block1sum:
            counter+=1
    print(counter)

answer(openFile('input.txt'))