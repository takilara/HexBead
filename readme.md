Usage 
python hexbead.py -h

Note, the averaging modes are dictating the averaging mechanics used to create the "hexes".
Mode will tend to give better results than Median.

Example:
python hexbead.py --mode all --size 20 ..\HexGrid\charmander.png charhex.png

Will ouput the following images:
charhex_mode_20.png
!(resources/charhex_mode_20.png)

charhex_median_20.png
!(resources/charhex_median_20.png)