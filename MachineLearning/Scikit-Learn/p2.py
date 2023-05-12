import pandas  as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.DataFrame([[np.nan,2,np.nan,0],
                   [3,4,np.nan,1],
                   [np.nan,np.nan,np.nan,5]],
                  columns=list("ABCD"))

df.cumsum(axis=1)
df.dropna(axis=1, how="all")
#print(df.dropna(axis=1, how="any"))

print(df.loc[:,"A"])