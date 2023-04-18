# Pass VorQ as 1 for verbal, 2 for Quant
# Run cell only once. Not more, else you gonna fuq up :D 
import math
def adjustGREmarks(greMarks, VorQ):
  if not isinstance(greMarks, int):
    return greMarks  # Do you want NaN values to be imputed with averages? 
  if greMarks%10 != 0 and greMarks>199:
    greMarks = int(math.ceil(greMarks / 10.0)) * 10
  if greMarks>=200 and greMarks<=800:
    return gre_score_conversion[gre_score_conversion["old"] == greMarks].values[0][VorQ]
  #At this point all processing is done, scrap values will be imputed with average gre marks.
  if greMarks < 130 or greMarks> 170:
    return 151 if VorQ == 1 else 157
  else: return greMarks

concatenated_df['GRE_V'] = concatenated_df['GRE_V'].astype('Int32').apply(lambda x: adjustGREmarks(x, 1))
concatenated_df['GRE_Q'] = concatenated_df['GRE_Q'].astype('Int32').apply(lambda x: adjustGREmarks(x, 2))

list(zip(concatenated_df['GRE_V'].value_counts().index.tolist(), concatenated_df['GRE_V'].value_counts().tolist()))

def getUwU(x):
  if not isinstance(x, float) or math.isnan(x): #Math.isnan() ahe but te kadhun taku apan as Null udavto ahe apan before processing the marks
    return 3.0 #Average for Indians :)
  if 0.0 <= x <= 6.0:
    return round(round(x, 1)*2)/2.0
  else:
    return 3.0

concatenated_df['GRE_AWA'] = concatenated_df['GRE_AWA'].astype(float).apply(lambda x: getUwU(x))
list(zip(concatenated_df['GRE_AWA'].value_counts().index.tolist(), concatenated_df['GRE_AWA'].value_counts().tolist()))