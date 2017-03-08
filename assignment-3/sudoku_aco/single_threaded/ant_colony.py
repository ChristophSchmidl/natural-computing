import random
import numpy as np
import copy
from sudoku_utils import *
import matplotlib.pyplot as plt


from single_threaded.ant import Ant


class AntColony:
    def __init__(self, sudoku_matrix, number_of_ants, number_of_steps, alpha=1, beta=3, rho=0.1,
                 pheromone_deposit_weight=1, initial_pheromone=1):
        self.sudoku_matrix = sudoku_matrix
        self.number_of_ants = number_of_ants
        self.number_of_steps = number_of_steps
        self.alpha = alpha  # importance of pheromone trail
        self.beta = beta  # importance of heuristic value (heurisitc value = probability of selecting digit at position?)
        self.rho = rho  # level of evaporation. Between 0(none) and 1(full evaporation)
        self.pheromone_deposit_weight = pheromone_deposit_weight
        self.initial_pheromone = initial_pheromone

        self.ants = []
        self.pheromone_matrix = None
        self.global_best_score = 0
        self.global_best_solution = None
        self.best_path_arr = None

        self.base_score = calculate_score(sudoku_matrix)
        self.best_score_statistics = []
        self.average_score_statistics = []

        # initial pheromone on 3 dimensional matrix on nodes which are available at the beginning
        # therefore, compute all available positions in the array and set the pheromones to 1

    def reset(self):
        self.global_best_score = 0
        self.global_best_solution = None
        self.best_path_arr = None
        self.ants = []

    def _create_ants(self):
        for ant_id in range(0, self.number_of_ants):
            self.ants.append(Ant(ant_id, self.alpha, self.beta, self.sudoku_matrix, self.pheromone_matrix))

    def run(self):
        self._create_pheromone_matrix()
        self._create_ants()

        # outer loop: number of steps for the whole colony
        for step in range(self.number_of_steps):
            # inner loop: let every ant search for a solution
            print("Step number: {}".format(step))
            summed_score = 0
            for ant in self.ants:
                # every ants solution modifies the pheromone_matrix,
                # so that the next ant in line can leverage the findings
                # of the previous ant
                self._add_pheromone(ant.find_solution(), ant.get_score())
                summed_score += ant.score
                if ant.score > self.global_best_score:
                    self.global_best_solution = ant.solution
                    self.global_best_score = ant.score
                    print("New best score of {} by ant {}".format(ant.score, ant.id))
                    self.print_current_best_sudoku_matrix()
                    self._check_for_highscore()
                ant.reset()  # So that the ant can be used again without its previous values
            self.average_score_statistics.append(summed_score / self.number_of_ants)
            self.best_score_statistics.append(self.global_best_score)

            # at the end of one step, every ant came up with a solution
            # and now the evaporation step/global update can take place
            self._perform_evaporation()

        print(self.global_best_score)

    def _perform_evaporation(self):
        for index, value in np.ndenumerate(self.pheromone_matrix):
            updated_pheromone = (1 - self.rho) * value
            self.pheromone_matrix[index] = updated_pheromone

    def _add_pheromone(self, solution, score, weight=1):
        # I've added ( 82 - score ) because the initial ACO algorithm is based on distance traveled.
        # The lower the distance, the better the solution. In this case, it is the opposite. The higher
        # the score, the better the solution. 82 - 81 = 1 (solved sudoku puzzle = highest pheromone)
        pheromone_to_add = self.pheromone_deposit_weight / (82 - score)

        # solution contains a list of triplets (x,y,digit)
        for i in solution:
            # pheromone_matrix[digit = digit - 1][x-position][y-position]
            self.pheromone_matrix[i[2] - 1][i[0]][[1]] += weight * pheromone_to_add

    def _create_pheromone_matrix(self):

        self.pheromone_matrix = np.zeros((9, 9, 9))
        empty_positions = get_empty_positions(self.sudoku_matrix)

        for position in empty_positions:
            candidate_digits = get_possible_digits_at_position(position[0], position[1], self.sudoku_matrix)
            for candidate in candidate_digits:
                self.pheromone_matrix[candidate - 1][position[0]][position[1]] = self.initial_pheromone

    def _check_for_highscore(self):
        if self.global_best_score == 81:
            self.print_current_best_sudoku_matrix()


    def print_current_best_sudoku_matrix(self):

        solution_matrix = copy.deepcopy(self.sudoku_matrix)
        for solution in self.global_best_solution:
            set_digit_at_position(solution[0], solution[1], solution[2], solution_matrix)
        print(solution_matrix)