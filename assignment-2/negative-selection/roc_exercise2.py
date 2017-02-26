import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from pprint import pprint

file_name_true = 'syscalls/snd-unm/snd-unm.1.labels'
file_name_pred = 'syscalls/snd-unm/10/scores/snd-unm.1_r_{}.score'

fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(1,10):
    with open(file_name_true.format(i), 'r') as true_file, open(file_name_pred.format(i), 'r') as pred_file:
		true = np.array(map(float, true_file.read().splitlines()[:99]))
		pred = np.array(map(float, pred_file.read().splitlines()[:99]))
		pred = pred/float(max(pred))
		fpr[i], tpr[i], _ = roc_curve(true, pred)
		roc_auc[i] = auc(fpr[i], tpr[i])

plt.figure()
for i in range(1,10):
    plt.plot(fpr[i], tpr[i],lw=2, label='ROC r={} (area = {:0.2f})'.format(i, roc_auc[i]))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic curve exercise 2 unm 1')
plt.legend(loc="lower right")
plt.show()
