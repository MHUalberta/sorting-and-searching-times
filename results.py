import random, time, sorts
from threading import Thread, Semaphore

# Setup
N = 1000           #Base number of elements in arrays to be sorted
numIterations = 5   #Number of arrays to be generated and averaged over
threading = True
if threading:
    printSem = Semaphore()


def bold(text):
    '''
    Generic function that bolds provided text.
    Args -
            text (String/Int): Text to be bolded.
    Returns -
            A bolded string.
    '''
    return '\033[1m' + text + '\033[0m'


def printSortSummary(sortClass, elapsedTimes, isCorrect):
    '''
    Print summary stats for a sort.
    Args -
            sortClass (Sort): An object of type Sort.
            elapsedTime (List<Float>): A list of all the times taken to finish sorting N elements over numIterations runs.
            isCorrect (Bool): A boolean representing wether the sort algorithm returned correct results or not.
    '''
    if threading:
        printSem.acquire()

    #Critical section if threading##############
    print(bold(f"Stats for {sortClass.getName()} -"))
    print(f"\tBest time complexity:    {sortClass.getBestTime()}")
    print(f"\tAverage time complexity: {sortClass.getAvgTime()}")
    print(f"\tWorst time complexity:   {sortClass.getWorstTime()}")
    print(f"\tWorst space complexity:  {sortClass.getSpace()}")
    if isCorrect:
        avgElapseds = sum(elapsedTimes)/len(elapsedTimes)
        print(f"\tAverage elapsed time for sorting {N} randomly generated numbers is {avgElapseds}\n")
    else:
        print(f"\tERROR: The provided implementation for {sortClass.getName()} has returned an incorrect output!\n")
    ############################################

    if threading:
        printSem.release()
    

def testSort(sortClass, arrs, arrsSorted):
    '''
    Tests a given sorting algorithm over an array and records its stats and correctness.
    Args -
            sortClass (Sort): An object of type Sort.
            arrs (List<Float>): A list of N unsorted numbers.
            arrsSorted (List<Float>): Sorted arrs.
    '''
    elapseds = []
    isCorrect = True
    for i in range(numIterations):
        arr = arrs[i].copy()    #Do not want to overwrite the original array since multiple sorting algorithms will sort with it.

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
            isCorrect = False
            break
    
    printSortSummary(sortClass, elapseds, isCorrect)


def generateArrs():
    '''
    Generates numIterations arrays of N random numbers.
    Returns -
            numIterations arrays of N random numbers.
            numIterations arrays of N random numbers, sorted.
    '''
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


def startTestingWOThreading(arrs, arrsSorted):
    '''
    Analyze performance of all the sorting algorithms in the <sorts> module
    Args -
            arrs (List<Float>): A list of N unsorted numbers.
            arrsSorted (List<Float>): Sorted arrs.
    '''
    for sortClass in sorts.allSorts:
        testSort(sortClass, arrs, arrsSorted)


def startTestingWThreading(arrs, arrsSorted):
    '''
    Analyze performance of all the sorting algorithms in the <sorts> module. This version of the function uses threading by running each algorithm on a seperate thread.
    Args -
            arrs (List<Float>): A list of N unsorted numbers.
            arrsSorted (List<Float>): Sorted arrs.
    '''
    threads = []
    for sortClass in sorts.allSorts:    
        thread = Thread(target=testSort, args=(sortClass, arrs, arrsSorted))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


def main():
    arrs, arrsSorted = generateArrs()

    if threading:
        startTestingWThreading(arrs, arrsSorted)
    else:
        startTestingWOThreading(arrs, arrsSorted)
    
          
if __name__ == "__main__":
    main()