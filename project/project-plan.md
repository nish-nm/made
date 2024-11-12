# Project Plan

## Title
<!-- Give your project a short title. -->
Income and Environmental Impact: Exploring Socioeconomic Influences on Deforestation and CO₂ Emissions in the U.S.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a significant relationship between median household income and environmental impact—specifically, deforestation and CO₂ emissions—across U.S. states?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
his data science project explores the correlation between socioeconomic factors, specifically median household income, and environmental conditions, focusing on deforestation and CO₂ emissions across U.S. states. The project aims to understand if and how economic disparities influence environmental impact, providing insights that could inform policy decisions for sustainable development.

The project follows an ETL (Extract, Transform, Load) pipeline to collect data from reputable sources like the NCES for income data and the Global Forest Watch for environmental metrics. The pipeline cleans, merges, and loads this data into a structured SQLite database for analysis. Using statistical methods, including correlation and hypothesis testing, the project examines relationships between income levels and environmental degradation indicators.

This approach enables the exploration of hypotheses, such as whether higher-income states exhibit less deforestation or CO₂ emissions. Results are visualized through choropleth maps and scatter plots to reveal geographic trends and potential income-based environmental patterns. Ultimately, the project provides a data-driven foundation for understanding socioeconomic and environmental interplay, contributing to ongoing discussions on sustainability and economic equity.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Digest of Education Statistics
* Metadata URL: [Digest of Education Statistics](https://nces.ed.gov/programs/digest/index.asp)
* Data URL: [Median household income, by state: Selected years, 1990 through 2021 Excel](https://nces.ed.gov/programs/digest/d22/tables/xls/tabn102.30.xlsx)
* Data Type: Excel 
* Description: This data source provides median data for the United States with state level granularity of income spanning for years of 1990, 2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2021.

### Datasource2: Global Forest Watch (GFW)
* Metadata URL: [Global Forest Watch](https://www.globalforestwatch.org/)
* Data URL: [GFW Data XLSX](https://gfw2-data.s3.amazonaws.com/country-pages/country_stats/download/2023/USA.xlsx)
* Data Type: Excel (XLSX)
* Description: This source offers deforestation statistics, including tree cover loss and carbon emissions related to land-use changes, providing an understanding of environmental conditions in the US.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Project Defiiniition [#1][i1]
2. ETL Pipeline [#2][i2]
3. Data Analysis and Data Report [#3][i3]
4. Automated Testing [#4][i4]
5. CI [#5][i5]
6. Results Report [#6][i6]

[i1]: https://github.com/nish-nm/made/milestone/1
[i2]: https://github.com/nish-nm/made/milestone/2
[i3]: https://github.com/nish-nm/made/milestone/3
[i4]: https://github.com/nish-nm/made/milestone/4
[i5]: https://github.com/nish-nm/made/milestone/5
[i6]: https://github.com/nish-nm/made/milestone/6

