import random

a = [i for i in range(100)]
random.shuffle(a)

def bubble_sort(arr):
	if len(arr) < 2:
		return arr
	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr

print bubble_sort(a)