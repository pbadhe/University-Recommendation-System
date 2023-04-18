import math
import numpy as np
import pandas as pd

def adjustGREmarks(greMarks, VorQ):
    gre_score_conversion = pd.read_csv("data/score.csv")
    if not isinstance(greMarks, int) or np.isnan(greMarks):
        return 151 if VorQ == 1 else 157 # NaN values imputed with averages 
    if greMarks%10 != 0 and greMarks>199:
        greMarks = int(math.ceil(greMarks / 10.0)) * 10
    if greMarks>=200 and greMarks<=800:
        return gre_score_conversion[gre_score_conversion["old"] == greMarks].values[0][VorQ]
    #At this point, all processing is done, scrap values will be imputed with average gre marks.
    if greMarks < 130 or greMarks> 170:
        return 151 if VorQ == 1 else 157
    else: return greMarks

def getUwU(x):
  if not isinstance(x, float) or math.isnan(x): 
    return 3.0 #Average 
  if 0.0 <= x <= 6.0:
    return round(round(x, 1)*2)/2.0
  else:
    return 3.0

def handleCGPA(cgpa):
    convert10to4 = {10.0 : 4, 9.9: 3.97, 9.8: 3.94, 9.7: 3.9, 9.6: 3.87, 9.5: 3.84, 9.4: 3.81, 9.3: 3.78, 9.2: 3.74, 9.1: 3.71, 9.0: 3.68, 8.9: 3.65, 8.8: 3.62, 8.7: 3.58, 8.6: 3.55, 8.5: 3.52, 8.4: 3.49, 8.3: 3.46, 8.2: 3.42, 8.1: 3.39, 8.0: 3.36, 7.9: 3.33, 7.8: 3.3, 7.7: 3.26, 7.6: 3.23, 7.5: 3.2, 7.4: 3.17, 7.3: 3.14, 7.2: 3.1, 7.1: 3.07, 7.0: 3.04, 6.9: 3, 6.8: 2.95, 6.7: 2.9, 6.6: 2.85, 6.5: 2.8, 6.4: 2.75, 6.3: 2.7, 6.2: 2.65, 6.1: 2.6, 6.0 : 2.55, 5.9: 2.5, 5.8: 2.45, 5.7: 2.4, 5.6: 2.35, 5.5: 2.3, 5.4: 2.25, 5.3: 2.2, 5.2: 2.15, 5.1: 2.1, 5.0  : 2.05, 4.9: 2, 4.8: 1.94, 4.7: 1.88, 4.6: 1.82, 4.5: 1.76, 4.4: 1.71, 4.3: 1.65, 4.2: 1.59, 4.1: 1.53}
    cgpa = float(cgpa)
    if cgpa <= 100.0 and cgpa > 10.0:
        cgpa = (cgpa/9.5) if cgpa <= 95.0 else 10.0

    cgpa = round(float(cgpa), 1)
    if cgpa > 4.0 and cgpa <= 10.0 :
        cgpa = convert10to4[cgpa]
    return cgpa

def ielts_to_toefl(ielts_score):
    ielts_to_toefl_table = {
        9: 118,
        8.5: 115,
        8: 110,
        7.5: 102,
        7: 94,
        6.5: 79,
        6: 60,
        5.5: 46,
        5: 35,
        4.5: 23,
        4: 12,
        3.5: 0,
        3: 0
    }
    return ielts_to_toefl_table.get(ielts_score, 0)