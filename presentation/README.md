# Notes regarding the paper "Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks"


## 1 Introduction



## 2 Weight Normalization

Equation 1:

![Equation1](img/2_weight_normalization/eq_1.PNG)

Equation 2:

![Equation2](img/2_weight_normalization/eq_2.PNG)


### 2.1 Gradients

Equation 3, left side:

![Equation3_1](img/2_1_gradients/eq_3_1.PNG)

Equation 3, right side:

![Equation3_2](img/2_1_gradients/eq_3_2.PNG)



Equation 4, left side:

![Equation4_1](img/2_1_gradients/eq_4_1.PNG)

Equation 4, right side:

![Equation4_2](img/2_1_gradients/eq_4_2.PNG)


### 2.2 Relation to batch normalization

Unlisted equation regarding batch normalization:

![Equation_unlisted](img/2_2_relation_to_batch_normalization/eq_unlisted.PNG)


## 3 Data-Dependent Initialization of Parameters


Equation 5, left side:

![Equation5_1](img/3_data-dependent_initialization_of_parameters/eq_5_1.PNG)

Equation 5, right side:

![Equation5_2](img/3_data-dependent_initialization_of_parameters/eq_5_2.PNG)


Equation 6, left side:

![Equation6_1](img/3_data-dependent_initialization_of_parameters/eq_6_1.PNG)

Equation 5, right side:

![Equation6_2](img/3_data-dependent_initialization_of_parameters/eq_6_2.PNG)


## 4 Mean-only Batch Normalization





## 5 Experiments



### 5.1 Supervised Classification: CIFAR-10




### 5.2 Generative Modelling: Convolutional VAE






### 5.3 Generative Modelling: DRAW





### 5.4 Reinforcement Learning: DQN




## 6 Conclusion

