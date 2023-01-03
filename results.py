import random, time, sorts

# Configuration
N = 10000   #Base number of elements in arrays to be sorted
numIterations = 5   #Number of arrays to be generated


def bold(text):
    return '\033[1m' + text + '\033[0m'


def testSort(sortClass, arrs, arrsSorted):
    print(bold(f"Testing {sortClass.getName()} -"))
    print(f"\tBest time complexity:    {sortClass.getBestTime()}")
    print(f"\tAverage time complexity: {sortClass.getAvgTime()}")
    print(f"\tWorst time complexity:   {sortClass.getWorstTime()}")
    print(f"\tWorst space complexity:  {sortClass.getSpace()}")

    elapseds = []
    incorrect = False
    for i in range(numIterations):
        arr = arrs[i].copy()

        start = time.time()
        if sortClass.getName().lower() == "quicksort":
            sortClass.sort(arr, 0, len(arr)-1)
        else:
            sortClass.sort(arr)
        end = time.time()

        elapsed = end - start
        elapseds.append(elapsed)

        #Check correctness
        if arr != arrsSorted[i]:
            print("ALERT: The provided implementation for", sortClass.getName(), "has returned an incorrect output, no further tests will be done with this algorithm!")
            incorrect = True
            break
    
    if not incorrect:
        avgElapseds = sum(elapseds)/len(elapseds)
        print(f"\tAverage elapsed time for sorting {N} randomly generated numbers is", avgElapseds)
    print()


def generateArrs():
    testArrs = []
    testArrsSorted = []
    for i in range(numIterations):
        testArrs.append([])
        for j in range(N):
            testArrs[i].append(random.randint(0, N))      
        sortedCopy = testArrs[i].copy()
        sortedCopy.sort()
        testArrsSorted.append(sortedCopy)
    
    return testArrs, testArrsSorted


def main():
    arrs, arrsSorted = generateArrs()
    for sortClass in sorts.allSorts:
        testSort(sortClass, arrs, arrsSorted)

if __name__ == "__main__":
    main()