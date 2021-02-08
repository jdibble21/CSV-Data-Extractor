# Read dataset from a csv, for each attribute, calculate min, max, mean, median, standard deviation
import csv
import statistics

class Extractor:
    def __init__(self,csvfilename):
        self.csvFilename = csvfilename
        self.csvData = ""
        self.turnList = []
        self.whiteRatingList = []
        self.blackRatingList = []
        self.openingPlayList = []
        self.ratedList = []

    def readFileToData(self):
        with open(self.csvFilename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.turnList.append(int(row['turns']))
                self.whiteRatingList.append(int(row['white_rating']))
                self.blackRatingList.append(int(row['black_rating']))
                self.ratedList.append(str(row['rated']))
    
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
        

extractor = Extractor('cs455_homework1_dibble.csv')
extractor.readFileToData()
print(extractor.calculateBooleanFrequency(extractor.ratedList))


        
    

