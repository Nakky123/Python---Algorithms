def selectionsort(arr, k):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if i == k-1:
            print(arr[i], arr[min_idx])

# Sample input
input_values = "7 10\n50 40 70 10 30 20 60\n"

# Split the input values
lines = input_values.strip().split('\n')
n, k = map(int, lines[0].split())
arr = list(map(int, lines[1].split()))

# Perform selection sort and print swapped numbers at the kth step
selectionsort(arr, k)
