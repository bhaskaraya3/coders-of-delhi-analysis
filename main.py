import pandas as pd

data_excel = pd.read_excel("coders_of_delhi.xlsx")
df = data_excel

# average salary of python developers
py_devs = df[df["language"]=="Python"]
avg_sal_py = py_devs["salary"].mean()
print("Python : ",avg_sal_py)

# average salary of C++ developers
C_devs = df[df["language"]=="C++"]
avg_C_devs = C_devs["salary"].mean()
print("C++ : ",avg_C_devs)

# average salary of Javascript developers
JavaScript_devs = df[df["language"]=="JavaScript"]
avg_sal_JavaScript = JavaScript_devs["salary"].mean()
print("JavaScript : ",avg_sal_JavaScript)

# count of developers by language
count_devs = df["language"].value_counts()

#average salary of males and females
avg_sal_gen = df.groupby("gender")["salary"].mean()

#count gender
count_gender = df["gender"].value_counts()




