Problem Statement:
HELP International is an international humanitarian NGO that is committed to fighting poverty and providing the people of backward countries with basic amenities and relief during the time of disasters and natural calamities.
HELP International have been able to raise around $ 10 million. Now the CEO of the NGO needs to decide how to use this money strategically and effectively. So, NGO has to make decision to choose the countries that are in the direst need of aid. Hence, the project focuses on building predictive model to categorise the countries using some socio-economic and health factors that determine the overall development of the country.

Steps taken during EDA:
Null value detection
Duplicate row detection
Outlier Detection
Winsorization

Hypothesis Testing:
T-test and Correlation Analysis used

ML Modeling: 
Training was done using multiple models like K-Means, DBSCAN, GMM, Heirarchical Clustering etc. Out of which K-Means with k=3 gave the best silhoutte score and was used for final deployment.

Insights: 
1. Countries with higher income, higher export, higher import was mostly categorised as Developed Nations
2. Countries having higher Child Mortality, Higher fertility were categoried as In Dire need status.
3. The dataset is very spare due to which DBSCAN clustered all the datapoints in single cluster.
4. The size of the dataset is too small which one of the reason for DBSCAN not working properly.
5. Inflation in general does not play a major role in the clustering of the countries.

Recommandations:
1. Helping the countries economically will have a better impact on moving the country out of poverty. It will reduce the mortality rates and increase life expectancy as well.
2. Rather than representing columns like import and export as percentage of GDPP. It will be better if we give there actual value for countries respectively.
3. Increasing the size of the dataset so that training will become much reliable.

The final silhoutte score achieved is 0.46 using K-Means algorithm with K=3. 

During the deployment we have created a flask and streamlit application hosted on an ec2 machine. Users enter there feature values using streamlit UI which is then send to flask using POST method. Flask then performs scaling and prediction and returns the prediction to the user.
