import os
import matplotlib.pyplot as plt
import pandas as pd
#read csv
gcp=pd.read_csv(r"H:\20200610_wbs1_macro\gcp\20200609nancypaired_15gcp.csv")
#assign index
gcp2=gcp.assign(index=gcp.index)
#export to csv
gcp2.to_csv(r"H:\20200610_wbs1_macro\gcp\20200609nancypaired_15gcp_index.csv")
