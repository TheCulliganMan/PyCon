import sys

from src import country_sub
from src import plotwines
from src import subset

COUNTRY = 'Chile'
FILENAME = 'data/raw/winemag-data_first150k.csv'

interum_result = subset.process_data_GBP(FILENAME)

plotwines.create_plots(interum_result)

final_result = country_sub.get_country(interum_result, COUNTRY)

print(final_result)