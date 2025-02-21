import heapq

heap = [3, 4, 5, 9,2]
heapq.heapify(heap) 
print("Heap heapify : ", heap)
print(heapq.heappop(heap)) 
print("Heap: " , heap)

# Create a list
data = [5, 3, 8, 1, 2]

# Convert the list into a heap
heapq.heapify(data)
print("Heap:", data)  # Output: [1, 2, 8, 3, 5]

# Push an element into the heap
heapq.heappush(data, 4)
print("After push:", data)  # Output: [1, 2, 4, 3, 5, 8]

# Pop the smallest element
smallest = heapq.heappop(data)
print("Smallest element:", smallest)  # Output: 1
print("After pop:", data)  # Output: [2, 3, 4, 8, 5]

# Example: Finding the K-th Smallest Element
def find_kth_smallest(nums, k):
    heapq.heapify(nums)  # Convert list to heap
    for _ in range(k - 1):
        heapq.heappop(nums)  # Remove k-1 smallest elements
    return heapq.heappop(nums)  # Return the k-th smallest

nums = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}-th smallest element:", find_kth_smallest(nums, k))  # Output: 7