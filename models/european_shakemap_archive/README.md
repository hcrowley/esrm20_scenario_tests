# European ShakeMap Archive

## ShakeMaps

The ShakeMaps for the events in the `summary_european_shakemap_archive_2020-2022.xlsx` have not been saved here but can be downloaded using the web services provided by the [European ShakeMap Service](http://shakemapeu.ingv.it/). The following commands can be used in Python to extract the ShakeMap files (`grid.xml` and `uncertainty.xml`) based on the unique id (`unid`) provided on the website. 

```
import requests

grid = requests.get('http://shakemapeu.ingv.it/data/{}/current/products/grid.xml'.format(unid)).text

uncertainty = requests.get('http://shakemapeu.ingv.it/data/{}/current/products/uncertainty.xml'.format(unid)).text

```

## OpenQuake-engine calculations

To run scenario damage and loss calculations with these ShakeMaps, the [ESRM20 models](https://gitlab.seismo.ethz.ch/efehr/esrm20), and the [OpenQuake-engine](https://github.com/gem/oq-engine) you can make use of the scripts provided with the [European Rapid earthquake Loss Assessment Code](https://gitlab.seismo.ethz.ch/hcrowley/rapid_loss_eu). These tools already download the ShakeMaps using the web service commands described above. If you would like any support with these calculations, please contact 'efehr.risk@sed.ethz.ch'.


