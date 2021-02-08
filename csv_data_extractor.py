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

    def readFileToData(self):
        with open(self.csvFilename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.turnList.append(row['turns'])
                self.whiteRatingList.append(int(row['white_rating']))
                self.blackRatingList.append(int(row['black_rating']))
    
    def getMin(self,list):
        return min(list)

    def getMax(self,list):
        return max(list)

    def getMean(self,list):
        pass
    def getMedian(list):
        pass
    def calculateStandardDev(list):
        return statistics.stdev(list)
        
        

extractor = Extractor('cs455_homework1_dibble.csv')
extractor.readFileToData()

print(extractor.getMin(extractor.whiteRatingList))
        
    

