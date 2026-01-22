import pandas as pd

data = {
    "user_id": [1, 2, 1, 3, 2],
    "name": ["Ala", "Bartek", "Ala", "Celina", "Bartek"],
    "amount": [100, 200, 150, 300, 50],
    "date": pd.to_datetime([
        "2024-01-01",
        "2024-01-03",
        "2024-02-01",
        "2024-02-15",
        "2024-03-01"
    ])
}

df = pd.DataFrame(data)
print(df)
print("#"*100)
# print(df.head())
# print(df.info())
# print(df.describe())
df.loc[df["name"]=="Bartek", "name"]="janusz"
# print(df[df["name"]=="Bartek","Janusz"])
print("&&&&&&&")
print(df.groupby("name")["amount"].min())
print("!!!!!!!!!!!")
df['dupa'] = "dupa1"
print(df)
