import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


langs = ['hiligaynon','middle-english','plautdietsch','xhosa']

file_name_neg = 'ex_1/english_r_{}.txt'
file_name_pos = 'ex_1/{}_r_{}.txt'

best_fpr = dict()
best_tpr = dict()
best_auc = dict()

for lang_idx in range(len(langs)):
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(1,10):
        with open(file_name_pos.format(langs[lang_idx],i), 'r') as p, open(file_name_neg.format(i), 'r') as n:
            pos_scores = p.read().split(" \n")[:-1]
            neg_scores = n.read().split(" \n")[:-1]
        true_label = np.ones((len(pos_scores)))
        neg_label = np.zeros((len(neg_scores)))
        y = np.append(true_label,neg_label)
        tot_scores = pos_scores + neg_scores
        scores = np.array([float(i) for i in tot_scores])
        fpr[i], tpr[i], _ = roc_curve(y, scores)
        roc_auc[i] = auc(fpr[i], tpr[i])
    
    best_index = np.array(list(roc_auc.values())).argmax() + 1
    print("Best r: ", best_index)
    best_fpr[lang_idx] = fpr[best_index]
    best_tpr[lang_idx] = tpr[best_index]
    best_auc[lang_idx] = roc_auc[best_index]

plt.figure()
for i in range(len(langs)):
    plt.plot(best_fpr[i], best_tpr[i],lw=2, label='ROC {} (area = {:0.2f})'.format(langs[i], best_auc[i]))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Best receiver operating characteristic curve per language')
plt.legend(loc="lower right")
plt.show()