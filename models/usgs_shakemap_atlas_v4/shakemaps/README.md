# USGS ShakeMap Atlas v4 - European events from 2000 to 2022

The ShakeMaps for the events in the `summary_usgs_shakemap_atlas-v4_2000-2022.xlsx` have not been saved here but can be downloaded using the web services provided by USGS. As described [here](http://usgs.github.io/shakemap/manual4_0/ug_products.html#subsec-comcat), users should first install [libcomcat](https://github.com/usgs/libcomcat) and then the following commands can be used to extract the ShakeMap files (`grid.xml` and `uncertainty.xml`) based on the `id` provided in `summary_usgs_shakemap_atlas-v4_2000-2022.xlsx`

``
getproduct shakemap grid.xml -i {id} --get-source atlas -d .
getproduct shakemap uncertainty.xml -i {id} --get-source atlas -d .

``
