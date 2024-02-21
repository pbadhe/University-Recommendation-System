# University Recommendation System (Weighted KNN)

A quick recommendation system for international graduate students in the US to select universities based on Weighted K-Nearest Neighbors (KNN) algorithm.
By scraping latest graduate data from active websites like YMGrad, TheGradCafe and Edulix, this tool provides personalized recommendations to students looking for the most suitable universities based on their preferences and academic profile. 

## Installation

1. Clone the repository. In the working environment, run the command ```pip install -r requirements.txt``` from the [src](https://github.com/pbadhe/University-Recommendation-System/tree/main/src) folder to install the required packages.
2. Run the flask server by executing ```python recommend.py``` to host the application.
3. Click the link in the terminal to start using the application.

## Usage
On the UI, input your details for the fields shown below and let the custom Weighted KNN algorithm do the magic for you. Sample inputs and output results are shown below.

![image](https://github.com/pbadhe/CureNsure/assets/44113251/6bad2f3c-9de3-4a3f-abb3-8f4ffea01496)
![image](https://github.com/pbadhe/CureNsure/assets/44113251/934e3458-dda6-47a1-87f1-a25e0f4beddd)

## Data
- The dataset contains information on the admission decisions made by universities for various programs to the applicants which the app uses for implementing our university recommendation system, most accurately catered for Computer Science students. 
- The data was obtained by web scraping data from the [YM Grad website](https://www.ymgrad.com/admits_rejects/), which provides information on latest admits and rejects. The [prepared dataset](https://github.com/pbadhe/University-Recommendation-System/blob/main/src/data/Prepared%20MS%20University%20Data.csv) also contains records from [TheGradCafe](https://www.thegradcafe.com/) and [Edulix](https://www.edulix.com) (from Kaggle).
- The original data is a heterogeneous mix of 3 sources which after preprocessing, consists of 8 columns each providing a specific piece of
information related to the admission decision as discussed below.

#### Features
1. ’Major’ column specifies the program that the applicant applied to.
2. ’University’ column specifies which university the applicant got admits from. 
3. ’Months’ column denotes the professional work experience of the applying candidate.
3. ’Papers’ column provides information on the research papers or publications that the applicant has authored or co-authored. 
3. ’CGPA’ column indicates the undergrad score of the applicant on a scale of 4. 
3. ’GRE Verbal,’ ’GRE Quant,’ and ’GRE AWA’ columns refer to the applicant’s scores in the GRE Verbal, GRE Quant, and GRE Analytical Writing Assessment sections respectively.
3. ’TOEFL Scores’ column provides information on the applicant’s scores in the TOEFL exam. The ’IELTS’ scores are converted into TOEFL Score based on the official conversion method found on TOEFL website. 
3. To enhance the recommendations, we have taken University Rankings from website the [US NEWS Rankings](https://www.usnews.com/education/best-global-universities/united-states/computer-science) website


## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change. Also, make sure to add tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
