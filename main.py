import pandas as pd
df1 = pd.read_csv('1.csv')

print(df1.head())
print(df1.info())
print(df1.describe())

df = pd.read_csv('dz.csv')


try:
    data_dict = {}
    for index, row in df.iterrows():
        key = row.iloc[1]
        value = row.iloc[2]
        if pd.notna(value):
            if key in data_dict:
                data_dict[key].append(value)
            else:
                data_dict[key] = [value]
    for i in data_dict:
        print(f'Средняя зарплата в городе {i} - {sum(data_dict[i])/len(data_dict[i])}')

except:
    print(0)

