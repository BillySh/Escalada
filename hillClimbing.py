
# Define the objective function you want to optimize
def objective_function(x):
    return -x**2  # A simple quadratic function for demonstration

# Define a function to generate neighbors for a given solution x
def generate_neighbors(x):
    neighbor1 = x + 0.1
    neighbor2 = x - 0.1
    return [neighbor1, neighbor2]

def hill_climbing(f, x0):
    x = x0  # initial solution
    while True:
        neighbors = generate_neighbors(x)  # generate neighbors of x
        # find the neighbor with the highest function value
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):  # if the best neighbor is not better than x, stop
            return x
        x = best_neighbor  # otherwise, continue with the best neighbor

if __name__ == "__main__":
    x0 = 2.0  # Initial solution
    result = hill_climbing(objective_function, x0)
    print(f"Best solution found: {result}")
    print(f"Objective function value at the best solution: {objective_function(result)}")
