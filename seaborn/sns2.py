#seaborn using AI

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.DataFrame({
#     "Dept": ["IT", "HR", "IT", "Sales"],
#     "Salary": [20000, 30000, 25000, 40000]
# })

# sns.barplot(x="Dept", y="Salary", data=df, hue='Dept')

# plt.title("Salary by Department")

#heatmap

df = sns.load_dataset('tips')
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True)

#pairplot

# sns.pairplot(df)

#barplot

# sns.barplot(data=df, x='day', y='total_bill')

#histogram

# sns.histplot(df['total_bill'],kde=True)

# sns.countplot(data=df, x='day')

# sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)

sns.regplot(x="total_bill", y="tip", data=df)

plt.show()
