import random
from statistics import median
from time import perf_counter

from quicksort import quicksort


def time_quicksort(original, expected, randomized):
    times = []

    for _ in range(5):
        values = original.copy()

        start = perf_counter()
        quicksort(values, 0, len(values) - 1, randomized=randomized)
        elapsed = perf_counter() - start

        assert values == expected, "Quicksort returned the wrong order"
        times.append(elapsed * 1000)

    return median(times)


random.seed(42)
input_rng = random.Random(42)

print(f"{'Size':>5}  {'Input':<15}  {'Deterministic':>14}  {'Randomized':>12}")

for size in (500, 2000, 5000):
    ordered = list(range(size))
    shuffled = ordered.copy()
    input_rng.shuffle(shuffled)

    inputs = {
        "Random": shuffled,
        "Sorted": ordered,
        "Reverse-sorted": ordered[::-1],
    }

    for name, values in inputs.items():
        fixed_ms = time_quicksort(values, ordered, randomized=False)
        random_ms = time_quicksort(values, ordered, randomized=True)
        print(f"{size:>5}  {name:<15}  {fixed_ms:>11.3f} ms  {random_ms:>9.3f} ms")
