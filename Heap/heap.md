# Heap (heapq module)

## A min-heap implementation using the heapq module.

## What is a Heap?

### - A heap is a specialized tree-based data structure that satisfies the heap property. It is commonly implemented as a binary heap, which is a complete binary tree where:

- Min-Heap: The value of each node is greater than or equal to its parent, and the smallest element is at the root.

- Max-Heap: The value of each node is less than or equal to its parent, and the largest element is at the root.

#### In Python, the heapq module provides a min-heap implementation.

### Why Do We Use Heaps?

- Heaps are used for efficiently managing data where you frequently need to:
  - Access the smallest (or largest) element quickly.
  - Insert new elements while maintaining the heap property.
  - Remove the smallest (or largest) element efficiently.

### Common Use Cases:

- Priority Queues: Heaps are the backbone of priority queues, where elements are processed based on their priority (e.g., smallest or largest value).

- Dijkstra’s Algorithm: Used in graph algorithms to efficiently find the shortest path.

- Heap Sort: A sorting algorithm that uses heaps.

- K-th Smallest/Largest Element: Finding the K-th smallest or largest element in a collection.

### How Does a Heap Work?

- A heap is typically represented as an array (or list in Python). For a node at index i:
  - Its left child is at index 2\*i + 1.
  - Its right child is at index 2\*i + 2.
  - Its parent is at index (i-1)//2.

### Heap Operations:

- Insert (Push):

  - Add the new element to the end of the array.

  - "Bubble up" the element to its correct position to maintain the heap property.

- Remove (Pop):

  - Remove the root element (smallest in a min-heap).

  - Move the last element to the root.

  - "Bubble down" the element to its correct position to maintain the heap property.

### Heap in Python: heapq Module

- Python provides the heapq module to work with heaps. It implements a min-heap by default.
  Key Functions:

- heapq.heappush(heap, item): Inserts an item into the heap.

- heapq.heappop(heap): Removes and returns the smallest item from the heap.

- heapq.heapify(list): Converts a list into a heap in-place.

- heapq.heappushpop(heap, item): Pushes an item and then pops the smallest item.

- heapq.heapreplace(heap, item): Pops the smallest item and then pushes a new item.

## How Does Heapify Work?

- The heapify function rearranges the elements of a list to satisfy the heap property. Here’s how it works:

  - Start from the last non-leaf node (i.e., (n//2 - 1)).

  - For each node, ensure it satisfies the heap property by "bubbling down" the node.

  - Repeat until the entire list is a valid heap.

## Why Use a Heap Instead of a List?

Operation | List | Heap
Insert | O(1) | O(log n)
Remove Min/Max | O(n) | O(log n)
Find Min/Max | O(n) | O(1)

- Heaps are much faster for finding and removing the smallest (or largest) element compared to a list.

- They are space-efficient since they are implemented as arrays.

# Summary

- A heap is a tree-based data structure that efficiently maintains the smallest (or largest) element at the root.

- It is used for priority queues, sorting, and graph algorithms.

- In Python, the heapq module provides a min-heap implementation.

- Heaps are faster than lists for accessing and removing the smallest/largest element.
