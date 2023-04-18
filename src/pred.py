import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

def getWeights():
    return {"Computer Science" : { "CGPA": 0.3,
		"GRE_V": 0.1,
		"GRE_Q": 0.2,
		"GRE_AWA": 0.05,
		"toeflScore": 0.15,
		"industryExp": 0.1,
		"researchExp": 0.1},

		"MIS" : { "CGPA": 0.3,
		"GRE_V": 0.1,
		"GRE_Q": 0.2,
		"GRE_AWA": 0.05,
		"toeflScore": 0.15,
		"industryExp": 0.1,
		"researchExp": 0.1} 
	}

def validate(y_test, results):
    if len(y_test) != len(results):
        return "Length of outputs is not equal"
    correct = 0.0
    for i, val in enumerate(y_test):
        if val in results[i]:
            correct += 1
    score = correct/float(len(y_test))
    print("Validation Score: ",score)
    return score

def filterTopUniversities(x, major):
    top_universities = {'Computer Science' : 100, 'MIS' : 50}
    top_accepted_df = x.copy()
    univ_counts = top_accepted_df['University'].value_counts()
    n = top_universities[major]
    top_univs = univ_counts[univ_counts > n].index
    top_accepted_df = top_accepted_df[top_accepted_df['University'].isin(top_univs)]
    return top_accepted_df

def getUniversities(top_accepted_df, major, cgpa, greV, greQ, greAWA, toefl, industryExp, researchExp):
    scaler = MinMaxScaler()
    scaled_df = scaler.fit_transform(top_accepted_df.drop(["Major", "University"], axis=1))
    scaled_df = pd.DataFrame(scaled_df, columns=["researchExp","industryExp","toeflScore","GRE_V","GRE_Q","GRE_AWA","CGPA"])
    copied_top = top_accepted_df.copy()
    copied_top = copied_top.reset_index(drop=True)
    scaled_df["Major"] = copied_top.Major
    scaled_df["University"] = copied_top.University
    scaled_df = scaled_df.reset_index(drop=True)
    
    test_point = pd.DataFrame({"researchExp": researchExp, "industryExp": industryExp, "toeflScore": toefl, "GRE_V": greV, "GRE_Q": greQ, "GRE_AWA": greAWA, "CGPA": cgpa}, index=[0])
    test_point = scaler.transform(test_point)
    test_data = pd.DataFrame(test_point, columns=["researchExp","industryExp","toeflScore","GRE_V","GRE_Q","GRE_AWA","CGPA"])
    weights = getWeights()
    df_filtered = scaled_df[scaled_df['Major'] == major]
    df_filtered = filterTopUniversities(df_filtered, major)
    X = df_filtered.drop(["Major", "University"], axis=1)
    y = df_filtered['University']
    for feature in weights[major]:
        X[feature] = X[feature] * weights[major][feature]
        
    for feature in weights[major]:
        test_data[feature] = test_data[feature] * weights[major][feature]
    
    knn = KNeighborsClassifier(n_neighbors=15, weights="distance")
    knn.fit(X, df_filtered['University'])
    
    _, indices = knn.kneighbors(test_data, n_neighbors=15)
    
    neighbor_universities = [y.iloc[index] for index in indices]
    return set(list(neighbor_universities)[0])