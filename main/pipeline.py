import pandas as pd
import numpy as np
import csv

with open('../timeseries_province/cases_timeseries_prov.csv',
          mode="r") as cases_timeseries_prov:
    reader = csv.reader(cases_timeseries_prov)
    for item in reader:
        # you have to loop through the document to get each data
        print(item)
