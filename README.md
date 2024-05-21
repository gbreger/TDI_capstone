[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gbreger/TDI_capstone/HEAD)

Binder: https://hub.binder.curvenote.dev/user/gbreger-tdi_capstone-temmqdpn/lab

# Predicting sales of video game development proposals
The video game industry is a multi-billion dollar industry, with new games coming out every day. The project aims to provide studios and publishers with projections of expected sales to better determine in which proposed video game project should they invest, maximizing their use of resources, financial or otherwise (though arguably, some video games should be made, regardless of their profitability).

## Problem Statement
The video game industry is a multi-billion dollar industry, with new games coming out every day. Some games rack up sales of millions of dollars while others falter. Conversely, games often require a substantial investment to develop and may take years to come to fruition. This project provides game publishers and studios with projections of expected sales of proposed video game projects in order to better determine which projects are indeed worth investing in and to what extent, thereby maximizing the use of their resources, financial or otherwise. The project does so by analyzing historical data of sales of games, from 2010 through 2020, alongside features of these games, such as genres, themes, player perspective, or association with established franchises.

## Project Description
The project uses two datasets, one for sales of games and the other for description of games and their features. The sales data is taken from Kaggle (https://www.kaggle.com/datasets/thedevastator/global-video-game-sales-and-reviews). The data itself was well structured for the most part and required little handling, primarily standardizing strings. The game description data was queried from the website www.igdb.com, an online database for video games. It was queried by accessing IGDB's API using the python code written in the data collection notebook (currently not published due to access key being included in the code directly). The data required substantial cleaning and refining, such as standardizing strings, parsing lists, transforming dates and platforms (so as to match the platforms data in the sales data). The size of the file was too large for GitHub (over 200mb) and so was broken down to 10 separate files.

The project defines a unique game as a combination of its name, platform, and year of release (AKA release_year). Games that share the same name and release year but different platforms are considered different games because the difference in platform may result in different sales. In order to merge the sales and game description data sets, all three of these needed to align. While doing so for release year and platform was fairly straightforward (due to the limited variability in these fields), possible variations in names of games needed to be taken into account. To solve this issue, for each platform/year combination, the project found the closest name match between the two data sets. A cut off score of 90% match was determined to provide the most matches with the least amount of mismatches. All of this is found in the data engineering notebook.

Once the two data sets were joined, it was possible to train a predictive model using machine learning, found in the model notebook. Most of the features were categorical, e.g., genre, platform, theme. Several of these features were singular classes, so could be one-hot encoded. The majority of the categorical data, however, was in the form of lists, i.e., for each observation a feature would be a list of values (for example, multiple themes for a single game). These were transformed into dictionaries and then vectorized. Two fields were free form descriptions of the game summary and storyline and were handled by a TFIDF vectorizer. Since all of these transformations created a large, yet sparse dimensional space, dimensionality reduction was used. In this case, truncated singular value decomposition (TruncatedSVD) that can handle sparse data. Several regressors were tested, including LinearRegression, Ridge, RandomForestRegressor, and KNeighborsRegressor. A train/test split was down (95/5) and the model was given the features and the log of sales to train on. Cross-validation was done for all regressors except for LinearRegression. The model did not perform well, with the highest R-squared score of 0.65 using a Ridge regressor. This suggests that the features utilized by this project are not good indicators of sales. Conversely, other factors not found in the data can impact sales. Potentially, with a richer data set, the model would be able to provide more accurate predictions. Note, however, that the video game industry is quite conservative with releasing this kind of information. Note also that the project makes an assumption that the overwhelming majority of a game's sales take place during its first year after release. Games that have been available longer would naturally have higher sales potential.
