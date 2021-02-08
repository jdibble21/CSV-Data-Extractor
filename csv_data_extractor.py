# Read dataset from a csv, for each attribute, calculate min, max, mean, median, standard deviation
import csv

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
                self.whiteRatingList.append(row['white_rating'])
                self.blackRatingList.append(row['black_rating'])

extractor = Extractor('cs455_homework1_dibble.csv')
extractor.readFileToData()
        
    

