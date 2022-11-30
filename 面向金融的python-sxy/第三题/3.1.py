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

def f(path):
    with open(path,"r") as file:
        data = json.load(file)
        for v in data:
            if v!=None:
                ra = v['related_apis']
                for i in range(len(ra)):
                    if ra[i]!=None:
                        url_ = ra[i]['url']
                        if url_ not in edge.keys():
                            edge[url_]={}
                        for j in range(i+1,len(ra)):
                            if ra[j]!=None:
                                url__ = ra[j]['url']
                                if url__ not in edge[url_].keys():
                                    edge[url_][url__]=0
                                edge[url_][url__]+=1
                                if url__ not in edge.keys():
                                    edge[url__]={}
                                if url_ not in edge[url__].keys():
                                    edge[url__][url_]=0


edge = dict()
f("python期末报告/data/raw/api_mashup/active_mashups_data.txt")
f("python期末报告/data/raw/api_mashup/deadpool_mashups_data.txt")
num = 0
for k,v in group1:
    if num==5:
        break
    num+=1
    enum = dict()
    for el in v.values:
        if el[2] not in enum.keys():
            enum[el[2]]=0
        enum[el[2]]+=1
    lt = list(enum.items())
    for i in lt:
        plt.barh(i[0],i[1])
    plt.title("WebAPI使用次数")
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.ylabel("WebAPI名称")
    plt.xlabel(k+"的WebAPI使用次数")
    plt.savefig("python期末报告/"+k+"使用次数.png",bbox_inches='tight')
    plt.close()
    F = nx.Graph()
    l = len(lt)
    for i in range(l):
        for j in range(i+1,l):
            a = lt[i][0]
            b = lt[j][0]
            if a in edge.keys() and b in edge[a].keys():
                F.add_edge(a, b, weight=edge[a][b])
    position = nx.spring_layout(F)
    label = nx.get_edge_attributes(F, 'weight')
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams['figure.figsize'] = (15, 20)
    plt.rcParams['font.size'] = 40
    nx.draw(F, position, with_labels=True)
    nx.draw_networkx_edge_labels(F, position, edge_labels=label, font_weight='bold',fontsize=50)
    plt.savefig("python期末报告/"+k+"的无向图.png",bbox_inches='tight')
    plt.close()