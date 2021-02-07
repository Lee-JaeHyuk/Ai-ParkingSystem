from pandas import Series, DataFrame
import pandas as pd
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

data = [[-4, -3, -2, -1], [1, 2, 3, 4]]
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
print(df)

