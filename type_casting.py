import pandas as pd

data = {
    "price": ["100", "200", "300"]
}

df = pd.DataFrame(data)

df["price"] = df["price"].astype(int)
print(df)

'''
Output :
   price
0    100
1    200
2    300

'''
