import random
import sys
import time
import matplotlib.pyplot as plt

# Set recursion limit for large arrays in recursive binary search
sys.setrecursionlimit(2000000)

# ==================== 1. Search Algorithms ====================

# A. Simple Sequential Search
def sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return True, comparisons
    return False, comparisons

# B. Optimised Sequential Search (for sorted tables)
def optimised_sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return True, comparisons
        elif item > target:  # Early stop if current item exceeds target
            return False, comparisons
    return False, comparisons

# C. Iterative Binary Search
def binary_search_iterative(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return True, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False, comparisons

# D. Recursive Binary Search
def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return False, comparisons
    
    mid = (low + high) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return True, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# ==================== 2. Running Experiments ====================

def run_all_experiments():
    sizes = [1000, 10000, 1000000]  # Required array sizes (10^3, 10^4, 10^6)
    num_tests = 30                  # Number of tests per case
    
    results = {
        'Sequential Simple': {'time': [], 'comp': []},
        'Optimised Sequential': {'time': [], 'comp': []},
        'Binary Iterative': {'time': [], 'comp': []},
        'Binary Recursive': {'time': [], 'comp': []}
    }

    print("--- Running Complete Search Algorithms Comparison ---")

    for size in sizes:
        print(f"Testing for array size: {size}...")
        
        t_seq, c_seq = 0, 0
        t_opt, c_opt = 0, 0
        t_bin_i, c_bin_i = 0, 0
        t_bin_r, c_bin_r = 0, 0

        for _ in range(num_tests):
            # Generate sorted random array
            arr = sorted([random.randint(1, size * 10) for _ in range(size)])
            target = random.choice(arr) # Pick an existing random element to search for

            # 1. Sequential Search
            start = time.perf_counter()
            _, comp = sequential_search(arr, target)
            t_seq += (time.perf_counter() - start)
            c_seq += comp

            # 2. Optimised Sequential Search
            start = time.perf_counter()
            _, comp = optimised_sequential_search(arr, target)
            t_opt += (time.perf_counter() - start)
            c_opt += comp

            # 3. Binary Search Iterative
            start = time.perf_counter()
            _, comp = binary_search_iterative(arr, target)
            t_bin_i += (time.perf_counter() - start)
            c_bin_i += comp

            # 4. Binary Search Recursive
            start = time.perf_counter()
            _, comp = binary_search_recursive(arr, target, 0, len(arr) - 1)
            t_bin_r += (time.perf_counter() - start)
            c_bin_r += comp

        # Store average results over 30 tests
        results['Sequential Simple']['time'].append(t_seq / num_tests)
        results['Sequential Simple']['comp'].append(c_seq / num_tests)

        results['Optimised Sequential']['time'].append(t_opt / num_tests)
        results['Optimised Sequential']['comp'].append(c_opt / num_tests)

        results['Binary Iterative']['time'].append(t_bin_i / num_tests)
        results['Binary Iterative']['comp'].append(c_bin_i / num_tests)

        results['Binary Recursive']['time'].append(t_bin_r / num_tests)
        results['Binary Recursive']['comp'].append(c_bin_r / num_tests)

    # ==================== 3. Plotting Results ====================
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Execution Time
    for alg in results:
        ax1.plot(sizes, results[alg]['time'], marker='o', label=alg)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Array Size (N)')
    ax1.set_ylabel('Execution Time (seconds)')
    ax1.set_title('Comparison of Execution Time (Log Scale)')
    ax1.legend()
    ax1.grid(True)

    # Plot 2: Number of Comparisons
    for alg in results:
        ax2.plot(sizes, results[alg]['comp'], marker='s', label=alg)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Array Size (N)')
    ax2.set_ylabel('Average Comparisons Count')
    ax2.set_title('Comparison of Comparisons Count (Log Scale)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig('all_search_algorithms_comparison.png')
    plt.show()

if __name__ == "__main__":
    run_all_experiments()