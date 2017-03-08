import sys

from single_threaded.ant_colony import AntColony
from sudoku_utils import *
import matplotlib.pyplot as plt


def plot_average_stats(name, ant_colonies):
    plt.figure()

    for colony in ant_colonies:
        plt.plot(list(range(0, colony.number_of_steps)), colony.average_score_statistics, lw=2,
                 label='Beta value: {}'.format(colony.beta))

    plt.title('Exercise 5: Average Score for {}'.format(name))
    plt.plot([0, ant_colonies[0].number_of_steps], [ant_colonies[0].base_score, ant_colonies[0].base_score], color='navy', lw=2,
             linestyle='--', label='Base Score at {}'.format(ant_colonies[0].base_score))
    plt.xlim([0.0, ant_colonies[0].number_of_steps])
    plt.ylim([0.0, 81])
    plt.xlabel('Number of steps')
    plt.ylabel('Average score value')
    plt.legend(loc="lower right")


    plt.draw()


def plot_best_stats(name, ant_colonies):
    plt.figure()

    for colony in ant_colonies:
        plt.plot(list(range(0, colony.number_of_steps)), colony.best_score_statistics, lw=2,
                 label='Beta value: {}'.format(colony.beta))


    plt.title('Exercise 5: Global Score for {}'.format(name))

    print("Base score: {}".format(ant_colonies[0].base_score))

    plt.plot([0, ant_colonies[0].number_of_steps], [ant_colonies[0].base_score, ant_colonies[0].base_score], color='navy', lw=2,
             linestyle='--', label='Base Score at {}'.format(ant_colonies[0].base_score))
    plt.xlim([0.0, ant_colonies[0].number_of_steps])
    plt.ylim([0.0, 81])
    plt.xlabel('Number of steps')
    plt.ylabel('Best global score value')
    plt.legend(loc="lower right")
    plt.draw()


def main(argv):
    print("Starting ACO ...")
    s10a = np.loadtxt("s10a.txt")
    s10b = np.loadtxt("s10b.txt")
    s11a = np.loadtxt("s11a.txt")
    s11b = np.loadtxt("s11b.txt")

    print("*** Single Threaded ***")
    number_of_ants = 10
    number_of_steps = 10
    alpha = 0.5  # importance of pheromone trail
    #beta = 0.5  # importance of heuristic value (heurisitc value = probability of selecting digit at position (x,y))
    rho = 0.002  # level of evaporation. Between 0(none) and 1(full evaporation)

    beta_values = [0, 0.5, 1, 1.5, 2]
    sudoku_files = [s10a, s10b, s11a, s11b]

    colonies = []

    for file in sudoku_files:
        for beta in beta_values:
            colony = AntColony(file, number_of_ants, number_of_steps, alpha, beta, rho)
            print(file)
            colony.run()
            print(colony.base_score)
            colonies.append(colony)

    plot_average_stats("s10a.txt", colonies[0:5])
    plot_best_stats("s10a.txt", colonies[0:5])

    plot_average_stats("s10b.txt", colonies[5:10])
    plot_best_stats("s10b.txt", colonies[5:10])

    plot_average_stats("s11a.txt", colonies[10:15])
    plot_best_stats("s11a.txt", colonies[10:15])

    plot_average_stats("s11b.txt", colonies[15:20])
    plot_best_stats("s11b.txt", colonies[15:20])


    plt.show()



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
