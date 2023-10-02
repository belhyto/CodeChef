import sys

def tsp(distance_matrix):

    num_cities = len(distance_matrix)
    all_sets = 2 ** num_cities
    dp = [[float('inf')] * num_cities for _ in range(all_sets)]
    for i in range(num_cities):
        dp[1 << i][i] = 0

    for subset in range(1, all_sets):
        for u in range(num_cities):
            if (subset >> u) & 1:  
                for v in range(num_cities):
                    if (subset >> v) & 1 and u != v: 
                        dp[subset][u] = min(dp[subset][u], dp[subset ^ (1 << u)][v] + distance_matrix[v][u])

    final_subset = (1 << num_cities) - 1
    min_tour_distance = min(dp[final_subset][u] + distance_matrix[u][0] for u in range(1, num_cities))

    return min_tour_distance

num_cities = int(input("Enter the number of cities: "))

distance_matrix = []
for i in range(num_cities):
    distance_matrix_row = input("Enter the distances from city {} to other cities separated by spaces: ".format(i))
    distance_matrix.append([float(number) for number in distance_matrix_row.split()])

minimum_tour_distance = tsp(distance_matrix)
print("The minimum tour distance is:", minimum_tour_distance)
import sys

def tsp(distance_matrix):

    num_cities = len(distance_matrix)
    all_sets = 2 ** num_cities
    dp = [[float('inf')] * num_cities for _ in range(all_sets)]
    for i in range(num_cities):
        dp[1 << i][i] = 0

    for subset in range(1, all_sets):
        for u in range(num_cities):
            if (subset >> u) & 1:  
                for v in range(num_cities):
                    if (subset >> v) & 1 and u != v: 
                        dp[subset][u] = min(dp[subset][u], dp[subset ^ (1 << u)][v] + distance_matrix[v][u])

    final_subset = (1 << num_cities) - 1
    min_tour_distance = min(dp[final_subset][u] + distance_matrix[u][0] for u in range(1, num_cities))

    return min_tour_distance

num_cities = int(input("Enter the number of cities: "))

distance_matrix = []
for i in range(num_cities):
    distance_matrix_row = input("Enter the distances from city {} to other cities separated by spaces: ".format(i))
    distance_matrix.append([float(number) for number in distance_matrix_row.split()])

minimum_tour_distance = tsp(distance_matrix)
print("The minimum tour distance is:", minimum_tour_distance)
