import random


def partition(values, low, high):
    pivot = values[high]
    next_small = low

    for current in range(low, high):
        if values[current] <= pivot:
            values[next_small], values[current] = values[current], values[next_small]
            next_small += 1

    values[next_small], values[high] = values[high], values[next_small]
    return next_small


def quicksort(values, low, high, randomized=False):
    while low < high:
        if randomized:
            chosen = random.randint(low, high)
            values[chosen], values[high] = values[high], values[chosen]

        pivot_index = partition(values, low, high)

        if pivot_index - low < high - pivot_index:
            quicksort(values, low, pivot_index - 1, randomized)
            low = pivot_index + 1
        else:
            quicksort(values, pivot_index + 1, high, randomized)
            high = pivot_index - 1


if __name__ == "__main__":
    original = [7, 2, 9, 4]
    deterministic = original.copy()
    randomized = original.copy()

    quicksort(deterministic, 0, len(deterministic) - 1)
    quicksort(randomized, 0, len(randomized) - 1, randomized=True)

    print("Deterministic:", deterministic)
    print("Randomized:   ", randomized)
