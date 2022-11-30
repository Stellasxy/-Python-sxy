import json
import csv
import pandas as pd
import numpy as np
from scipy import stats
from  scipy.stats import chi2_contingency
import seaborn as sns
import re
import networkx as nx
import matplotlib.pyplot as plt

dt = {}
r1 = re.compile(r"/api/(.*?)\-.*")
r2 = re.compile(r"/api/(.*)")

for el in df['target']:
    if '-' in el:
        tp = r1.match(el)
        if tp.group(1) not in dt.keys():
            dt[tp.group(1)] = 0
        dt[tp.group(1)] += 1
    else:
        tp = r2.match(el)
        if tp.group(1) not in dt.keys():
            dt[tp.group(1)] = 0
        dt[tp.group(1)] += 1
pAPI = list(dt.items())
pAPI.sort(key=lambda x:x[1],reverse=True)

with open("python期末报告/Web API提供商（URL网址）发布Web API的个数.csv", "w", encoding='utf-8-sig', newline='') as file3:
    wr = csv.writer(file3)
    wr.writerow(["Web API提供商", "发布Web API的个数"])
    for i, el in enumerate(pAPI):
        if i<15:
            plt.barh(el[0],el[1])
        wr.writerow([el[0], el[1]])

plt.title("Web API提供商（URL网址）发布Web API的个数(前15)")
plt.xlabel("发布Web API的个数")
plt.savefig("python期末报告/Web API提供商（URL网址）发布Web API的个数.png",bbox_inches='tight')