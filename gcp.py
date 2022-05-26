# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

gcp=pd.read_csv(r"H:\20200610_wbs1_macro\gcp\20200609nancypaired_15gcp.csv")

gcp2=gcp.assign(index=gcp.index)

gcp2.to_csv(r"H:\20200610_wbs1_macro\gcp\20200609nancypaired_15gcp_index.csv")