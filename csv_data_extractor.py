# Read dataset from a csv, for each attribute, calculate min, max, mean, median, standard deviation
import csv

class Extractor:
    def __init__(self,csvfilename):
        self.csvFilename = csvfilename
        self.csvData = ""

    def readFileToData(self):
        with open(self.csvFilename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                print(row[0] + "  " + row[1])

extractor = Extractor('cs455_homework1_dibble.csv')
extractor.readFileToData()
        
    

