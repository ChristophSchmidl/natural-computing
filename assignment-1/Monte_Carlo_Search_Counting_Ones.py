
# coding: utf-8

# In[8]:

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

def generate_random_bit_array(length):
    return np.random.randint(2, size=(length,))

def counting_ones(arr):
    return np.sum(arr)

def binary_monte_carlo(objective_function, array_length, evaluations):
    print('Performing binary monte carlo search...')
    
    # Generate random bitarray of length 'bitarray_length'
    best_bitarray = generate_random_bit_array(array_length)
    # Get the fitness of the current solution
    best_fitness = objective_function(best_bitarray)
    fitness_history = [best_fitness]
    
    for x in range(0, evaluations):
        tmp_best_bitarray = generate_random_bit_array(array_length)
        tmp_best_fitness = objective_function(tmp_best_bitarray)
        
        if tmp_best_fitness >= best_fitness:
            best_bitarray = tmp_best_bitarray
            best_fitness = tmp_best_fitness
        
        fitness_history.append(best_fitness)
        
    axes = plt.gca()
    axes.set_xlim([0,evaluations])
    axes.set_ylim([0,array_length])    
    plt.plot(fitness_history)
    plt.xlabel('evaluations')
    plt.ylabel('fitness')
    plt.title('Monte-Carlo Counting Ones Problem')

    plt.show()
    return [best_bitarray, best_fitness]
    
result = binary_monte_carlo(counting_ones, 100, 1500)

print("Best bit sequence: " + str(result[0]))
print("Best fitness: " + str(result[1]))


# In[ ]:



