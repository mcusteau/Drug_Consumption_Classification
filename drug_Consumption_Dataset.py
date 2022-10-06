import pandas as pd
import numpy as np
from sklearn import tree, ensemble, svm, neighbors, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
respondents = pd.read_csv("drug_consumption.csv")

feature_list = [
"ID",
"Age",
"Gender",
"Education",
"Country",
"Ethnicity",
"Nscore",
"Escore",
"Oscore",
"Ascore",
"Cscore",
"Impulsive",
"SS",
"Alcohol",
"Amphet",
"Amyl",
"Benzos",
"Caff",
"Cannabis",
"Choc",
"Coke",
"Crack",
"Ecstasy",
"Heroin",
"Ketamine",
"Legalh",
"LSD",
"Meth",
"Mushrooms",
"Nicotine",
"Semer",
"VSA"
]
drugs_list = ["Alcohol",
"Amphet",
"Amyl",
"Benzos",
"Caff",
"Cannabis",
"Choc",
"Coke",
"Crack",
"Ecstasy",
"Heroin",
"Ketamine",
"Legalh",
"LSD",
"Meth",
"Mushrooms",
"Nicotine",
"Semer",
"VSA"]

# create features
respondents.columns = feature_list

# create labels
drugs = respondents[drugs_list].copy()
respondents = respondents.drop(drugs_list, axis=1)

# create label values function 
def BinaryLabel(df, column):
	for i in df[column].index:
		if(df[column][i]=="CL0" or df[column][i]=="CL1"):
			df[column][i] = 0
		else:
			df[column][i] = 1


# create and plot confusion matrix
def createConfusionMatrix(test_col, pred_col, drug_name, col_num, axes):
	cm = metrics.confusion_matrix(test_col.values.tolist(), pred_col)
	disp = metrics.ConfusionMatrixDisplay(cm)
	disp.plot(ax=axes[col_num], xticks_rotation=45)
	disp.ax_.set_title(drug_name)
	disp.im_.colorbar.remove()
	disp.ax_.set_xlabel('predicted labels')


# label data with value 1 for user and value 0 for non-user
for drug in drugs:
	BinaryLabel(drugs,drug)

# use holdout method of 33% for creating training and testing set
respondents_train, respondents_test, drugs_train, drugs_test = train_test_split(respondents, drugs, test_size = 0.33)

# create a model specifically for trainning set
def create_train_model(clf, train_set, train_labels, **kwargs):
	model = clf(**kwargs)
	model = model.fit(train_set, train_labels)
	return model

# training and prediction function that creates a new model for each drug and trains on it individually
def train_predict(clf, model_name, drug_subset, confusionMatrix=True, train_set=respondents_train, train_labels=drugs_train, test_set=respondents_test, test_labels=drugs_test, **kwargs):
	predictions = []
	models = []
	print("\nResults for "+model_name+"\n")
	for individual_drug in drug_subset:
		# train model for specific drug
		individual_model = create_train_model(clf, train_set, train_labels[individual_drug].astype('int'), **kwargs)
		# predict on test set
		drug_pred = individual_model.predict(test_set)
		print(individual_drug)
		print("precision:", metrics.precision_score(test_labels[individual_drug].values.tolist(), drug_pred))
		print("recall:", metrics.recall_score(test_labels[individual_drug].values.tolist(), drug_pred))
		print()
		predictions.append(drug_pred)
		models.append(individual_model)
	# create confusion matrix
	if(confusionMatrix):
		f, axes = plt.subplots(1, 6, figsize=(20, 5), sharey='row')
		plt.suptitle(model_name)
		for col in range(len(drug_subset)):
			createConfusionMatrix(test_labels[drug_subset[col]], predictions[col], drug_subset[col], col, axes)	
	
	return predictions, models

# plot roc curve based on given values
def plotROC(i, j, false_positive_rate, true_positive_rate, area_under_curve, drugs_subset, legend_names, axes):
	if(i>=3):
		row=1
	else:
		row=0
	col=i%3

	axes[row, col].set_title(drugs_subset[i])
	axes[row, col].axis('square')
	axes[row, col].set_xlabel("false positive rate")
	axes[row, col].set_ylabel("true positive rate")
	axes[row, col].plot(false_positive_rate, true_positive_rate, label=legend_names[j]+", area_under_curve="+str(area_under_curve))
	axes[row, col].legend(loc=4)

# calculate false positive rate, true positive rate and area under the curve
def createROC(models, legend_names, drugs_subset, train_labels=respondents_test, test_labels=drugs_test):
	fig, axes = plt.subplots(2, 3, figsize=(17, 17), sharex='col', sharey='row')
	for i in range(len(drugs_subset)):
		for j in range(len(models)):
			# calculate probability estimates for class
			y_pred_proba = models[j][i].predict_proba(train_labels)[::,1]
			# calculate false positive rate, true positive rate and area under the curve
			false_positive_rate, true_positive_rate, _ = metrics.roc_curve(test_labels[drugs_subset[i]].values.tolist(), y_pred_proba)
			area_under_curve = metrics.roc_auc_score(test_labels[drugs_subset[i]].values.tolist(), y_pred_proba)
			# plot roc graph
			plotROC(i, j, false_positive_rate, true_positive_rate, area_under_curve, drugs_subset, legend_names, axes)
	
		


# Chose our subset of 6 drugs 
drugs_subset = ["Alcohol", "Cannabis", "Coke", "Crack", "Heroin", "Meth"]

# create our 4 types of models
dt_predictions, dt_models = train_predict(tree.DecisionTreeClassifier, "Decision Tree Classifier", drugs_subset)

rf_predictions, rf_models = train_predict(ensemble.RandomForestClassifier, "Random Forest Classifier", drugs_subset)

svm_predictions, svm_models = train_predict(svm.SVC, "Support Vector Machine", drugs_subset, probability=True)

knn_predictions, knn_models = train_predict(neighbors.KNeighborsClassifier, "K Nearest Neighbors Classifier", drugs_subset)

# create ROC curve
createROC([dt_models, rf_models, svm_models, knn_models], ["DT", "RF", "SVM", "KNN"], drugs_subset)

plt.show()