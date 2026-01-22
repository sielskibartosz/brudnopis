import pandas as pd

data = {
    "order_id": [1, 2, 3, None, 5, 6],
    "product": ["Jabłko", "Pomarańcza", "Chleb", "Jogurt", "Jabłko", "Masło"],
    "category": ["Owoce", "Owoce", "Pieczywo", "Nabiał", "Owoce", "Nabiał"],
    "quantity": [10, 5, 2, 7, 3, 1],
    "price_per_item": [2.5, 3.0, 4.5, 3.5, 2.5, 7.0],
    "order_date": [
        "2023-07-01",
        "2023-07-02",
        "2023-07-02",
        "2023-07-03",
        "2023-07-03",
        "2023-07-04",
    ],
}

df = pd.DataFrame(data)
df["order_date"] = pd.to_datetime(df["order_date"])

print(df)
print("%%%%%%%%%%%")

df["total_price"]= df['quantity']*df['price_per_item']
print(df)
print("calkowity przychod%%%%%%%%%%%%%%")
print(df.groupby('category')['total_price'].sum())

print("more than 5 ")
print(df[df['quantity']>5])
print("!!!!!!!!!!!!!!!!!!")
print(df.groupby('order_date').sum())
print(df.groupby('order_date')['order_id'].count())  # też liczba zamówień

print('*************')

