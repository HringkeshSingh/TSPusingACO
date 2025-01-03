# ACO.py

import numpy as np
import random

class AntColonyOptimization:
    def __init__(self, distances, num_ants, num_iterations, alpha=1, beta=2, rho=0.5, Q=100):
        self.distances = distances
        self.num_cities = len(distances)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.pheromone = np.ones((self.num_cities, self.num_cities)) / self.num_cities

    def run(self):
        best_path = None
        best_distance = float('inf')
        for iteration in range(self.num_iterations):
            ant_paths = self.generate_ant_paths()
            self.update_pheromone(ant_paths)
            shortest_path, shortest_distance = self.get_shortest_path(ant_paths)
            if shortest_distance < best_distance:
                best_path = shortest_path
                best_distance = shortest_distance
        return best_path, best_distance

    def generate_ant_paths(self):
        ant_paths = []
        for ant in range(self.num_ants):
            path = self.generate_ant_path()
            ant_paths.append((path, self.calculate_path_distance(path)))
        return ant_paths

    def generate_ant_path(self):
        path = [0]  # Start from the first city
        while len(path) < self.num_cities:
            available_cities, probabilities = self.calculate_probabilities(path[-1], path)
            next_city = self.choose_next_city(available_cities, probabilities)
            path.append(next_city)
        path.append(path[0])  # Return to the first city
        return path



    def choose_next_city(self, available_cities, probabilities):
        return np.random.choice(available_cities, p=probabilities)


    def calculate_probabilities(self, current_city, path):
        pheromone_values = np.copy(self.pheromone[current_city])
        pheromone_values[path] = 0  # Setting zero pheromone for visited cities
        available_cities = [i for i in range(self.num_cities) if i not in path]
        probabilities = []
        total = 0
        for city in available_cities:
            probability = (pheromone_values[city] ** self.alpha) * ((1.0 / self.distances[current_city][city]) ** self.beta)
            probabilities.append(probability)
            total += probability
        probabilities = [prob / total for prob in probabilities]  # Normalize probabilities
        return available_cities, probabilities




    def calculate_path_distance(self, path):
        distance = sum(self.distances[path[i-1]][path[i]] for i in range(1, len(path)))
        distance += self.distances[path[-1]][path[0]]  # Return to starting city
        return distance

    def update_pheromone(self, ant_paths):
        pheromone_delta = np.zeros((self.num_cities, self.num_cities))
        for path, distance in ant_paths:
            for i in range(1, len(path)):
                pheromone_delta[path[i-1]][path[i]] += self.Q / distance
            pheromone_delta[path[-1]][path[0]] += self.Q / distance
        self.pheromone = (1 - self.rho) * self.pheromone + pheromone_delta

    def get_shortest_path(self, ant_paths):
        shortest_path, shortest_distance = min(ant_paths, key=lambda x: x[1])
        return shortest_path, shortest_distance