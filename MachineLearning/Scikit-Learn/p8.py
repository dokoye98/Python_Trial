import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt

df =  pd.DataFrame([[11,2],[32,11],[11,32]],columns=("col1","col2"),index=("one","two","three"))

df1 =pd.DataFrame([[11,11,"yes"],[22,22,"no"],[11,11,"yes"]],columns=list("ABC"),index=list("DEF"))

df1[df1.loc[:,"C"]=="yes"]=1 
df1[df1.loc[:,"C"]=="no"]=0

mat1 = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

i1 = np.array([[2,2],[1,1]])
i2 = np.array([[2,1],[1,0]])

mat1[i1,i2] = np.array([[100,90],[50,40]])

arr = pd.DataFrame({"P1":[10,20,30],"P2":[["A","B","C"],["A","D","E"],["C","D","F"]]})
arr["P3"]= arr["P2"].apply(lambda x:" ".join(["_".join(i.split(" "))for i in x]))
print(arr["P3"])