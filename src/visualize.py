import pandas as pd
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as pp
from csv import DictReader


hotel_cluster = []
srch_dest_id = []
for i, row in enumerate(DictReader(open("../input/train.csv"))):
	hotel_cluster.append(int(row['hotel_cluster']))
	srch_dest_id.append(int(row['srch_destination_id']))



