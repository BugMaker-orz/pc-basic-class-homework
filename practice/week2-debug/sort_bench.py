import random, cProfile, pstats, io

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = key

def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

data = [random.randint(0, 10000) for _ in range(5000)]
pr = cProfile.Profile()
pr.enable()
insertion_sort(data.copy())
quicksort(data.copy())
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats(3)
print(s.getvalue())
