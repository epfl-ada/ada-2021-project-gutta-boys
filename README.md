# An Investigation of the Mood in the Media Across Time and Subsamples

## Abstract

In this project, we investigated how the mood in the media and the debate differs over time and subsamples. Our motivation was to understand the general trends in the mood, and how they are reflected through quotations in the media. For example, does the temper get better towards the weekend, or do we love Mondays deep inside? Is the mood better in the summer than in the winter? In addition, we analyzed the sentiment across subsamples of different media outlets and professions.

Through the project, we examined the questions by doing sentiment analysis on the [Quotebank](https://dlab.epfl.ch/people/west/pub/Vaucher-Spitz-Catasta-West_WSDM-21.pdf) data set from 2015 to 2020. The sentiment is measured utilizing the compound score from the ([Vader Lexicon](https://www.nltk.org/_modules/nltk/sentiment/vader.html) and the subjectivity scores from the [TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html) library.

The resulting data story can be found [here](https://sigurdkampevold.github.io/media_mood/).

## Research questions

The research questions we started out with was all under the umbrella:

“How does the mood in the media differ across time and subsamples?”

More specifically, we wanted to investigate the following:

- Are there any differences in mood based on weekdays, weeks, or months?
- Are there any differences in the mood across media outlets?
- Do any subsamples differ from the general trends, for example, politicians or men/women?

## Key Insights

- There is no evidence for significant variations in the mood in media quotations across weekdays or months
- The mood in the media became significantly more negative in the first phase of the COVID-19 pandemic
- There are statistically significant differences in mood and subjectivity across media outlets. For example, sports and celebrity magazines tend to be more positive and subjective than daily newspapers
- There are no significant differences in mood in quotes from men and women
- On average, quotations from politicians are more negative than the average quotation

## Additional datasets

To complete our project, we used the “Wikidata metadata about speakers” dataset provided by the course. The motivation for this was to study subsamples of the data.

The dataset was primarily utilized for two purposes:

1. Extracting quotes where the most likely speaker is a politician
2. Separating quotes spoken by men and women

We utilized functions that matched politicians from the Wikidata dataset to quotes from the Quotebank data to process the additional dataset. We considered appending binary values for woman/man and politician/not-politician to the original dataset but found this too computationally expensive. We decided to rather use the functions on the go and analyzed subsamples. To match the quotes from Quotebank to the desired attribute, we used the speaker attribute in the Quotebank dataset. More information about the functions can be found in the notebook.

## Methods

The main methods utilized in this project are:

- Hypothesis testing, in particular paired t-tests and Welch’s t-test, to test the significance of differences in mood.
- Sentiment analysis by using the NLTK library and TextBlob library for Python.
- The sentiment.vader module from NLTK to quantify the sentiment, i.e., positivity and negativity of quotations.
- The TextBlob library to quantify the subjectivity of quotations.

The methods and their mathematical outlines are described in more detail at the bottom of the notebook delivery.

## Timeline

The timeline for the project stretched over three milestones from 22 September to 17 December.

**Milestone 1 (22.09 – 08.10)**

- Individual proposals for the project idea.

**Milestone 2 (08.10 - 12.11)**

- Final project idea and research questions.
- Initial analyses and data handling pipelines.

**Milestone 3 (12.11 - 17.12)**

Week 1 & 2 (12/11 - 21/11):

- Reviewing feedback from milestone 2.

Week 3 & 4 (22/11 - 05/12):

- Cleaning of data sets and appending necessary attributes for the different tasks.
- Initial sentiment analysis for time trend and subsamples.
- Launching the GitHub page.

Week 5 (06/11 - 12/11):

- Completion of sentiment analysis for time trend.
- Completion of sentiment analysis for media outlets.
- Finished draft for data story, including visualizations and diagrams.

Week 6 (13/11 - 17/11):

- Completion of sentiment analysis for subsamples of men and women and politicians.
- Spell-checking and other polishing of the data story finished.
- Finalization of the project notebook.
- Updating Readme
- Celebration of the data story and its tremendous visualizations and exciting insights.

## Organization within the team:

Each member had a main responsibility for the project. However, all members were involved in the processes by participating in the decision-making and discussions, ensuring the best possible collaboration. The group has met weekly throughout the semester and more frequently in busy periods.

_Name: Responsibilities_

**Asbjørn**: General processing and analysis in early phases. Focus on the media outlet analysis.

**Benjamin**: Analyzing the time trend of the dataset. Responsible for defining the statistical methods and ensuring uniform code quality.

**Marcus**: Processing and analyses involving the Wikidata set, i.e., men/women and politicians.

**Sigurd**: Launching of GitHub page. Responsible for the creativity and written part of the final data story.
