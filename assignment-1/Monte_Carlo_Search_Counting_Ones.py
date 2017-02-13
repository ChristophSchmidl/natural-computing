
# coding: utf-8

# In[79]:

get_ipython().magic('matplotlib inline')
from bitarray import bitarray
import matplotlib.pyplot as plt

def counting_ones(bitarray_instance):
    return bitarray_instance.count(True)

def binary_monte_carlo(objective_function, bitarray_length, evaluations):
    print('Performing binary monte carlo search...')
    
    # Generate random bitarray of length 'bitarray_length'
    best_bitarray = bitarray(bitarray_length)
    # Get the fitness of the current solution
    best_fitness = objective_function(best_bitarray)
    fitness_history = [best_fitness]
    
    for x in range(0, evaluations):
        tmp_best_bitarray = bitarray(bitarray_length)
        tmp_best_fitness = objective_function(tmp_best_bitarray)
        
        if tmp_best_fitness >= best_fitness:
            best_bitarray = tmp_best_bitarray
            best_fitness = tmp_best_fitness
        
        fitness_history.append(best_fitness)
        
    axes = plt.gca()
    axes.set_xlim([0,evaluations])
    axes.set_ylim([0,bitarray_length])    
    plt.plot(fitness_history)
    plt.xlabel('evaluations')
    plt.ylabel('fitness')
    plt.title('Monte-Carlo Counting Ones Problem')

    plt.show()
    return [best_bitarray, best_fitness]
    
result = binary_monte_carlo(counting_ones, 100, 10)

print("Best bit sequence: " + str(result[0]))
print("Best fitness: " + str(result[1]))


# In[ ]:



