import math

def perpendicularDistance(points, line):
    a, b, c = line
    min_distance = float('inf')
    min_index = -1

    for i in range(len(points)):
        x, y = points[i]
        distance = abs(a * x + b * y + c) / math.sqrt(a ** 2 + b ** 2)
        
        if distance < min_distance or (distance == min_distance and i < min_index):
            min_distance = distance
            min_index = i

    return points[min_index]
