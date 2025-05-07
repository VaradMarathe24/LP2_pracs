def greedy_selection_sort(arr):
    n = len(arr)
    sorted_arr = []
    visited = [False] * n

    print("\nSorting Process:")

    for step in range(n):
        min_value = float('inf')
        min_index = -1

        for i in range(n):
            if not visited[i] and arr[i] < min_value:
                min_value = arr[i]
                min_index = i

        visited[min_index] = True
        sorted_arr.append(min_value)

        print(f"Step {step+1}: Selected {min_value}, Sorted so far: {sorted_arr}")

    return sorted_arr

# ------------------------ Main Program ------------------------

# Take user input
arr = list(map(int, input("Enter array elements separated by space: ").split()))

print("\nOriginal Array:", arr)

# Sort the array using Greedy Selection Sort
sorted_arr = greedy_selection_sort(arr)

# Final output
print("\nFinal Sorted Array:", sorted_arr)
