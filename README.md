# Malaysian Political Dynamics Predictor (MPDP)

## Overview
The Malaysian Political Dynamics Predictor (MPDP) is a web-based application designed to predict the outcomes of Malaysian parliamentary seats based on demographic data and other relevant factors. It utilizes machine learning models, specifically a RandomForestClassifier, to analyze and predict election results, and GPT-4-Turbo to provide reasoning and relevant information on the various Malaysian constituencies. The application provides an interface for users to input key characteristics such as age, gender, party affiliation, ethnicity, and the specific parliamentary region (parlimen) to receive a prediction and reasoning for the election outcome. 

## Background
In the dynamic landscape of Malaysian politics, where demographics and party affiliations play a significant role, the MPDP serves as a tool to explore the interplay of these factors and their potential impact on election results. By examining data from past census records and considering the influence of various attributes, the MPDP aims to bring a data-driven approach to understanding political trends.

## Goals
1. To provide an accessible platform for political analysts, researchers, and the public to forecast election outcomes.
2. To offer insights into the demographic and political variables that are indicative of electoral success in Malaysia.
3. To foster a greater understanding of the Malaysian political climate through data visualization and interactive features such as the network graph of politicians and parties.

## Data Sources
1. Thevesh Theva's [Github](https://github.com/Thevesh/analysis-election-msia): Thevesh's data on Malaysian parliamentary election results

## Features
1. __Interactive Form__: Users can input demographic details and select a parliamentary region to generate predictions.
2. __Machine Learning Integration__: Incorporates a trained RandomForestClassifier to make predictions based on user inputs.
3. __GPT-4-Turbo Reasoning__: Utilizes a GPT model to provide a narrative explanation for the predicted outcomes, enhancing user understanding of the model's decision-making process.
4. __Network Visualization__: An embedded iframe displays the network graph detailing the connections between politicians and parties within the application.

## Usage

To use the MPDP, follow these steps:

1. Enter the candidate's age and ballot order in the provided input fields.
2. Select the candidate's gender, party affiliation, and ethnicity from the dropdown menus.
3. Choose the relevant parlimen code that corresponds to the candidate's region.
4. Click the "Submit" button to receive the prediction and reasoning. (Might take a while for the page to reload for reasoning)

You can also view the network graph to understand the relationships between politicians and parties located at the end of the page.

## Setup and Installation

### Clone
`git clone git@github.com:jeonghin/MPDP.git`

### Dependencies
`pip install -r requirements.txt`

### OpenAI Key

Navigate to `analysis.py` and paste your OpenAI key in there.


## Data Description

### candidates_ge15.csv

This file provides detailed information about the candidates in a general election.

- `state`: The state in Malaysia where the election is being held.
- `parlimen`: The parliamentary constituency within the state.
- `ballot_order`: The order in which the candidate's name appears on the ballot paper.
- `name`: The legal name of the candidate.
- `name_display`: The name of the candidate as displayed on the ballot paper or in public forums.
- `age`: The age of the candidate at the time of the election.
- `sex`: The gender of the candidate.
- `ethnicity`: The ethnic background of the candidate.
- `party`: The political party the candidate represents.
- `votes`: The number of votes received by the candidate.
- `result`: Indicates whether the candidate won or lost.
- `result_desc`: A description of the election result for the candidate (e.g., elected, not elected).
- `new_mp`: Indicates whether the candidate is a new Member of Parliament (MP) or not.

### census_parlimen.csv

This file provides census information for the parliamentary constituencies.

- `state`: The state or administrative area.
- `parlimen`: The parliamentary constituency.
- `code_state`: A numerical or coded representation of the state.
- `code_parlimen`: A numerical or coded representation of the parliamentary constituency.
- `year`: The year in which the census data was collected.
- `area_km2`: The total area of the parliamentary constituency in square kilometers.
- `population_total`: The total population within the parliamentary constituency.
- `nationality_citizen`: The number of citizens within the constituency.
- `nationality_non_citizen`: The number of non-citizens within the constituency.
- `sex_male`: The total male population within the constituency.
- `sex_female`: The total female population within the constituency.
- `ethnicity_proportion_bumi`: The proportion of the population that is Bumiputera (indigenous).
- `ethnicity_proportion_chinese`: The proportion of the population that is Chinese.
- `ethnicity_proportion_indian`: The proportion of the population that is Indian.
- `ethnicity_proportion_other`: The proportion of the population that is of other ethnicities.
- `age_proportion_0_14`: The proportion of the population aged 0-14.
- `age_proportion_15_64`: The proportion of the population aged 15-64.
- `age_proportion_65_above`: The proportion of the population aged 65 and above.
- `age_proportion_18_above`: The proportion of the population aged 18 and above.
- `housing_total`: The total number of housing units.
- `household_total`: The total number of households.
- `household_size_avg`: The average household size.
- `live_births`: The total number of live births.
- `live_births_male`: The number of live male births.
- `live_births_female`: The number of live female births.
- `deaths`: The total number of deaths.
- `deaths_male`: The number of male deaths.
- `deaths_female`: The number of female deaths.
- `labour_participation_rate`: The labor force participation rate.
- `labour_unemployment_rate`: The unemployment rate within the labor force.
- `income_median`: The median income.
- `income_avg`: The average income.
- `expenditure_avg`: The average expenditure.
- `gini`: The Gini coefficient (a measure of income inequality).
- `poverty_incidence`: The incidence of poverty.
- `sme_small`: The number of small-sized enterprises.
- `sme_micro`: The number of micro-sized enterprises.
- `sme_medium`: The number of medium-sized enterprises.
- `businesses_agriculture`: The number of businesses in the agriculture sector.
- `businesses_crops`: The number of crop-based businesses.
- `businesses_livestock`: The number of livestock-based businesses.
- `businesses_fisheries`: The number of fisheries-based businesses.
- `businesses_forestry`: The number of forestry-based businesses.
- `businesses_mining`: The number of mining-based businesses.
- `businesses_manufacturing`: The number of manufacturing businesses.
- `businesses_construction`: The number of construction businesses.
- `businesses_services`: The number of service-based businesses.
- `utilities_pipedwater_home`: The proportion of households with piped water at home.
- `utilities_pipedwater_public`: The proportion of households with access to public piped water.
- `utilities_pipedwater_other`: The proportion of households with access to other sources of piped water.
- `utilities_electricity_home`: The proportion of households with electricity at home.
- `utilities_electricity_none`: The proportion of households without electricity.


## License
This project is licensed under the [MIT License](LICENSE)

## Acknowledgments
Special thanks to Thevesh Theva's open data and Dr. Bobby Madamanchi's guidance.