# Risk assessment for population exposed to drought


## Risk assessment methodology

The approach is to visualize the exposed vulnerable population to the drought. This can be done by overlaying the hazard data of drought, expressed as Combined Drought Indicator (CDI), and population data.


## Datasets

The CDI (the hazard component of this drought risk workflow) that is implemented in the European Drought Observatory (EDO) is used to identify areas affected by agricultural drought and areas with the potential to be affected. CDI can be downloaded from the [Copernicus data server](https://edo.jrc.ec.europa.eu/gdo/php/index.php?id=2112) and is derived by combining three drought indicators produced operationally in the EDO framework - namely the

- **Standardized Precipitation Index (SPI)**: The SPI indicator measures precipitation anomalies at a given location, based on a comparison of observed total precipitation amounts for an accumulation period of interest (e.g. 1, 3, 12, 48 months), with the long-term historic rainfall record for that period (McKee et al., 1993; Edwards and McKee, 1997).
- **Soil Moisture Anomaly (SMA)**: The SMA indicator is derived from anomalies of estimated daily soil moisture (or soil water) content - represented as standardized soil moisture index (SMI) - which is produced by the JRC’s LISFLOOD hydrological model, and which has been shown to be effective for drought detection purposes (Laguardia and Niemeyer, 2008).
- **FAPAR Anomaly**: The FAPAR Anomaly indicator is computed as deviations of the biophysical variable Fraction of Absorbed Photosynthetically Active Radiation (FAPAR), composited for 10- day intervals, from long-term mean values. Satellite-measured FAPAR represents the fraction of incident solar radiation that is absorbed by land vegetation for photosynthesis and is effective for detecting and assessing drought impacts on vegetation canopies (Gobron et al., 2005).

Exposure is assessed by overlaying the European population density map at 30 arcsec resolution using the [Global Human Settlement Population dataset](https://ghsl.jrc.ec.europa.eu/download.php?ds=pop).


## Output of the workflow

A map overlapping the number of affected populations with CDI. In particular, areas are classified according to three primary CDI drought classes as:

  1. **Watch**:
     indicating that precipitation is less than normal.
     SPI-3 <-1 or SPI-1 < -2.
  2. **Warning**:
     indicating that soil moisture is in deficit.
     SMA <-1 and (SPI-3 < -1 or SPI-1 < -2).
  3. **Alert**:
     indicating that vegetation shows signs of stress.
     DeltaFAPAR < -1 and (SPI-3 < -1 or SPI-1 < -2).

Two additional classes, namely

  4. **Partial recovery** and
  5. **Recovery**,

identify the stages of the vegetation recovery process.
 
