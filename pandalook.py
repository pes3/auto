import pandas as pd


df = pd.DataFrame(dict(A=[5,3,5,6,6,6,6], C=["foo","bar","fooXYZbar", "bat","rat","rat","fat"]))


df2 = pd.DataFrame(dict(A=["XYZ","ABC","EFg","6","foo"], C=["test","bar","testABC", "ba6t","ets"]))

l=df2['A'].unique().tolist()
reg='|'.join(l)
print (df[df['C'].str.contains(reg)==False])
