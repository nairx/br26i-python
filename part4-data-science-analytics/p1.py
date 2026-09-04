import pandas as pd
data = {'Year': [2020, 2021, 2022, 2023],
        'Sales': [150, 200, 250, 300]}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales Growth')
plt.show()