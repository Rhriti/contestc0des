def isPossible(A, B, ColorA, ColorB):
    n = len(A)
    m = len(B)

    # Create a dictionary to store the indices of elements in array A with each color
    colorIndexA = {}
    for i in range(n):
        if ColorA[i] not in colorIndexA:
            colorIndexA[ColorA[i]] = []
        colorIndexA[ColorA[i]].append(i)

    # Create a dictionary to store the indices of elements in array B with each color
    colorIndexB = {}
    for i in range(m):
        if ColorB[i] not in colorIndexB:
            colorIndexB[ColorB[i]] = []
        colorIndexB[ColorB[i]].append(i)

    # Check if it is possible to sort array A using swaps
    for color in colorIndexA.keys():
        # Get the indices of elements in array A and B with this color
        indicesA = colorIndexA[color]
        indicesB = colorIndexB[color]

        # Count the number of elements in each position in array B
        countB = [0] * (m + 1)
        for index in indicesB:
            countB[index + 1] += 1

        # Get the starting positions of each color in array B
        startingPositionsB = [0] * (n + 1)
        for i in range(1, n + 1):
            startingPositionsB[i] = startingPositionsB[i - 1] + countB[i - 1]

        # Sort the indices of elements in array B using counting sort
        sortedIndicesB = []
        for index in indicesB:
            sortedIndicesB.append(None)
        for index in indicesB:
            sortedIndex = startingPositionsB[ColorB[index]]
            sortedIndicesB[sortedIndex] = index
            startingPositionsB[ColorB[index]] += 1

        # Check if the indices of elements in array A with this color can be sorted in the same order
        if sortedIndicesB != indicesA:
            return False

    return True

# Example usage
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    ColorA=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ColorB=list(map(int,input().split()))

    print(isPossible(A, B, ColorA, ColorB))
