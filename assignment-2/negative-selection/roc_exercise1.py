import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from pprint import pprint


file_name_neg = 'ex_1/english_r_{}.txt'
file_name_pos = 'ex_1/tagalog_r_{}.txt'

fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(1,10):
    with open(file_name_pos.format(i), 'r') as p, open(file_name_neg.format(i), 'r') as n:
        pos_scores = p.read().split(" \n")[:-1]
        neg_scores = n.read().split(" \n")[:-1]
    true_label = np.ones((len(pos_scores)))
    neg_label = np.zeros((len(neg_scores)))
    y = np.append(true_label,neg_label)
    tot_scores = pos_scores + neg_scores
    scores = np.array([float(i) for i in tot_scores])
    fpr[i], tpr[i], _ = roc_curve(y, scores)
    roc_auc[i] = auc(fpr[i], tpr[i])

plt.figure()
for i in range(1,10):
    plt.plot(fpr[i], tpr[i],lw=2, label='ROC r={} (area = {:0.2f})'.format(i, roc_auc[i]))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic curve exercise 1')
plt.legend(loc="lower right")
plt.show()