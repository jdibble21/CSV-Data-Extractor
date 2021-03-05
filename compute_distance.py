# Choose 4 attributes from 100 rows, normalize numeric vals and compute distance between row values
from colorama import Fore, Style
import pandas as pd
import math

def normalizeDataframe(dataframe):
    MAX = dataframe.max()
    MIN = dataframe.min()
    dataframe = dataframe.astype(float)
    for i in range(0,len(dataframe)):
        value = float(dataframe[i])
        normValue = float((value - MIN)/(MAX-MIN))
        dataframe[i] = math.fabs(normValue)
    return dataframe

def calculateTwoRecordDistance(num1rec1,num1rec2,num2rec1,num2rec2,ordDistance,catDistance):
    #example: index = 8,29 need num1[8] - num1[29] + num2[8] - num2[29] + ordDistance + catDistance
    distance = math.fabs(num1rec1 - num1rec2) + math.fabs(num2rec1 - num2rec2) + ordDistance + catDistance
    return distance * 0.25

def calculateOrdinalDistance(ordDataframe,d1,d2):
    valDict = {
        "A": 0.25,
        "B":0.50,
        "C":0.75,
        "D":1
    }
    #First record data
    record1 = ordDataframe[d1]
    record1Letter = record1[0]
    record1NumVal = float(record1[1:3])
    record1Distance = valDict[record1Letter] + (record1NumVal*0.001)

    #Second record data
    record2 = ordDataframe[d2]
    record1Letter = record2[0]
    record1NumVal = float(record2[1:3])
    record2Distance = valDict[record1Letter] + (record1NumVal*0.001)
    return math.fabs(record1Distance - record2Distance)
        
def calculateCategoricalDistance(catDataframe,d1,d2):
    valDict = {
        "outoftime": 0.25,
        "resign":0.50,
        "mate":0.75,
        "draw":1
    }
    #First record data
    record1 = valDict[catDataframe[d1]]

    #Second record data
    record2 = valDict[catDataframe[d2]]
    return math.fabs(record1 - record2)



R8 = 8
R29 = 29
R73 = 73

pd.set_option('display.max_rows', None)
data = pd.read_csv("cs455_homework3_dataset_dibble.csv")

numericData1 = data['white_rating']
numericData2 = data['black_rating']
categoricalData = data['victory_status']
numericData1 = normalizeDataframe(numericData1)
numericData2 = normalizeDataframe(numericData2)
ordinalData = data['opening_eco']

# FIRST COMPUTATION
# Calculate Distance between record 8 and 29
ordDistance = calculateOrdinalDistance(ordinalData,R8,R29)
categoricalDistance = calculateCategoricalDistance(categoricalData,R8,R29)
print("\n== FIRST COMPUTATION ==")
print("Records 8 and 29\n")
print("Normalized Record 8 Numeric Attribute 1 Value: ",numericData1[R8])
print("Normalized Record 29 Numeric Attribute 1 Value: ",numericData1[R29])
print("Normalized Record 8 Numeric Attribute 2 Value: ",numericData2[R8])
print("Normalized Record 29 Numeric Attribute 2 Value: ",numericData2[R29])
print("Ordinal Records Distance: ", ordDistance)
print("Categorical Records Distance: ",categoricalDistance)
print(Fore.YELLOW,"Final Distance: ",calculateTwoRecordDistance(numericData1[R8],numericData1[R29],numericData2[R8],numericData2[R29],ordDistance,categoricalDistance),"\n")
print(Style.RESET_ALL)

# SECOND COMPUTATION
# Calculate Distance between record 29 and 73
ordDistance = calculateOrdinalDistance(ordinalData,R29,R73)
categoricalDistance = calculateCategoricalDistance(categoricalData,R29,R73)
print("== SECOND COMPUTATION ==")
print("Records 29 and 73\n")
print("Normalized Record 29 Numeric Attribute 1 Value: ",numericData1[R29])
print("Normalized Record 73 Numeric Attribute 1 Value: ",numericData1[R73])
print("Normalized Record 29 Numeric Attribute 2 Value: ",numericData2[R29])
print("Normalized Record 73 Numeric Attribute 2 Value: ",numericData2[R73])
print("Ordinal Records Distance: ", ordDistance)
print("Categorical Records Distance: ",categoricalDistance)
print(Fore.YELLOW,"Final Distance: ",calculateTwoRecordDistance(numericData1[R29],numericData1[R73],numericData2[R29],numericData2[R73],ordDistance,categoricalDistance),"\n")
print(Style.RESET_ALL)

# THIRD COMPUTATION
# Calculate Distance between record 8 and 73
ordDistance = calculateOrdinalDistance(ordinalData,R8,R73)
categoricalDistance = calculateCategoricalDistance(categoricalData,R8,R73)
print("== THIRD COMPUTATION ==")
print("Records 8 and 73\n")
print("Normalized Record 8 Numeric Attribute 1 Value: ",numericData1[R8])
print("Normalized Record 73 Numeric Attribute 1 Value: ",numericData1[R73])
print("Normalized Record 8 Numeric Attribute 2 Value: ",numericData2[R8])
print("Normalized Record 73 Numeric Attribute 2 Value: ",numericData2[R73])
print("Ordinal Records Distance: ", ordDistance)
print("Categorical Records Distance: ",categoricalDistance)
print(Fore.YELLOW,"Final Distance: ",calculateTwoRecordDistance(numericData1[R8],numericData1[R73],numericData2[R8],numericData2[R73],ordDistance,categoricalDistance),"\n")
print(Style.RESET_ALL)


