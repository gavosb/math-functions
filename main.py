#Miscellaneous math related tools
#Some of these are not properly documented; their purpose is primarily for reference.
#Documentation should be improved later.
#Signed: Gavin

from random import randint #import randint

#output the amount of integers within each section of ten integers for ten whole sections in an array of given number of elements
#note: this was briefly converted into a class and has not been tested
class countTens:
    def __init__(self, lov):
        size = 1000
        lov = [] #The main array of random integers

    #Populates the list lov with random integers of the value between 0 to 99 for (size) amount of times
    def createList(self, self.size):
        for i in range(self.size):
            self.lov.append(randint(0,99))

    #Iterates through the entire list searching for numbers that fall into the current section
    def countSection(self, section):
        amount = 0
        for i in self.lov:
            if i in range(section-9, section):
                amount += 1
        print(str(section) + ": " + str(amount))

    #Iterates through each section of 10 integers, building on top of the previous section
    def iterateSections(self):
        currentSection = -1
        for i in range(10):
            for o in range(10):
                currentSection += 1
            countSection(currentSection)

#adds together all elements of a list
#pre: given list
#post: all elements of list returned as sum
def sumUp(L):
    n = len(L)
    i = 0
    sum = 0
    while i < n:
        sum = sum + L[i]
        i = i + 1
    return sum

#counts through a list and returns amount of odd numbers
#pre: given list of numbers
#post: returns the amount of odd numbers
def countOdd(lov):
    oddnums = 0
    for i in lov:
        if i % 2 != 0:
            oddnums += 1
    return oddnums

#predicate: determines whether a list is in ascending order or not
#pre: flag is true, list is given; 
#post: flag is false if list is not ascending; returns flag
def isSorted(lov):

    flag = True
    i = 0
    while i < len(lov) and flag == True: #iterates through list
        if lov[i-1] > lov[i] and i != 0: #flags false if a single number is not in ascending order
            flag = False
        i += 1
    return flag

#predicate function determining if a number is perfect; returns true or false
#pre: a single number is passed as a parameter
#post: flag is false if sum of divisors is not equal to given number; returns flag
def isPerfect(num):
    flag = True
    i = 0
    L = []
    while i < num and flag:
        if i != 0 and num % i == 0:
            L.append(i)
        i += 1
    if sumUp(L) != num:
        flag = False
    return flag

def findAverage(L):
    n = len(L)
    i = 0
    sum = sumUp(L)
    avg = 0
    if n > 0:
        avg = sum/n
    return avg
    
def allOdd(L):
    n = len(L)
    i = 0
    flag = True
    while i < n and flag:
        elem = L[i]
        if elem % 2 == 0:
            flag = False
        i = i + 1
    return flag    

#counts the amount of negative numbers in a list
def countNegative(lov):
    lon = 0 #number of negative values
    for i in lov:
        if i < 0:
            lon += 1
    return lon

# findLargestFromPoint - return the index of the largest value in the list,
#   given a specific starting point in the list
# preconditions: start: an integer in [0..len(lov)]
# return value: index of largest value found; integer in [start..len(lov)]
def findLargestFromPoint(lov, start):
    largestSoFar = lov[start]
    largestIndex = start
    current = start+1
    while (current < len(lov)):
        if (lov[current] > largestSoFar):
            largestSoFar = lov[current]
            largestIndex = current
        current = current + 1
    return (largestIndex)

# selectionSort - implementation of the Selection Sort algorithm
# preconditions: none
def selectionSort(lov):
    leftEdge = 0
    while (leftEdge < (len(lov)-1)):
        biggestPosition = findLargestFromPoint(lov, leftEdge)
        temp = lov[biggestPosition]
        lov[biggestPosition] = lov[leftEdge]
        lov[leftEdge] = temp
        
        leftEdge = leftEdge + 1
        
    return lov

# findLargest - return the index of the largest value in the parameter list
# preconditions: lov is a list of integer values
# return value: integer in [0..len(listNum)]
def findLargest(lov):
    listSize = len(lov)
    largestSoFar = lov[0]
    current = 1
    while (current < listSize):
        if (lov[current] > largestSoFar):
            largestSoFar = lov[current]
        current = current + 1
    return(largestSoFar)

# helper function that takes as input a single value and returns the sum of its proper divisors
def factorSum (value):
	sumOfDivisors = 1
	index = 2
	while index < value:
		if value % index == 0: #proper divisor
			sumOfDivisors += index
		index = index + 1
	return sumOfDivisors

# function to count the number of amicable pairs of numbers present in a list of integers
def amicablePairs (lov):
	pairCnt = 0
	outer = 0
	while outer < len(lov):
		inner = outer + 1
		while inner < len(lov):
			outerSum = factorSum(lov[outer])
			innerSum = factorSum(lov[inner])
			if outerSum == lov[inner] and innerSum == lov[outer]:
				pairCnt += 1
			inner += 1
		outer += 1
	return pairCnt

#Computes average distance between numbers in a list
#pre: list of integers is passed to function (L)
#post: returns absolute value of distance between each integer in the list
def computeAvgGap(L):
	result = 0
	distances = []
	index = 0
	
	while index < len(L):
		if not index+2 > len(L):
			distances.append(L[index] - L[index+1])
		index += 1
		
	for i in distances:
		result += abs(i)
	result = result / len(distances)
		
	return result

#given an integer n, return True or False as to whether n is a prime number
#pre: n is an integer
#post: returns True or False indicating whether n is prime
def isPrime(n):
	flag = True
	if n >= 2: #n must be greater or equal to 2 so i gets the proper index
		for i in range(n):
			if i > 1 and n % i == 0:
				flag = False
	return flag

#given an integer m, return the number of prime numbers from 1 to m
#pre: m is an integer, isPrime() is an existing function
#post: returns number of prime numbers within m
def countPrimes(m):
	i = 0
	count = 0
	while i < m and m >= 2: #m (and later i) must be greater or equal to 2 for indexing
		if i >= 2 and isPrime(i) == True:
			count += 1
		i += 1
	return count

#given an array --called L-- of integers, return True or False as to whether or not each number in L is a multiple of the immediately previous number in the list.
#pre: L is a list
#post: returns True or False indicating whether list is a sequence of multiples
def areMultiples(L):
	flag = True
	i = 0
	while i < len(L):
		if i > 1 and not L[i] % L[i-1] == 0: #i must be greater than 1 for indexing
			flag = False
		i += 1
	return flag

#In a Fibonacci sequence, every element beginning with the 3rd element is equal to the sum of the 2 previous elements
#pre: given 3 inputs - s1, s2, and length are integers
#post: returns list including a fibonacci sequence derived from inputs
def createFib(s1, s2, length):
	sequence = [s1, s2]
	i = 0
	while i < length:
		if i > 1:
			sequence.append(sequence[i-1] + sequence[i-2])
		i += 1
	return sequence
