# Choose 4 attributes from 100 rows, compute distance and normalize between values
import csv

class DistanceCalculator:
    def __init__(self, csvfilename):
        self.csvFilename = csvfilename
        self.csvData = ""
        self.categoricalColumn = []
        self.numericalOneColumn = []
        self.numericalTwoColumn = []
        self.ordinalColumn = []

    def getData(self):
         with open(self.csvFilename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:

    
