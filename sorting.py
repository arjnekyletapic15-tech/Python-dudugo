"""Assessment 3.7: Sorting Algorithms
Type any full name and press Enter to see it sorted.

Rules:
  - Build an array from the letters of the name.
  - Names with symbols are excluded (only letters are kept).
  - Duplicate letters are discarded.
  - Keep two arrays: unsorted and sorted.
Sorting method: Bubble Sort.
"""


def build_array(full_name):
    """Keep letters only (no spaces/symbols), discard duplicates, keep original order."""
    letters = []
    for ch in full_name.upper():
        if not ch.isalpha():      # exclude spaces and symbols
            continue
        if ch in letters:         # discard duplicate letters
            continue
        letters.append(ch)
    return letters


def bubble_sort(arr):
    """Return a sorted copy of arr (ascending) using Bubble Sort."""
    data = arr[:]                 # copy so the unsorted array stays unchanged
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:           # already sorted, stop early
            break
    return data


if __name__ == "__main__":
    print("Sorting Algorithm (Bubble Sort)")
    print("Type a name and press Enter. Type q to quit.\n")

    while True:
        full_name = input("Enter a name: ").strip()

        if full_name.lower() == "q":
            print("Goodbye!")
            break

        unsorted_array = build_array(full_name)

        if not unsorted_array:
            print("No letters found. Please enter a name.\n")
            continue

        sorted_array = bubble_sort(unsorted_array)

        print("Unsorted array :", unsorted_array)
        print("Sorted array   :", sorted_array)
        print()