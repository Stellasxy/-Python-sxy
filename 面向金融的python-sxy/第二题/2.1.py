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

file = open("python期末报告/Mp_WA.csv", "w", encoding='utf-8-sig', newline='')
wr = csv.writer(file,delimiter='\t')
wr.writerow(["类别", "Mp","WA"])
df1 = pd.read_csv("python期末报告/data/m-a_edges.csv", delimiter="\t")
df2 = pd.read_csv("python期末报告/data/mashup_nodes_estimator.csv", delimiter="\t")
group_c = df2.groupby('c')
for k, v in group_c:
    for i in v['name']:
        for el in df1[df1['source'] == i]['target'].values:
            wr.writerow([k,i,el])
file.close()

file1 = open("python期末报告/Chi_square.csv", "w", encoding='utf-8-sig', newline='')
wr = csv.writer(file1)
wr.writerow(["类别","p值","df","95%"])
group1 = pd.read_csv("python期末报告/Mp_WA.csv", delimiter="\t").groupby('类别')
n1 = 0
n2 = 0
lst = []
for k,v in group1:
    cols = set()
    rows = set()
    for el in v.values:
        rows.add(el[1])
        cols.add(el[2])
    Chi = pd.DataFrame(data=0,columns=list(cols),index=list(rows))
    for el in v.values:
        Chi.loc[el[1], el[2]] += 1
    chi,Pvalue,df,prob = chi2_contingency(Chi,correction=True, lambda_=None)
    lst.append([k,Pvalue])
    ct = stats.chi2.ppf(q=0.95,df=df)
    p = 1-stats.chi2.cdf(x=Pvalue,df=df)
    wr.writerow([k,str(Pvalue),str(df),ct >= p])
    if ct >= p:
        n1+=1
    else:
        n2+=1
file1.close()

R=np.random.randint(0,len(lst),size = 15)
for i in R:
    plt.barh(lst[i][0],lst[i][1])

plt.title("15个编程开发人员的组合需求（Mashup）与该需求所调用的服务（Web API）的卡方关联情况")
plt.ylabel("类别")
plt.xlabel("p值")
plt.savefig("python期末报告/15个编程开发人员的组合需求（Mashup）与该需求所调用的服务（Web API）的卡方关联情况.png",bbox_inches='tight')
plt.close()
plt.pie(x=[n1, n2], labels=["达成95%相关", "未达成95%相关"], autopct="%0.2f%%",colors = ['#9999ff', '#ff9999'])
plt.title("有95%可能性Mashup与API相关 vs.无95%可能性Mashup与API相关")
plt.rcParams['font.size'] = 25
plt.legend()
plt.savefig("python期末报告/是否95%可能性Mashup与API相关.png")
