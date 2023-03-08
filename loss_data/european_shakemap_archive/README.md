# Loss Data: European ShakeMap Archive


The file `losses_european_shakemap_archive_2000-2022.xlsx` includes both reported (from NCEI/WDS Global Significant Earthquake Database and EMDAT) and modelled losses (using [ESRM20 exposure and vulnerability models](https://gitlab.seismo.ethz.ch/efehr/esrm20): Crowley et al., 2021) for 1048 events that have occurred in Europe between April 2020 (when the European ShakeMap Archive became operational) and 2022. The ShakeMaps for events have been extracted from the [European ShakeMap Archive](http://shakemapeu.ingv.it/archive.html): the details of these events can be found in `models/european_shakemap_archive` directory.  

A plots comparing the reported and median predicted losses is also provided. This plot also shows the [USGS PAGER](https://earthquake.usgs.gov/data/pager/) alert levels (see Wald et al., 2022).   

## Comparison plot: EMDAT fatalities

<img src="./EMDAT_vs_model_fatality_ShakeMap_EU2020-2022" alt="EMDAT_rupture_ecoloss" width="400" 


## References

Crowley H., Dabbeek J., Despotaki V., Rodrigues D., Martins L., Silva V., Romão, X., Pereira N., Weatherill G. and Danciu L. (2021) European Seismic Risk Model (ESRM20), EFEHR Technical Report 002, V1.0.0, [https://doi.org/10.7414/EUC-EFEHR-TR002-ESRM20](https://doi.org/10.7414/EUC-EFEHR-TR002-ESRM20)

EMDAT (n.d.) International Disasters Database of the Centre for Research on the Epidemiology of Disasters, Available at: [https://www.emdat.be/](https://www.emdat.be/) (accessed 15 September 2021).

National Geophysical Data Center / World Data Service (NGDC/WDS): NCEI/WDS Global Significant Earthquake Database. NOAA National Centers for Environmental Information. doi:10.7289/V5TD9V7K (accessed 21 November 2021)

Wald D.J., Maranoo K.D., Jaiswal K.S., Thompson E., James-Ravenell M.J. and Hearne M. (2022) "Evaluating a Decade of U.S. Geological Survey’s PAGER Real-Time Earthquake Loss Estimates" 12th National Conference on Earthquake Engineering, Salt Lake City, Utah. 





