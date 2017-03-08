import sys

from single_threaded.ant_colony import AntColony
from sudoku_utils import *


def main(argv):
    print("Starting ACO ...")
    sudoku_matrix = np.loadtxt("s10a.txt")

    print("*** Single Threaded ***")
    number_of_ants = 700
    number_of_steps = 1000
    alpha = 0.1  # importance of pheromone trail
    beta = 0.9  # importance of heuristic value (heurisitc value = probability of selecting digit at position (x,y))
    rho = 0.2  # level of evaporation. Between 0(none) and 1(full evaporation)

    AntColony(sudoku_matrix, number_of_ants, number_of_steps, alpha, beta, rho).run()

    """
    print("*** Multi Threaded ***")

    ants = []

    for thread_number in range(0, 50):
        ant_thread = Ant(data, 20)
        ants.append(ant_thread)
        ant_thread.start()

    for ant in ants:
        ant.join()
    """

if __name__ == "__main__":
    main(sys.argv)
