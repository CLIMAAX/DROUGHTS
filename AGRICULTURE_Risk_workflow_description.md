# Agricultural Drought Risk Assessment Description
<br>
Climate change is posing an increasing threat to food production systems, furtherly complicating the challenge of satisfying the food demand of a rising global population while respecting the limits imposed by planetary resource boundaries. In Europe, the effects of climate change differ between historically semi-arid (e.g., Mediterranean) and wet (e.g., Central and North Europe) regions. In the former, while rainfall events will become less frequent and more extreme, droughts will get more severe and extend beyond the historical dry seasons, compromising the long-term stability of freshwater resources. At the same time, higher latitudes will experience a significant reduction in mean precipitation rates that, coupled with increasing mean temperatures, will negatively affect soil water availability. These climatic shifts have profound consequences for the agricultural sector. On one hand, semi-arid regions will be increasingly prone to water shortages and forced to reduce allocations to irrigation to satisfy other public needs. On the other, historically wet regions might be forced to invest in the large-scale expansion of their irrigation systems, as the decreasing water availability will hinder the potential of rainfed systems to satisfy growing production demands. In this context, a transition towards more water-stress-resilient agricultural practices is urgently needed to limit losses across the european food production system.
<br>
<br>
Indeed, risk quantification is a fundamental first step in the design of an effective adaptation strategy. Thus, the aim of this workflow is to provide a simple tool to quantify potential revenue losses caused by precipitation deficit. The hazard component of the asssessment is represented by the potential yield losses deriving from water scarcity, defined as the deficit in crop evapotranspiration potential, in the absence of irrigation. The total crop production and the aggregated crops revenue are used to quantify the exposure of the agricultural sector in economic terms. Finally, the current distribution of irrigation systems is used to map vulnerability. Thus, using this tool communities will get a spatial quantification of potential revenue losses from reduced crop production, and will also be able to identify the most vulnerable areas to precipitation deficits.

![risk_graphic](agriculture_risk_graphic.png)

## Datasets used

The assessment is based on well-established climate projections and global agricultural datasets allowing to estimate potential losses at approximately 10 km resolution. These include:

* Daily mean precipitation flux, maximum and minimum temperature, 2 m relative humidity, surface downward solar radiation and 10 m wind speed from CORDEX Climate projections (Copernicus Data Storage, 2019).
* Global production [ton] for 42 crops in 2010 from the MapSPAM repository (International Food Policy Research Institute, 2019).
* Crop aggregated value [US$] and irrigation availability for 2010 from the FAO-IIASA Global Agro-Ecological Zones data repository (GAEZ).

The tool is designed to work considering different future time periods and emission scenarios, allowing the user to understand the implications of different levels of gloabl warming. The user is invited to further personalise the workflow using local datasets for agricultural production to increase the accuracy of the assessment or to test the reliability of the default global datasets.






