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

dl = df['target'].value_counts()
WAnum = list(dl.items())
WAnum.sort(key=lambda x:x[1],reverse=True)
file2 = open("python期末报告/每个Web API被使用的次数.csv", "w", encoding='utf-8-sig', newline='')
wr = csv.writer(file2,delimiter='\t')
wr.writerow(["url","WebAPI使用次数"])

for i,element in enumerate(WAnum):
    if i<15:
        plt.barh(element[0],element[1])
    wr.writerow([element[0],element[1]])

plt.title("每个Web API被使用的次数(前15)")
plt.xlabel("Web API被使用的次数")
plt.savefig("python期末报告/每个Web API被使用的次数.png",bbox_inches='tight')

