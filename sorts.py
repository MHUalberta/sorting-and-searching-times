#DISCLAIMER: All sorts used here are referenced from geeksforgeeks.org

from sortsclass import Sort

class QuickSort(Sort):
	def partition(self, array, low, high):
		# choose the rightmost element as pivot
		pivot = array[high]

		# pointer for greater element
		i = low - 1

		# traverse through all elements
		# compare each element with pivot
		for j in range(low, high):
			if array[j] <= pivot:

				# If element smaller than pivot is found
				# swap it with the greater element pointed by i
				i = i + 1

				# Swapping element at i with element at j
				(array[i], array[j]) = (array[j], array[i])

		# Swap the pivot element with the greater element specified by i
		(array[i + 1], array[high]) = (array[high], array[i + 1])

		# Return the position from where partition is done
		return i + 1


	def sort(self, array, low, high):
		if low < high:
			# Find pivot element such that
			# element smaller than pivot are on the left
			# element greater than pivot are on the right
			pi = self.partition(array, low, high)

			# Recursive call on the left of pivot
			self.sort(array, low, pi - 1)

			# Recursive call on the right of pivot
			self.sort(array, pi + 1, high)


class BubbleSort(Sort):
	def sort(self, arr):
		n = len(arr)
		# optimize code, so if the array is already sorted, it doesn't need
		# to go through the entire process
		swapped = False
		# Traverse through all array elements
		for i in range(n-1):
			# range(n) also work but outer loop will
			# repeat one time more than needed.
			# Last i elements are already in place
			for j in range(0, n-i-1):

				# traverse the array from 0 to n-i-1
				# Swap if the element found is greater
				# than the next element
				if arr[j] > arr[j + 1]:
					swapped = True
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
			
			if not swapped:
				# if we haven't needed to make a single swap, we
				# can just exit the main loop.
				return


class HeapSort(Sort):
	def heapify(self, arr, N, i):
		largest = i # Initialize largest as root
		l = 2 * i + 1	 # left = 2*i + 1
		r = 2 * i + 2	 # right = 2*i + 2

		# See if left child of root exists and is
		# greater than root
		if l < N and arr[largest] < arr[l]:
			largest = l

		# See if right child of root exists and is
		# greater than root
		if r < N and arr[largest] < arr[r]:
			largest = r

		# Change root, if needed
		if largest != i:
			arr[i], arr[largest] = arr[largest], arr[i] # swap

			# Heapify the root.
			self.heapify(arr, N, largest)


	def sort(self, arr):
		N = len(arr)

		# Build a maxheap.
		for i in range(N//2 - 1, -1, -1):
			self.heapify(arr, N, i)

		# One by one extract elements
		for i in range(N-1, 0, -1):
			arr[i], arr[0] = arr[0], arr[i] # swap
			self.heapify(arr, i, 0)


class InsertionSort(Sort):
	def sort(self, arr):
		for i in range(1, len(arr)):
			up = arr[i]
			j = i - 1
			while j >= 0 and arr[j] > up:
				arr[j + 1] = arr[j]
				j -= 1
			arr[j + 1] = up	
		return arr	
			

class ShellSort(Sort):
	def sort(self, arr):
		n = len(arr)
		gap = n // 2 
		while gap > 0: 
			for i in range(gap,n): 
				temp = arr[i] 
				j = i 
				while  j >= gap and arr[j-gap] > temp: 
					arr[j] = arr[j-gap] 
					j = j - gap 
				arr[j] = temp 
			gap = gap // 2


# Instantiate the sort methods with their respective complexities.
quickSort = QuickSort("nlogn", "nlogn", "n^2", "logn")
bubbleSort = BubbleSort("n", "n^2", "n^2", "1")
heapSort = HeapSort("nlogn", "nlogn", "nlogn", "n")
insertionSort = InsertionSort("n", "n^2", "n^2", "1")
shellSort = ShellSort("n", "[nlogn]^2", "[nlogn]^2", "1")
allSorts = [quickSort, bubbleSort, heapSort, insertionSort, shellSort]