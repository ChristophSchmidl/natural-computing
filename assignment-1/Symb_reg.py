# BASIC LIBS
import sys
import operator
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# GENETIC PROGRAMMING LIB
from deap import algorithms, base, creator, tools, gp

# PROTECT FROM DIVIDING BY ZERO
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1000

# PROTECT FROM TAKING LOG OF ZERO
def protectedLog(arg):
    try:
        return math.log(arg)
    except ValueError:
        return -10

# PROTECT FROM OVERFLOWING OF EXP
def protectedExp(arg):
	try:
		return math.exp(arg)
	except OverflowError:
		return 10000
	

# ADDING POSSIBLE FUNCTIONS, THE SECOND ARGUMENT IS HOW MANY INPUTS THE 
# FUNCTION ACCEPTS SO THE COSINE WORKS WITH 1 INPUT, ADDITION WITH 2
pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(protectedLog, 1)
pset.addPrimitive(protectedExp, 1)
pset.addPrimitive(math.cos, 1)
pset.addPrimitive(math.sin, 1)
pset.renameArguments(ARG0='x')

# BASICALLY SETTING THE UP THE FITNESS
creator.create("FitnessMin", base.Fitness, weights = (-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness = creator.FitnessMin)

# SETTING UP THE EVOLUTION, HOW DO WE HANDLE THE POPULATION AND PASSING THE 'GENES'
# MOREOVER THE TOOLBOX IS RESPONSIBLE FOR HANDLING AND SAVING THE GENERATIONS
toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset = pset, min_ = 1, max_ = 5)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset = pset)

# EVALUATION OF INDIVIDUAL
def evalSymbReg(individual):
	# TRANSFORM THE TREE INTO A CALLABLE FUNCTION
	func = toolbox.compile(expr = individual)
	
	# OUR DATA
	x = [x/10. for x in range(-10,11)]
	y = [0, -0.1629, -0.2624, -0.3129, -0.3264, -0.3125, -0.2784, -0.2289, -0.1664, -0.0909, 0, 0.1111, 0.2496, 0.4251, 0.6496, 0.9375, 1.3056, 1.7731, 2.3616, 3.0951, 4]
	
	# EVALUATE THE ERROR
	abs_err = (np.abs(func(x[i]) - y[i]) for i in range(20))
	return math.fsum(abs_err)/21,

toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize = 5)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_ = 0, max_ = 2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# THE 'MAIN' PART OF THE CODE, FROM HERE EVERYTHING IS RUN ...
def main(p_cross, p_mut, seed):
	random.seed(seed)
	
	# THE SIZE OF OUR POPULATION AND HALL OF FAMER(S) ...
	pop = toolbox.population(n = 1000)
	hof = tools.HallOfFame(1)
	hof.update(pop)
	
	# KEEP TRACK OF STATS OF THE BEST INDIVIDUAL
	fit_b = np.zeros((51, 1))
	sz_b = np.zeros((51, 1))
	gen = np.linspace(1, 50, 50)
	
	# ALGORITHM IMPLEMENATION
	for g in range(51):
		# OBTAIN HALL OF FAMER FROM THE CURRENT GENERATION
		hof.remove(0)
		hof.update(pop)
		fit_b[g] = evalSymbReg(hof[0])
		sz_b[g] = len(hof[0])
		
		# CREATE OFFSPRING FROM CURRENT POPULATION
		offspring = toolbox.select(pop, 1000)
		offspring = algorithms.varAnd(offspring, toolbox, p_cross, p_mut)
		
		# EVALUATE OFFSPRING, WITH SMALL IMPLEMENTATION TO ENSURE VALID FITNESS SCORES
		invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
		fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit
		
		# REPLACE THE POPULATION ...
		pop = offspring
	
	# SET PLOT STYLE ELEMENTS
	sns.set(style="ticks")
	
	# PLOT THE BEST FITNESS
	plt.figure(1)
	plt.plot(gen, fit_b[1:51])
	plt.xlabel('Generation')
	plt.ylabel('Fitness of best individual')
	plt.xlim([1, 50])
	plt.ylim(ymin = 0)

	# PLOT THE SIZE OF BEST FITNESS
	plt.figure(2)
	plt.plot(gen, sz_b[1:51])
	plt.xlabel('Generation')
	plt.ylabel('Size of best individual')
	plt.xlim([1, 50])
	plt.ylim(ymin = 0)
	
	plt.show()

	

if __name__ == "__main__":
	if (len(sys.argv) != 4):
		print 'please provide 3 arguments: probability crossover, probability mutation, seed'
	else:
		main(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
