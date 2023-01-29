# European Earthquake Scenario Loss Repository 

This repository provides aggregated loss/damage data  of past earthquake scenarios in Europe from various sources, together with associated [OpenQuake-engine](https://github.com/gem/oq-engine) scenario input models, based on the European Seismic Risk Model, [ESRM20](https://gitlab.seismo.ethz.ch/efehr/esrm20) (Crowley et al, 2021). 


## Organisation of the repository 

This repository is organised into two main directories:
- `loss_data`: this includes summaries of both reported and modelled losses for a number of earthquake events that have occurred in Europe.
- `models`: this includes the [OpenQuake-engine](https://github.com/gem/oq-engine) scenario input models. Inside the `selected_damaging_events` folder you will find a `summary_selected_damaging_events.xlsx` file which summarises the main characteristics of these events, and includes the assumptions used in the rupture sources models.  

If you would like to run the scenario calculations yourself, you will need to add organise the folder `esrm20` (inside the `models` folder) as follows:
- `Exposure_30arcsec`: Directory into which you should copy all the exposure files from the [esrm20 Exposure_30arcsec repository](https://gitlab.seismo.ethz.ch/efehr/esrm20/Exposure_30arcsec).
- `Vulnerability`: Directory into which you should copy all of the files from the [esrm20 Vulnerability repository](https://gitlab.seismo.ethz.ch/efehr/esrm20/Vulnerability).
- `Vs30`: Directory into which you should copy all of the files from the [esrm20 Vs30 repository](https://gitlab.seismo.ethz.ch/efehr/esrm20/Vs30).
- `GMPE`: this folder is already provided with this repository and includes the ground motion models for different tectonic environments.

## Acknowledgements

This repository has been developed within the SERA and RISE projects, with funding
received from the European Union's Horizon 2020 research and innovation programme under
grant agreements No. 730900 and 821115, respectively, and the Geo-INQUIRE project, with funding received from the the European Union's Horizon Europe programme under grant agreement No. 101058518.

## License 

This work is licensed under the Creative Commons Attribution 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or 
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## How to cite this work


If you make use of the data in this repository in any way, please cite as follows:

H. Crowley, J. Dabbeek, L. Danciu, P. Kalakonas, E. Riga, V. Silva, E. Veliu, G. Weatherill (2021). 
Earthquake Scenario Loss Testing Repository (Version 1.0) [Data set] https://doi.org/10.5281/zenodo.5728008

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5728008.svg)](https://doi.org/10.5281/zenodo.5728008)


## Contact

If you have any questions or feedback on the data included in this repository, please send it via email to 'efehr.risk@sed.ethz.ch'.

## References

Crowley H., Dabbeek J., Despotaki V., Rodrigues D., Martins L., Silva V., Romão, X., Pereira N., Weatherill G. and Danciu L. (2021) European Seismic Risk Model (ESRM20), EFEHR Technical Report 002, V1.0.0, https://doi.org/10.7414/EUC-EFEHR-TR002-ESRM20