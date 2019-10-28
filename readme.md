# Usage 
python hexbead.py -h

Note, the averaging modes are dictating the averaging mechanics used to create the "hexes".
Mode will tend to give better results than Median.

# Examples:
python hexbead.py --mode all --size 20 ..\HexGrid\charmander.png charhex.png

Will ouput the following images:

charhex_mode.png
![charhex_mode.png](resources/charhex_mode_20.png "20x20 cells, using Mode for averaging")

charhex_median.png
![charhex_median.png](resources/charhex_median_20.png "20x20 cells, using Median for averaging")

python hexbead.py --mode all --size 50 ..\HexGrid\charmander.png charhex.png

charhex_mode.png
![charhex_mode.png](resources/charhex_mode_50.png "50x50 cells, using Mode for averaging")

charhex_median.png
![charhex_median.png](resources/charhex_median_50.png "50x50 cells, using Median for averaging")