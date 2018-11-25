from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import matplotlib
import matplotlib.pyplot as plt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def Q6PenData():
	
	for i in xrange(0, 45, 5):
		penresult = []
		penMax = 0.0
		templist = [i]

		for x in range (0,5):
			nnet, accuracy = testPenData(templist)
			penresult.append(accuracy)
			if(accuracy> penMax):
				penMax = accuracy

		penAvg = average(penresult)
		penStd = stDeviation(penresult)

		print('Number of Hidden Layers', i)
		print('Pen max :', penMax)
		print('Pen average :', penAvg)
		print('Pen std: ', penStd)

	print('End of Q6 Pen Data')

def Q6CarData():
	
	for i in xrange(0, 45, 5):
		penresult = []
		penMax = 0.0
		templist = [i]

		for x in range (0,5):
			nnet, accuracy = testCarData(templist)
			penresult.append(accuracy)
			if(accuracy> penMax):
				penMax = accuracy

		penAvg = average(penresult)
		penStd = stDeviation(penresult)

		print('Number of Hidden Layers', i)
		print('Car max :', penMax)
		print('Car average :', penAvg)
		print('Car std: ', penStd)

	print('End of Q6 Car Data')


def Q5PenData():
	penresult = []
	penMax = 0.0
	for x in range (0,5):
		nnet, accuracy = testPenData()
		penresult.append(accuracy)
		if(accuracy> penMax):
			penMax = accuracy

	penAvg = average(penresult)
	penStd = stDeviation(penresult)

	print('Pen max :', penMax)
	print('Pen average :', penAvg)
	print('Pen std: ', penStd)

def Q5CarData():
	carresult = []
	carMax = 0.0
	for x in range (0,5):
		nnet, accuracy = testPenData()
		carresult.append(accuracy)
		if(accuracy> carMax):
			carMax = accuracy

	carAvg = average(carresult)
	carStd = stDeviation(carresult)

	print('Car max :', carMax)
	print('Car average :', carAvg)
	print('Car std: ', carStd)




def main():

	# Q5CarData()
	# Q5PenData()
	
	# Q6PenData()
	Q6CarData()
	
if __name__ == "__main__":
    main()
