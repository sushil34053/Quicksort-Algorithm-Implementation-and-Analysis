import random
import time
import matplotlib.pyplot as plt

# Deterministic Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort Implementation
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Performance Analysis Function
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

def empirical_analysis():
    input_sizes = [100, 1000, 5000, 10000, 20000]
    distributions = {
        "Random": lambda n: [random.randint(0, 100000) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse Sorted": lambda n: list(range(n, 0, -1)),
    }

    results = {"Deterministic": {}, "Randomized": {}}

    for name, dist_func in distributions.items():
        results["Deterministic"][name] = []
        results["Randomized"][name] = []

        for size in input_sizes:
            arr = dist_func(size)

            time_det = measure_time(quicksort, arr.copy())
            time_rand = measure_time(randomized_quicksort, arr.copy())

            results["Deterministic"][name].append(time_det)
            results["Randomized"][name].append(time_rand)

    # Plot Results
    for name in distributions.keys():
        plt.figure(figsize=(10, 5))
        plt.plot(input_sizes, results["Deterministic"][name], label="Deterministic")
        plt.plot(input_sizes, results["Randomized"][name], label="Randomized")
        plt.title(f"Performance Comparison ({name} Distribution)")
        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (s)")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    print("Running empirical analysis...")
    empirical_analysis()

    # Theoretical Analysis
    print("\nTheoretical Analysis:")
    print("Best Case Time Complexity: O(n log n)")
    print("Average Case Time Complexity: O(n log n)")
    print("Worst Case Time Complexity: O(n^2)")
    print("Space Complexity: O(log n) due to recursion stack in the best case.")
