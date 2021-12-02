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
    for ind in range(len(array)-1):
        if array[ind+1] > array[ind]:
            counter+=1
    print(counter)



answer(openFile('input.txt'))

