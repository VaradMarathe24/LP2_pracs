def greedy_selection_sort(arr):
    n = len(arr)

    # Edge case: If the array is empty, return an empty list
    if n == 0:
        print("Array is empty. Nothing to sort.")
        return []

    sorted_arr = []              # This will store the final sorted elements
    visited = [False] * n       # Keeps track of which elements have been selected
    total_comparisons = 0       # To count how many comparisons are made during the sort

    print("\nSorting Process:")

    # Outer loop runs n times to select n smallest elements one by one
    for step in range(n):
        min_value = float('inf')  # Start with the maximum possible value
        min_index = -1            # To track the index of the minimum value

        # Inner loop to find the smallest unvisited element
        for i in range(n):
            total_comparisons += 1  # Count each comparison
            if not visited[i] and arr[i] < min_value:
                min_value = arr[i]
                min_index = i

        # Mark the selected element as visited
        visited[min_index] = True
        # Add the selected smallest element to the sorted array
        sorted_arr.append(min_value)

        # Show the selected element and the sorted array so far
        print(f"Step {step+1}: Selected {min_value} (index {min_index}), Sorted so far: {sorted_arr}")

    # Display the total number of comparisons made
    print(f"\nTotal comparisons made: {total_comparisons}")
    return sorted_arr

# ------------------------ Main Program ------------------------

# Take user input as a list of integers
arr = list(map(int, input("Enter array elements separated by space: ").split()))

print("\nOriginal Array:", arr)

# Call the Greedy Selection Sort function
sorted_arr = greedy_selection_sort(arr)

# Display the final sorted array
print("\nFinal Sorted Array:", sorted_arr)


# Time complexity: O(n^2)
#Space Complexity: O(1)
#comparison based greedy sorting algorithm 
'''less swaps than bubble sort
non adaptive non recursive not stable in place sorting algorithm '''

