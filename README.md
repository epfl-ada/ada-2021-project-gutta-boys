
# An Investigation of the Mood in the Media Across Time and Subsamples

## Abstract
In this project, we have investigated how the mood in the media and the debate changes over time and subsamples. The motivation for to project was to understand the general trends in the mood. For example, does the temper get better towards the weekend, or do we love Mondays deep inside? Is the mood better in the summer than in the winter? In addition, we have done analysis on the sentiment across subsamples of different media outlets and professions. 

Through the project we have examined these questions by doing a sentiment analysis on the Quotebank dataset from 2015 to 2020. The sentiment is measured using the compound score from the Vader Lexicon (NLTK library) and the subjectivity scores from the TextBlob library. 

## Research questions
The research questions we started out with was all under the umbrella 
* “How does the mood in the media differ across time and subsamples?”

More specifically, we wanted to investigate the following:
•	Are there any differences in mood based on weekdays, weeks, or months?
•	Are there any differences in the mood across media outlets?
•	Do any subsamples differ from the general trends, for example, politicians or men/women?

## Key insight
-	There are no significant variations or trends in the mood in media quotations throughout the weekdays or months.
-	The mood in the media became significantly more negative in the first phase of the COVID-19 pandemic.
-	The mood and subjectivity across media outlets vary significantly. When subsampling the outlets based on category, clusters appear. Sports newspapers and celebrity magazines tend to be more positive and more subjective than daily newspapers.
-	The mood in the quotations said by men and women is very similar, but women are slightly more positive.
-	Quotations spoken by politicians are on average more negative than the average quotation in the data set.

## Additional datasets
To complete our project, we have used the “Wikidata metadata about speakers” dataset provided by the course. The motivation for this was to be able to study subsamples of the data.
The dataset was primarily used for two things:
1.	Extracting quotes where the most likely speaker is a politician
2.	Separating quotes spoken by men and women.
We used functions that matched politicians from the Wikidata dataset to quotes from the Quotebank data to process the additional dataset. We were considering appending binary values for women/man and politician/not-politician to the original dataset but found this to be too computationally expensive. We decided to rather use the functions as we go and analysed subsamples. To match the quotes from Quotebank to the desired attribute, we used the speaker attribute in the Quotebank dataset. More information about the functions can be found in the notebook.

## Methods
The main methods used in this project are:
•	Hypothesis testing, in particular paired t-tests and Welch's t-test
•   To test the significance of differences in mood
•	Sentiment analysis by using the NLTK library and TextBlob library for Python
•	The sentiment.vader module was used to quantify the sentiment (positive/negative) in quotes
•	The TextBlob library was used to quantify the subjectivity in quotes
The methods and their mathematical outlines are described in more detail in the bottom of the notebook delivery.

## Proposed timeline
The timeline for the project stretched over three milestones from 22 September to 17 December. 

__Milestone 1 (22.09 – 08.10)__
-	Made individual proposals for the project

__Milestone 2 (08.10-12.11)__
 initial analyses and data handling pipelines
-	Decided project and research questions 
-	Started initial analyses and made data handling pipelines

__Milestone 3 (12.11-17.12)__

__Week 1 + 2 (12/11 - 21/11)__:
-	Reviewing feedback from milestone 2

__Week 3 +4 (22/11 - 05/12)__:
-	Loaded the datasets. Added the necessary attributes for the different tasks
-	Initial sentiment analysis for time trend and subsamples
-	Launching the Jekyll webpage

__Week 5 (06/11 - 12/11)__:
-	Completed sentiment analysis for time trend
-	Completed sentiment analysis for media outlets
-	Finished draft for data story, including drafts for plots

__Week 6 (13/11 - 17/11)__:
-	Completed sentiment analysis for subsamples of men and women and politicians.
-	Spell-checking and other polishing of the data story finished. 
-	Putting together the final and complete notebook for the project
-	Updating Readme
-	Celebrating the completion of the data story and its tremendous visualizations and exciting insights.

## Organization within the team:
Each member had a main responsibility for the project. However, all members were involved in the processes by taking part in the decision-making and discussions, ensuring the best possible collaboration. The group have met weekly through the whole semester and more frequently in busy periods.
Name: Responsibilities
__Asbjørn__: General processing and analysis in early phases. Focus on the media outlet analysis. 
__Benjamin__: Analysing the time trend of the dataset. Responsible for defining the statistical methods and ensuring uniform code quality. 
__Marcus__: Processing and analysis involving the Wikidata set, i.e., men/women and politicians. 
__Sigurd__: Written part of the final data story and visualizations, due 10 December.
