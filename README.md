
Here are the resulting RUC curves from the 4 models on a subset of 6 drugs.

![ruc_curves](https://user-images.githubusercontent.com/54859612/194197741-a8bbcd87-fdde-4165-aac9-e864438b7224.png)

And here are the resulting confusion matrices

![dt cm](https://user-images.githubusercontent.com/54859612/194197851-134779eb-9d26-4b86-a4fc-0d0d1cb3a380.png)
![rf cm](https://user-images.githubusercontent.com/54859612/194197858-406c8570-e63b-4e6f-835d-553121650872.png)
![Knn cm](https://user-images.githubusercontent.com/54859612/194197794-f7ac85e7-0e5f-4d4c-9b56-bdbb75507e2c.png)
![svm cm](https://user-images.githubusercontent.com/54859612/194197812-b4f625c3-160c-4a92-b853-fd6839253d0e.png)

As we can see from the results, it is apparent that Random Forest was the most accurate model as it consistently was able to have the highest true positive rate and the lowest false positive rate on all six RUC curves, with K Nearest Neighbour arguably the second best model and Decision Trees and Support Vector machine the least good performing models. It also seems from the RUC curves that alcohol was the biggest challenge for the models as the results don't stray far from random guessing, and Cannabis the easiest to predict. It is also interesting to note that all models except RF had trouble with Heroin. Given these results, I think it is apparent that ensembles are indeed a very effective model for classifications as RF not only always got the best results, but was also very consistent, unlike SVM which sometimes got ok results and sometimes was the worst performing model. 

When looking at the results from the paper "The Five Factor Model of personality and evaluation of drug consumption risk", it is suprising to see that on their table 18 at page 34, that their best results was from using Decision Trees. However, it is important to note that, unlike me who used all 12 features for prediction, the authors of the paper only used a few of the features for prediction, which makes me suspect that perhaps they are overfitting since topics like the human brain and addiction seems far too complex for this little amount of features, which is why in my case I thought it would be best to keep all of them. I also changed the classes to binary classification, with 0 for C1 and C2, and 1 for C3 to C6. 
