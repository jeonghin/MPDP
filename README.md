# Malaysian Political Dynamics Predictor (MPDP)
## Overview
The Malaysian Political Dynamics Predictor (MPDP) is a data-driven project designed to analyze and predict key aspects of the Malaysian political landscape. This project primarily focuses on forecasting party-switching behavior among politicians, identifying influential figures in such transitions, and projecting potential coalition formations. It leverages historical election data, political affiliations, and other relevant political events from the 2020–2022 Malaysian political crisis.

## Background
The 2020–2022 Malaysian political crisis, marked by significant party shifts, coalition government collapses, and the rapid succession of prime ministers, presents a complex political landscape for analysis. The crisis peaked with a snap general election in 2022, leading to the formation of a new coalition government. Key events like the Sheraton Move, which saw the fall of the Pakatan Harapan government and the resignation of Prime Minister Mahathir Mohamad, epitomize the political volatility that this project aims to decipher.

## Data Sources
1. Wikipedia: Entries detailing Malaysian political parties and politicians, linked with election outcomes.
2. Thevesh Theva's Github: Thevesh's data on Malaysian parliamentary election results

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

### results_parlimen_ge15.csv

This file provides information about the election results for the parliamentary constituencies.

- `state`: The state in Malaysia where the election is being held.
- `parlimen`: The parliamentary constituency within the state.
- `undi_keluar_peti`: The number of ballots taken out from the ballot boxes.
- `undi_dalam_peti`: The number of ballots found inside the ballot boxes.
- `undi_tak_kembali`: The number of ballots not returned.
- `undi_tolak`: The number of rejected ballots.
- `majoriti`: The majority margin (i.e., the difference in votes between the winning candidate and the runner-up).
- `peratus_keluar`: The percentage of voter turnout.
- `undi_rosak`: The number of spoiled ballots.
- `pengundi_jumlah`: The total number of registered voters in the constituency.
- `pengundi_tidak_hadir`: The number of registered voters who did not vote.
- `rosak_vs_keseluruhan`: The proportion of spoiled ballots compared to the total ballots.
- `rosak_vs_majoriti`: The proportion of spoiled ballots compared to the majority margin.
- `tidakhadir_vs_majoriti`: The proportion of non-voters compared to the majority margin.

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

## Goals
1. __Predicting Party-Switching Likelihood__: Determine the probability of Malaysian politicians switching political parties.
2. __Identifying Key Influencers__: Recognize politicians who significantly influence others to change parties, such as Azmin Ali's role in the defection of MPs from PKR to BERSATU.
3. __Forecasting Coalition Formations__: Analyze potential alliances between political parties, considering historical rivalries and recent collaborations.

## Methodology
The project employs a combination of statistical analysis, machine learning models, and network analysis to:

- Analyze historical voting patterns and political affiliations.
- Identify patterns in party-switching behavior.
- Model the influence of key political figures.
- Simulate potential future political alliances and coalition formations.

## How to Use

### Clone
`git clone git@github.com:jeonghin/MPDP.git`

### Dependencies
`pip install -r requirements.txt`


## License
This project is licensed under the [MIT License](LICENSE)

## Acknowledgments
Special thanks to Thevesh Theva's open data and Dr. Bobby Madamanchi's guidance.