# Risk assessment for drought - Advanced risk workflow


## Risk assessment methodology

Drought risk is a measure for quantifying the likelihood of an impact from a drought event (or multiple events) on the population, economic activities and assets, and on the environment.
The risk is assessed as a combination of drought hazard, exposure, and vulnerability.
- Hazard measures the magnitude, duration, and timing of drought events.
- Exposure to droughts represents the spatial distribution of drought relative to the distribution of potentially impactful systems, e.g., location of cultivated land, wetlands, etc.
- Vulnerability stands for the level of impact expected for a given system during a given event and is affected by the systems' intrinsic attributes. For example, fields with drought-resistant crop varieties would be less vulnerable to droughts.

This workflow quantifies drought risk as the product of drought hazard (dH), exposure (dE), and vulnerability (dV). The methodology used here was developed and applied globally by Carrão et al. (2016) 


## Quantifying drought hazard

Hazard indicators Drought hazard (dH) for a given region is estimated as the probability of exceedance of the median of regional (e.g., EU level) severe precipitation deficits for the historical reference period 1979 -2019. The precipitation deficit is calculated using the weighted anomaly of standardized precipitation (WASP) index. This index accounts for precipitation seasonal patterns and is computed by summing weighted and standardized monthly precipitation anomalies (Lyon and Barnston, 2005).

We use the weighted anomaly of standardized precipitation (WASP) index to define the severity of precipitation deficit. The WASP-index takes into account the annual seasonality of the precipitation cycle and is computed as a function of monthly precipitation, a monthly threshold defining precipitation severity, and the annual threshold for precipitation severity. The thresholds are defined by dividing multi-annual monthly observed rain using the 'Fisher-jenks' classification algorithm.

This algorithm requires monthly total precipitation for each NUTS2 region during the historical reference period. Usually, these are observation-based or simulated time series of gridded precipitation data. Processing these data is performed by applying Geographic Information System (GIS) techniques, to extract an aggregated value (e.g., total precipitation) of the data points located within each area of interest (e.g., NUTS2 region). Zonal statistics is widely used for that purpose.


## Quantifying drought exposure

Drought exposure (dE) indicates the potential losses from different types of drought disasters in different geographic regions. Quantifying drought exposure utilizes a non-compensatory model to account for the spatial distribution of a potential impact on crops and livestock, competition on water (e.g., for industrial uses represented by the water stress indicator), and human direct need (e.g., for drinking represented by population size). We apply a Data Envelopment Analysis (DEA) to determine the relative exposure of each region to drought.

Data Envelopment Analysis (DEA) has been broadly used for evaluating the efficiency of decision-making units (DMUs) in many areas for organizational performance improvement, such as financial institutions, manufacturing companies, hospitals, airlines, and government agencies. In the same way DEA estimates the relative efficiency of the decision-making units, DEA can also be used to quantify the relative exposure of a region (the DMUs in this case) to drought from a multidimensional set of indicators.

DEA works with a set of multiple inputs and outputs. In our case, the regions are described only the indicators so a dummy output that has unity value can be used, i.e. all the outputs are the same and equal, e.g. 1000. The efficiency of each region is estimated as a weighted sum of outputs divided by a weighted sum of inputs, where all efficiencies are restricted to lie between zero and one. An optimization algorithm is used for the weights to achieve the highest efficiency.

The assessment of drought exposure is based on a non-compensatory model to account for the spatial distribution of a potential impact on crops and livestock, competition on water (e.g., for industrial uses represented by the water stress indicator), and human direct need (e.g., for drinking represented by population size).

TABLE 1

## Quantifying drought vulnerability

Vulnerability to drought is computed as a 2-step composite model that derives from the aggregation of proxy indicators representing the economic, social, and infrastructural factors of vulnerability at each geographic location.

In the first step, indicators for each factor (i.e. economic, social, and infrastructural) are combined using a DEA model (Sherman and Zhi, 2006), similar to drought exposure. In the second step, individual factors resulting from independent DEA analyses are arithmetically aggregated (using the simple mean) into a composite model of drought vulnerability (dV).

The normalization of the vulnerability indicator accounts for the correlation of the indicator with drought vulnerability. The correlation is given in the table below.

TABLE 2

Social_ | Government Effectiveness | Government Effectivenesse is one of the indicators used by the Worldwide Governance Indicators (WGI) project, which features six aggregate governance indicators for over 200 countries and territories over the period 1996–2022. Government effectiveness captures perceptions of the quality of public services, the quality of the civil service and the degree of its independence from political pressures, the quality of policy formulation and implementation, and the credibility of the government's commitment to such policies. | The six aggregate indicators are reported in tabular format in two ways: (1) in their standard normal units, ranging from approximately -2.5 to 2.5, and (2) in percentile rank terms from 0 to 100, with higher values corresponding to better outcomes. | + | https://www.gu.se/en/quality-government/qog-data/data-downloads/european-quality-of-government-index | Social_ | Management of Water related Disasters | Self reporting on national compliance with the SDG 6.5.1 targets: Management of water-related disasters (3.1e). | The data represents the percent of compliance between 0-100, and is given at a country scale in a tabular format for the year 2020. | - | http://iwrmdataportal.unepdhi.org/country-reports | | Infrast_ | Agricultural irrigated land (percentage of total agricultural land) | Agricultural land is the combination of crop (arable) and grazing land. Data show the percentage of total agricultural land area that is irrigated (i.e. purposely provided with water), including land irrigated by controlled flooding. | EUROSTAT data is available in tabular format at the NUTS2 level. | - | https://ec.europa.eu/eurostat/web/main/data/database | Infrast_ | Road density | The Global Roads Inventory Project is a harmonized global dataset of approximately 60 geospatial datasets on road infrastructure collected for 2018. This dataset includes 5 road types: highways/ primary/ secondary/ tertiary/ local roads. | 5 arc-minutes grid. All grids are to be summed and aggregated (using Zonal Statistics) per area of interest. | - | https://www.globio.info/download-grip-dataset



## Workflow implementation

See the files Hazard_Assessment.ipynb and Risk_Assessment.ipynb.


## Output of the workflow

The resulting risk map shows relative drought risk classes ranging between 1 (low risk, 0 -0.2 risk) to 5 (high risk, 0.8 -1) of different spatial units (i.e., NUTS2) out of a bigger region (i.e., European Union).

## Contributors

The workflow has been developed by Silvia Artuso and Dor Fridman from IIASA's Water Security Research Group, and supported by Michaela Bachmann from IIASA's Systemic Risk and Resilience Research Group.


## Reference

Carrão, H., Naumann, G., & Barbosa, P. (2016). Mapping global patterns of drought risk: An empirical framework based on sub-national estimates of hazard, exposure and vulnerability. Global Environmental Change, 39, 108-124.
Lyon, B., & Barnston, A. G. (2005). ENSO and the spatial extent of interannual precipitation extremes in tropical land areas. Journal of climate, 18(23), 5095-5109.
Sherman, H. D., & Zhu, J. (2006). Service productivity management: Improving service performance using data envelopment analysis (DEA). Springer science & business media.
