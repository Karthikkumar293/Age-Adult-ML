import pandas as pd
import numpy as np

np.random.seed(42)
ages = np.random.randint(1, 81, size=1000)
adults = (ages >= 18).astype(int)

df2 = pd.DataFrame({
    'Age': ages,
    'Adult': adults
})

# Print without index
print(df2.head(10).to_string(index=False))
# --taken data set from ai--#

df2.head(1000)
df2.isnull()

import matplotlib.pyplot as mlt
import seaborn as sns
sns.scatterplot(x="Age",y="Adult",data=df2)

# supratting x and y
x=df2[["Age"]]
y=df2["Adult"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LogisticRegression

karthik2=LogisticRegression()
karthik2.fit(x_train,y_train)

#karthik2.predict(x_test)
age_input = float(input("enter your age"))
karthik2.predict([[age_input]])

#karthik2.score(x_test,y_test)*100
#output(100.0)%
