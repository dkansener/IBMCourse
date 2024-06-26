import math

points = [(1, 2), (4, 6)]

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    # return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2) alternative for math library

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("Noktalar arasındaki minimum mesafe:", min_distance)
