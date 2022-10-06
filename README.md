
Here are the resulting RUC curves from the 4 models on a subset of 6 drugs.

![ruc_curves](https://user-images.githubusercontent.com/54859612/194201676-be25204b-2490-4958-8a16-6b0686b0e7e5.png)


And here are the resulting confusion matrices

![dt cm](https://user-images.githubusercontent.com/54859612/194201692-87935fc0-5f13-41ca-be99-28d248a36b70.png)
![rf cm](https://user-images.githubusercontent.com/54859612/194201702-14390712-121b-4f23-aa98-d37885186558.png)
![Knn cm](https://user-images.githubusercontent.com/54859612/194201712-92b4eac7-f391-4aed-afb5-ce9d56f81e50.png)
![svm cm](https://user-images.githubusercontent.com/54859612/194201727-2bf25556-1622-45f5-990f-7f41a8db047d.png)


As we can see from the results, it is apparent that Random Forest was the most accurate model as it consistently was able to have the highest true positive rate and the lowest false positive rate on all six RUC curves, with Decision Trees arguably the least good performing model. It also seems from the RUC curves that alcohol was the biggest challenge for the models as, for the most part, the results don't stray far from random guessing, and Cannabis the easiest to predict. It is also interesting to note that all models except RF had trouble with Heroin. Given these results, I think it is apparent that ensembles are indeed a very effective model for classifications as RF not only always got the best results, but was also very consistent, unlike SVM which sometimes got decent results and sometimes was the worst performing model. 

When looking at the results from the paper "The Five Factor Model of personality and evaluation of drug consumption risk", it is suprising to see that on their table 18 at page 34, that their best results was from using Decision Trees. However, it is important to note that, unlike me who used all 12 features for prediction, the authors of the paper only used a few of the features for prediction, which makes me suspect that perhaps they are overfitting since topics like the human brain and addiction seems far too complex for this little amount of features, which is why in my case I thought it would be best to keep all of them. I also changed the classes to binary classification, with 0 for C1 and C2 representing "Non-Users", and 1 for C3 to C6 representing "Users". 

Looking at the precision and recall, it is apparent that some of the results are worrisome, like the 0.0 precison and recall values in most of the SVM results, which I suspect could be attributed to the fact the the dataset is unbalanced.  
