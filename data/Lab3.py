"""
 Name: Angelo Ramos, Seth Verenski
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: 10-11-23
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: n/a

 Creativity: anything extra that you added to the lab

 Instructions: navigate to dir that file is in. example run: python lab3.py --mode R --input input_file.txt --output output_train.txt output_test.txt

"""
import random
import sys
import argparse
import math

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """

    split_index = int(len(data)*ratio)

    trainData.extend(data[:split_index])
    testData.extend(data[split_index:])

def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    
    random.shuffle(data)

    split_index = int(len(data)*ratio)

    trainData.extend(data[:split_index])
    testData.extend(data[split_index:])

def readFile(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file.readlines()]
    return data

def writeFile(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """

    if mode == 'R':
        inputFile = options.input
        data = readFile(inputFile)
        [trainOutFile, testOutFile] = options.output
        ratio = .7
        trainData, testData = splitDataRandom(data, ratio)
        writeFile(trainOutFile, testOutFile, trainData, testData)
    if mode == 'N':
        inputFile = options.input
        data = readFile(inputFile)
        [trainOutFile, testOutFile] = options.output
        ratio = .7
        trainData, testData = splitData(data, ratio)
        writeFile(trainOutFile, testOutFile, trainData, testData)

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("Please provide input argument. Here are examples:")
    print("python " + sys.argv[0] + " --mode N --input DATA/epidemiology.csv --output TrainingData.txt TestData.txt")
    print("python " + sys.argv[0] + " --mode R --input DATA/epidemiology.csv --output TrainingDataRandom.txt TestDataRandom.txt") 
    sys.exit(0)

if __name__ == "main":
        #------------------------arguments------------------------------#
        #Shows help to the users                                        #
        #---------------------------------------------------------------#
        parser = argparse.ArgumentParser()
        parser._optionals.title = "Arguments"
        parser.add_argument('--mode', dest='mode',
                                default='',  # default empty!
                                help='Mode: R for random splitting, and N for normal splitting')
        parser.add_argument('--input', dest='input',
                                default='',  # default empty! 
                                )
        parser.add_argument('--output', nargs=2, dest='output',
                                default='',  # default empty!
                                )
        parser.add_argument('--modelPath', dest='modelPath',
                                default='',  # default empty!
                                help='The path of the machine learning model ')
        parser.add_argument('--trueLabel', dest='trueLabel',
                                default='',  # default empty!
                                help='The path of the correct label ')
        options = parser.parse_args()
        if not options.mode or not options.input or not options.output:
                showHelper()
        main()