#imports for the fucntion
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
from plot_confusion_matrix import plot_confusion_matrix


"""
    This function prints Accuracy and AUC results for test subset. It also plot the confusion matrix for each model.
   
    Return: AUC(%),Accuracy(%), Confusion Matrix 
    
"""


def model_to_results(model_to_test):
    
    #read the results from model test subset
    filename='intermediary_data/' + model_to_test+'_results.csv'
    results=pd.read_csv(filename)
    
    if model_to_test=='irrelevant_check':
        #calculate metrics (Accuracy and AUC)
        AUC = roc_auc_score(results['class_true'],results['class_prob'])
        ACC = accuracy_score(results['class_true'],results['class_pred'])
        print('Irrelevant Check Results:')
        print('AUC:',100*round(AUC,4),'%')
        print('Accuracy:',100*round(ACC,4),'%')
        
        #plot confusion matrix
        confmat=confusion_matrix(results['class_pred'], results['class_true'],labels=[0,1])
        target_names = ['relevant','irrelevant']
        fig_1=plt.figure(1)
        plot_confusion_matrix(confmat, classes=target_names,
                         title='Confusion matrix - irrelevant check')
        plt.show()
        
    elif model_to_test=='multitask':
        #calculate metrics (Accuracy and AUC) for street_width
        AUC = roc_auc_score(results['street_width_class_true'],results['street_width_prob'])
        ACC = accuracy_score(results['street_width_class_true'],results['street_width_class'])
        print('Street_width Results(Multitask Model):')
        print('AUC:',100*round(AUC,4),'%')
        print('Accuracy:',100*round(ACC,4),'%')
        
        #calculate metrics (Accuracy and AUC) for pavement type
        probs=pd.concat([results['pavement_type_prob_alcatrao'],results['pavement_type_prob_terra_batida'],results['pavement_type_prob_paralelo']], axis=1)
        AUC = roc_auc_score(results['pavement_type_class_true'],np.array(probs), multi_class='ovr')
        ACC = accuracy_score(results['pavement_type_class_true'],results['pavement_type_class'])
        print('Pavement Type Results(Multitask Model):')
        print('AUC:',100*round(AUC,4),'%')
        print('Accuracy:',100*round(ACC,4),'%')
        
        #plot confusion matrix for street width
        confmat=confusion_matrix(results['street_width_class'], results['street_width_class_true'],labels=[0,1])
        target_names = ['Single Car','Doble Car or more']
        fig_1=plt.figure(1)
        plot_confusion_matrix(confmat, classes=target_names,
        title='Confusion matrix - Street Width')
        
        #plot confusion matrix for pavement type
        confmat=confusion_matrix(results['street_width_class'], results['street_width_class_true'],labels=[0,1,2])
        target_names = ['Alcatrão','Terra Batida', 'Paralelo']
        fig_2=plt.figure(2)
        plot_confusion_matrix(confmat, classes=target_names,
        title='Confusion matrix - Pavement Type')
        plt.show()
        
    elif model_to_test=='quality':
        #calculate metrics (Accuracy and AUC)
        AUC = roc_auc_score(results['class_true'],results['class_prob'])
        ACC = accuracy_score(results['class_true'],results['class_pred'])
        print('Irrelevant Check Results:')
        print('AUC:',100*round(AUC,4),'%')
        print('Accuracy:',100*round(ACC,4),'%')
        
        #plot confusion matrix
        confmat=confusion_matrix(results['class_pred'], results['class_true'],labels=[0,1])
        target_names = ['Low','High']
        fig_1=plt.figure(1)
        plot_confusion_matrix(confmat, classes=target_names,
                         title='Confusion matrix - Quality of road')
        plt.show()
            
        
