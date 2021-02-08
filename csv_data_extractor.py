# Read dataset from a csv, for each attribute, calculate min, max, mean, median, standard deviation
import csv
import statistics
from collections import Counter

class Extractor:
    def __init__(self,csvfilename):
        self.csvFilename = csvfilename
        self.turnList = []
        self.whiteIDList = []
        self.blackIDList = []
        self.whiteRatingList = []
        self.blackRatingList = []
        self.openingPlayList = []
        self.ratedList = []
        self.createdAtList = []
        self.lastMoveAtList = []
        self.openingEcoList = []
        self.openingMoveNameList = []

    def readFileToData(self):
        with open(self.csvFilename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.whiteIDList.append(row['white_id'])
                self.blackIDList.append(row['black_id'])
                self.turnList.append(int(row['turns']))
                self.createdAtList.append(row['created_at'])
                self.lastMoveAtList.append(row['last_move_at'])
                self.whiteRatingList.append(int(row['white_rating']))
                self.blackRatingList.append(int(row['black_rating']))
                self.openingEcoList.append(row['opening_eco'])
                self.openingMoveNameList.append(row['opening_name'])
                self.openingPlayList.append(int(row['opening_ply']))
                self.ratedList.append(str(row['rated']))
    
    def printDatasetValues(self):
        print("\n=== Dataset Stats and Distinct Values ===")
        print("\n- NUMERICAL ATTRIBUTES -\n")
        print("turns:")
        print("Min: ", self.getMin(self.turnList))
        print("Max: ", self.getMax(self.turnList))
        print("Mean: ", self.getMean(self.turnList))
        print("Median: ",self.getMedian(self.turnList))
        print("Standard Deviation: ", self.calculateStandardDev(self.turnList))

        print("\nwhite_rating:")
        print("Min: ", self.getMin(self.whiteRatingList))
        print("Max: ", self.getMax(self.whiteRatingList))
        print("Mean: ", self.getMean(self.whiteRatingList))
        print("Median: ",self.getMedian(self.whiteRatingList))
        print("Standard Deviation: ", self.calculateStandardDev(self.whiteRatingList))

        print("\nblack_rating:")
        print("Min: ", self.getMin(self.blackRatingList))
        print("Max: ", self.getMax(self.blackRatingList))
        print("Mean: ", self.getMean(self.blackRatingList))
        print("Median: ",self.getMedian(self.blackRatingList))
        print("Standard Deviation: ", self.calculateStandardDev(self.blackRatingList))

        print("\nopening_ply:")
        print("Min: ", self.getMin(self.openingPlayList))
        print("Max: ", self.getMax(self.openingPlayList))
        print("Mean: ", self.getMean(self.openingPlayList))
        print("Median: ",self.getMedian(self.openingPlayList))
        print("Standard Deviation: ", self.calculateStandardDev(self.openingPlayList))

        print("\n- OTHER ATTRIBUTES -\n")

        booleanArray = self.calculateBooleanFrequency(self.ratedList)
        print("rated boolean count: TRUE:", booleanArray[0], " FALSE: ", booleanArray[1])
        whiteIdArray = self.getUniqueMaxValue(self.whiteIDList)
        print("\nwhite_id distinct VALUE: ", whiteIdArray[0], " COUNT: ", whiteIdArray[1])
        blackIdArray = self.getUniqueMaxValue(self.blackIDList)
        print("\nblack_id distinct VALUE: ", blackIdArray[0], " COUNT: ",blackIdArray[1])
        openingEcoArray = self.getUniqueMaxValue(self.openingEcoList)
        print("\nopening_eco distinct VALUE: ", openingEcoArray[0], " COUNT: ", openingEcoArray[1])
        openingNameArray = self.getUniqueMaxValue(self.openingMoveNameList)
        print("\nopening_name distinct VALUE: ", openingNameArray[0], " COUNT: ", openingNameArray[1])

    def getMin(self,list):
        return min(list)

    def getMax(self,list):
        return max(list)

    def getMean(self,list):
        return statistics.mean(list)

    def getMedian(self,list):
        return statistics.median(list)

    def calculateStandardDev(self,list):
        return statistics.stdev(list)

    def calculateBooleanFrequency(self,list):
        trueNum = 0
        falseNum = 0
        for value in list:
            if value == "TRUE":
                trueNum += 1
            if value == "FALSE":
                falseNum += 1
        return [trueNum,falseNum]
        
    def getUniqueMaxValue(self,list):
        valueDict = dict(Counter(list).items())
        maxValue = max(valueDict, key=valueDict.get)
        return [maxValue,valueDict[maxValue]]

extractor = Extractor('cs455_homework1_dibble.csv')
extractor.readFileToData()
extractor.printDatasetValues()



        
    

