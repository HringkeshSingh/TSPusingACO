# 🐜 Ant Colony Optimization for TSP

A Python implementation of Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman Problem (TSP). This implementation provides an efficient way to find near-optimal solutions for routing problems.

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/numpy-1.19+-blue.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

```python
import numpy as np
from ACO import AntColonyOptimization

# Example distance matrix
distances = np.array([
    [0, 2, 3, 4],
    [2, 0, 4, 3],
    [3, 4, 0, 2],
    [4, 3, 2, 0]
])

# Initialize and run ACO
aco = AntColonyOptimization(distances=distances, num_ants=10, num_iterations=100)
best_path, best_distance = aco.run()
```

## 📋 Prerequisites

- Python 3.6 or higher
- NumPy

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/HringkeshSingh/TSPusingACO.git
cd TSPusingACO
```

2. Install the required packages:
```bash
pip install numpy
```

## 🔧 Configuration

The `AntColonyOptimization` class accepts the following parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `distances` | Distance matrix between cities | Required |
| `num_ants` | Number of ants per iteration | Required |
| `num_iterations` | Number of iterations to run | Required |
| `alpha` | Pheromone importance factor | 1 |
| `beta` | Distance importance factor | 2 |
| `rho` | Pheromone evaporation rate | 0.5 |
| `Q` | Pheromone deposit factor | 100 |

## 📖 Example Usage

```python
# Create a more complex example
distances = np.array([
    [0, 2, 3, 4, 5],
    [2, 0, 4, 3, 6],
    [3, 4, 0, 2, 2],
    [4, 3, 2, 0, 7],
    [5, 6, 2, 7, 0]
])

# Initialize with custom parameters
aco = AntColonyOptimization(
    distances=distances,
    num_ants=20,
    num_iterations=150,
    alpha=1.5,
    beta=2.5,
    rho=0.3,
    Q=80
)

# Run optimization
best_path, best_distance = aco.run()

print(f"Optimal Path: {best_path}")
print(f"Total Distance: {best_distance}")
```

## 🧮 How It Works

The ACO algorithm mimics the behavior of ant colonies to find optimal paths:

1. **Initialization**: Sets up initial pheromone trails across all possible paths.
2. **Construction**: Ants construct solutions by probabilistically choosing paths based on:
   - Pheromone intensity
   - Distance between cities
3. **Update**: After each iteration:
   - Pheromones evaporate at rate `rho`
   - New pheromones are deposited based on path quality
4. **Iteration**: Process repeats until the best solution is found

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👥 Authors

* **Hringkesh Singh** 

## 🌟 Acknowledgments

* Based on Marco Dorigo's Ant Colony Optimization algorithm
* Inspired by nature's problem-solving capabilities

## 📞 Contact

Hringkesh Singh - hringkeshsingh.college@gmail.com

Project Link: [https://github.com/HringkeshSingh/TSPusingACO](https://github.com/HringkeshSingh/TSPusingACO)
