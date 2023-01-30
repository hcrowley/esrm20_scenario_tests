# USGS ShakeMap Atlas v4 - European events from 2000 to 2022

## ShakeMaps

The ShakeMaps for the events in the `summary_usgs_shakemap_atlas-v4_2000-2022.xlsx` have not been saved here but can be downloaded using the web services provided by USGS. As described [here](http://usgs.github.io/shakemap/manual4_0/ug_products.html#subsec-comcat), users should first install [libcomcat](https://github.com/usgs/libcomcat) and then the following commands can be used to extract the ShakeMap files (`grid.xml` and `uncertainty.xml`) based on the `id` provided in `summary_usgs_shakemap_atlas-v4_2000-2022.xlsx`

```
getproduct shakemap grid.xml -i {id} --get-source atlas -d .
getproduct shakemap uncertainty.xml -i {id} --get-source atlas -d .

```

## OpenQuake-engine calculations

To run scenario damage and loss calculatins with these ShakeMaps, the [ESRM20 models](https://gitlab.seismo.ethz.ch/efehr/esrm20), and the [OpenQuake-engine](https://github.com/gem/oq-engine) you can make use of the scripts provided with the [European Rapid earthquake Loss Assessment Code](https://gitlab.seismo.ethz.ch/hcrowley/rapid_loss_eu). However, please note that some changes will need to be made to those scripts, as the code is currently set up to download ShakeMaps from the [European ShakeMap Archive](http://shakemapeu.ingv.it/archive.html). If you would like any support in making these changes, please contact 'efehr.risk@sed.ethz.ch'.


