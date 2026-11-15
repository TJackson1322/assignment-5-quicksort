# Assignment 5 Quicksort

This project compares deterministic Quicksort with randomized Quicksort. The deterministic version uses the last value as the pivot. The randomized version selects a pivot from the current section and moves it to the last position so both versions can use the same partition function.

## Run the code

From the repository folder, use Python 3:

```bash
python3 quicksort.py
python3 benchmark.py
```

The first script sorts a four-number example with both versions. The benchmark uses shuffled, sorted, and reverse-sorted lists of 500, 2,000, and 5,000 distinct integers. Each timing is the median of five runs, in milliseconds. The script checks the result after each run.

## Benchmark findings

On the original MacBook run, the sorted list of 5,000 integers took 691.614 ms with the fixed pivot and 4.097 ms with the random pivot. The randomized version was faster on sorted and reverse-sorted inputs at every size tested. The fixed-pivot version was slightly faster on the shuffled inputs. Timings vary by machine and run.
