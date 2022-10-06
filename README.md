
Here are the resulting RUC curves from the 4 models on a subset of 6 drugs.

![Here are the RUC curves](https://user-images.githubusercontent.com/54859612/193950370-db7624c1-5835-4fca-94f6-9cc8bc0b091e.png)

And here are the resulting confusion matrices
![dt cm](https://user-images.githubusercontent.com/54859612/193950919-6698faab-eca9-4af7-bc41-3b87b3d6b45e.png)
![Knn cm](https://user-images.githubusercontent.com/54859612/193950928-020f724f-5d75-433f-b43b-ca4a53c1625d.png)
![rf cm](https://user-images.githubusercontent.com/54859612/193950931-b28b1f87-ed9e-42b7-8b51-0c084b33a7c2.png)
![svm cm](https://user-images.githubusercontent.com/54859612/193950933-6c40f08b-015d-4429-8b23-af0c8afc8aa9.png)

As we can see from the results, it is apparent that Random Forest was the most accurate model as it consistently was able to have the highest true positive rate and the lowest false positive rate on all six RUC curves, with K Nearest Neighbour arguably the second best model and Decision Trees and Support Vector machine the least good performing models. It also seems from the RUC curves that alcohol was the biggest challenge for the models as the results don't stray far from random guessing, and Cannabis the easiest to predict. It is also interesting to note that all models except RF had trouble with Heroin. Given these results, I think it is apparent that ensembles are indeed a very effective model for classifications as RF not only always got the best results, but was also very consistent, unlike SVM which sometimes got ok results and sometimes was the worst performing model. 

When looking at the results from the paper "The Five Factor Model of personality and evaluation of drug consumption risk", it is suprising to see that on their table 18 at page 34, that their best results was from using Decision Trees. However, it is important to note that, unlike me who used all 12 features for prediction, the authors of the paper only used a few of the features for prediction, which makes me suspect that perhaps they are overfitting since topics like the human brain and addiction seems far too complex for this little amount of features, which is why in my case I thought it would be best to keep all of them. I also changed the classes to binary classification, with 0 for C1 and C2, and 1 for C3 to C6. 
