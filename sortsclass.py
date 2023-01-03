from abc import ABC, abstractmethod

class Sort(ABC):
    '''
    Parent sorting class. All sorting subclasses are to inherit this class and give their own definitions for the sort method.
    Args -
            time (String): The time complexity at which the sorting algorithm runs at.
            space (String): The space complexity at which the sorting algorithm runs at.
    '''
    def __init__(self, bestTime, avgTime, worstTime, space) -> None:
        assert isinstance(bestTime , str) and \
               isinstance(avgTime , str) and \
               isinstance(worstTime , str) and \
               isinstance(space, str) , \
               "time and space complexities must be string values relative to n, without the outer O()"

        self.bestTime = f'O({bestTime.strip("oO()")})'
        self.avgTime = f'O({avgTime.strip("oO()")})'
        self.worstTime = f'O({worstTime.strip("oO()")})'
        self.space = f'O({space.strip("oO()")})'
    
    def getBestTime(self):
        return self.bestTime
    
    def getAvgTime(self):
        return self.avgTime

    def getWorstTime(self):
        return self.worstTime

    def getSpace(self):
        return self.space
    
    def getName(self):
        return self.__class__.__name__
    
    @abstractmethod
    def sort(self):
        pass