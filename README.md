
# An investigation of the mood in media across time and subsamples
## Abstract
In this project, we want to investigate how the mood in the media and the debate changes over time. We want to understand the general trends in the mood. For example, does the temper get better towards the weekend, or do we love Mondays deep inside? Is the mood better in the summer than in the winter?

These are exciting questions that we talk about in everyday life. The media sets the agenda for discussion and essentially decides which cases reach the general public’s mind. It would be interesting to see how much negativity and positivity reaches the public, and how this varies across media outlets. Additionally, it would be interesting to see how the mood changes across a subsample of speakers, for example, politicians. Are politicians more negative or positive than others? These questions will help us tell the story about the mood in the media.

## Research Questions

All our research questions are under the umbrella 

*“How is the mood in the media?”* 

More specifically, we want to investigate the following:
* Do we see any general trends in the mood?
* Are there any differences in mood based on weekdays, weeks, or months?
* Do any subsamples differ from the general trends, for example, politicians or men/women?
* Are there any differences in the mood across media outlets?


## Proposed additional datasets
To complete our project, we want to use the *“Wikidata metadata about speakers”* dataset provided by the course. The motivation for this is to be able to study subsamples of the data. 

We will primarily use it for two things:
 1) Extracting quotes where the most likely speaker is a politician
 2) Separating quotes spoken by men and women.

We are using functions that match politicians from the Wikidata dataset to quotes from the Quotebank data to process the additional dataset. We were considering appending binary values for women/man and politician/not-politician to the original dataset but found this to be too computationally expensive. We decided to rather use the functions as we go and analyze subsamples. To match the quotes from Quotebank to the desired attribute, we use the `speaker` attribute in the Quotebank dataset. More information about the functions can be found in the notebook. 
 
## Methods
The main methods we will use in this project are:
* Hypothesis testing, in particular paired t-tests and Welch's t-test
    * To test the significance of differences in mood
* Confidence Intervals
    * To quantify the uncertainty in our results
* Sentiment analysis by using the NLTK library for Python
    * We will use the sentiment.vader module to quantify the sentiment in quotes 

The methods and their mathematical outlines are described in more detail in the bottom of the notebook delivery.

## Proposed timeline
The timeline stretches from 12 November to 17 December. We plan to finish the project by 12 December to spare some time for unforeseen problems and feedback from our teaching assistant. Most of the work is planned after 26 November as work with Homework 2 will be prioritized before 26 November.

__26 Nov__: Initial sentiment analysis on the mood on Mondays vs. Fridays and corresponding significance testing completed.

__28 Nov__: Sentiment analysis and hypothesis testing for the mood over weeks/seasons/months completed.

__30 Nov__: Initial Github page created with non-polished results from the initial analyses.

__3 Dec__: Completed sentiment analysis for media outlets.

__3 Dec__: Speak with the Teaching Assistant about our current findings to identify what to prioritize for the last part of the project.

__5 Dec__: Completed sentiment analysis for subsamples of men and women and politicians.

__8 Dec__: Populated Github page with all analysis we want to include in the data story.

__10 Dec__: Completed writing the draft for the data story.

__12 Dec__: Spell-checking and other polishing of the data story finished. Data story sent to the Teaching Assistant for feedback.

__14 Dec__: Feedback received and processed. 

__15 Dec__: Changes to data story made to the Github pages.

__16 Dec__: Celebrating the completion of the data story and its tremendous visualizations and exciting insights.

## Organization within the team:
Each member will have a main responsibility for milestone 3. However, all members will be involved in all milestone processes to ensure the best possible collaboration.

*__Name__: Responsibilities*

__Asbjørn__: General processing and analysis in early phases, due 8 December and visualizations for data story due 12 December.

__Benjamin__: Sentiment analysis and hypothesis testing due 8 December.

__Marcus__: Processing and analysis involving the Wikidata set, i.e., men/women and politicians with due date 3 December.

__Sigurd__: Written part of the final data story and visualizations, due 10 December.

## Questions for TAs
* If we during milestone 3, find some initial research that would support our data story. Is it ok to do them or should we stick to the research questions in this ReadMe-file?
* Do you think that the research questions are feasible, or do you have any concerns?
* Currently we use the vader lexicon to implement our sentiment analysis. Do you have any experience with this lexicon and if so, do you think it is a smart choice of model for sentiment analysis? Alternatively, do you have any alternative options you recommend? 
* If you see any improvements we could do to make the code run faster on the big dataset, we would love to hear them!
