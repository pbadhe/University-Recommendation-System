%%time

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.4icu.org/us/a-z/" # website that lists universities in the USA

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "table table-hover"}) # find table with university names

usa_universities = [] # list to store USA universities

for index, row in concatenated_df.iterrows(): # loop through each row of the DataFrame
    University = row["University"] # get university name from the column
    for row in table.find_all("tr"): # loop through each row of the table
        cols = row.find_all("td")
        if len(cols) > 1: # check if row contains university name
            name = cols[1].text.strip()
            if University.lower() in name.lower(): # check if entered university name matches the name in the row
                usa_universities.append(True) # add True to the list if the university is in the USA
                break
    else:
        usa_universities.append(False) # add False to the list if the university is not in the USA

# add a new column to the DataFrame indicating if the university is in the USA
concatenated_df["is_usa"] = usa_universities

# filter out non-USA universities and keep only the USA universities in the DataFrame
concatenated_df = concatenated_df[concatenated_df["is_usa"] == True]

# drop the "is_usa" column
concatenated_df = concatenated_df.drop(columns=["is_usa"])

# # save the updated DataFrame to the original CSV file
# df.to_csv("universityData_trail4.csv", index=False)

concatenated_df
