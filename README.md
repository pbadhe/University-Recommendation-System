# University Recommendation System using Weighted KNN
A quick recommendation system for international MS students 

This project aims to develop a recommendation system for university selection based on the Weighted K-Nearest Neighbors (KNN) algorithm. By analyzing various factors and historical data, we seek to provide personalized recommendations to students looking for the most suitable universities based on their preferences and academic profile. The recommendation system utilizes machine learning techniques and the weighted KNN algorithm to generate accurate and relevant recommendations.


## Table of Contents

- [Introduction](https://github.com/SarthakChawathe/University-Recommendation-System/blob/main/README.md#introduction)
- [Usage](https://github.com/SarthakChawathe/University-Recommendation-System/blob/main/README.md#introduction)
- [Data](https://github.com/SarthakChawathe/University-Recommendation-System/blob/main/README.md#data)
- [Model Training](https://github.com/SarthakChawathe/University-Recommendation-System/blob/main/README.md#model-training)
- [Evaluation](https://github.com/SarthakChawathe/University-Recommendation-System/blob/main/README.md#evaluation)




# Introduction
Choosing the right university is a critical decision for students, considering factors such as location, academic programs, campus facilities, reputation, and more. This project focuses on building a recommendation system that assists students in making informed choices by leveraging historical data and the weighted KNN algorithm.

The recommendation system considers various input parameters, such as student preferences (e.g., desired location, program of interest, campus facilities), academic performance, and historical data on universities (e.g., rankings, acceptance rates, alumni feedback). By calculating weighted distances between the student's profile and universities, the system identifies the most similar institutions and provides recommendations accordingly.

# Usage
1) Prepare the data: Ensure that the dataset containing university profiles and student preferences is available in a suitable format.
2) Train the recommendation model: Use the provided scripts to train the recommendation model using the available data. 
3) Generate recommendations: After training the model, you can utilize it to generate personalized recommendations for a given student. Provide the student's profile and preferences as input to the model, and it will return a list of recommended universities ranked by their similarity to the student's profile.
4) Evaluate the model: Assess the performance of the recommendation model by comparing its recommendations against actual student choices and feedback. Further details on evaluation can be found in the Evaluation section.

# Data
The data used in this project consists of university profiles, student preferences, and historical information related to universities and student choices. The dataset should contain relevant information such as university attributes (e.g., location, programs offered, facilities), student profiles (e.g., academic performance, preferred location, program of interest), and feedback or choices made by previous students.

Please ensure that the data is formatted properly and includes the necessary features for training the recommendation model. For guidance on data preparation, refer to the documentation provided in the repository.

# Model Training
The model training process involves the following steps:

1) Data preprocessing: Prepare the university and student preference dataset by cleaning the data, handling missing values, and transforming features as required.
2) Feature engineering: Extract relevant features from the dataset that can contribute to the recommendation process. This step may involve feature selection, dimensionality reduction, or generating new features based on domain knowledge.
3) Model selection: Choose the Weighted KNN algorithm as the recommendation model. Weighted KNN takes into account the importance of different features when calculating distances between data points.
4) Model training: Split the dataset into training and validation sets, and train the recommendation model using the Weighted KNN algorithm. Optimize the model parameters to improve performance.
5) Model evaluation: Assess the performance of the trained recommendation model using appropriate evaluation metrics. Evaluate the model's accuracy, precision, recall, or other suitable metrics based on the nature of the recommendation task.

Refer to the code and documentation provided in the repository for detailed instructions on training the model.

# Evaluation
To evaluate the performance of the recommendation model, compare the generated recommendations against actual student choices and feedback. Measure the accuracy of the recommendations and gather feedback from users to assess the system's effectiveness.

Additionally, you can employ evaluation techniques such as cross-validation or holdout evaluation to estimate the model's performance on unseen data and detect potential overfitting. Continuous evaluation and feedback from users will help improve the recommendation system over time.


# Link to final dashboard

Link : http://pbadhe.pythonanywhere.com/
