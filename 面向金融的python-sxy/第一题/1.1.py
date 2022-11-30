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

df = pd.read_csv("python期末报告/data/m-a_edges.csv", delimiter="\t")
dl = df.groupby('source')
print(dl)
APInum = []
for k, v in dl:
   APInum.append([k, len(v.values)])
APInum.sort(key=lambda x: x[1], reverse=True)
# print(APInum)
file1 = open("python期末报告/每个Mashup中的包含Web API个数.csv", "w", encoding='utf-8-sig', newline='')
wr = csv.writer(file1, delimiter='\t')
wr.writerow(["Mashup", "WebApi个数"])

for i, element in enumerate(APInum):
   if i < 15:
      plt.barh(element[0], element[1])
   wr.writerow([element[0], element[1]])

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams['font.size'] = 25
plt.title("每个Mashup包含的Web API的个数(前15)")
plt.xlabel("Web API个数")
plt.rcParams['figure.figsize'] = (23, 13)
plt.savefig("python期末报告/每个Mashup中的包含Web API个数.png", bbox_inches='tight')




