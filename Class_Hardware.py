import pandas as pd
import matplotlib.pyplot as plt
data =pd.read_excel("/Users/lucyshichman/Desktop/MSDS-Orientation/MSDS-Orientation-Computer-Survey.xlsx")
# renaming columns
data =data.rename(columns={"Timestamp":"Timestamp",
                           'What is your uva net id? (e.g. mst3k)':"UVA_ID",
                           'What is your github user name?':"Github_ID",
                           'Operating System':"OS",
                           'CPU Cycle Rate (in GHz)':"CPU_Rate",
                           'CPU Number of Cores (int)':"CPU_Cores",
                           'RAM (in GB)':"RAM",
                           'Hard Drive Size (in GB)':"Hard_Drive",
                           'GPU (short description as a string)':"GPU_type",
                           'GPU CUDA Number of Cores (int)':"GPU_Cores"})
# deleting outlier row
data=data.drop(0)
# eliminate duplicate rows
data=data.drop_duplicates()

# Exploratory Analysis:

# Timestamp
plt.hist(data["Timestamp"])
plt.title('Distribution of Survey Submission Times')
plt.show()

# UVA_ID
print(data['UVA_ID'].count()) # 259 responses,
print(data["UVA_ID"].isna().sum()) # 61 NaN 

# Github_ID
print(data['Github_ID'].count()) # 243 responses,
print(data["Github_ID"].isna().sum()) # 77 NaN 

# OS
data['OS'] = data['OS'].apply(lambda x: "Windows" if x == 'Windows 10' else x)
data['OS'] = data['OS'].apply(lambda x: "Multiple" if x == 'Windows (by professional necessity), MacOS (by personal choice)' else x)
data['OS'] = data['OS'].apply(lambda x: "Multiple" if x == 'I use Mac and Linux' else x)
data['OS'] = data['OS'].apply(lambda x: "Multiple" if x == 'All of the above' else x)
data['OS'] = data['OS'].apply(lambda x: "Linux" if x == 'Any Linux' else x)

data["OS"].value_counts()

plt.hist(data['OS'])
plt.title('Distribution of Operating Systems')
plt.show()

# CPU_Rate
print(data["CPU_Rate"].dtype)

plt.hist(data['CPU_Rate'], bins=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
plt.xlim(0,5) # excluding outliers
plt.title('Distribution of CPU Cycle Rate (in GHz)')
plt.show()

# CPU_Cores
print(data["CPU_Cores"].unique())
plt.hist(data["CPU_Cores"])
plt.title("Distribution of Number of CPU Cores")
plt.show()

# RAM
print(data["RAM"].unique())
plt.hist(data["RAM"])
plt.title("Distribution of RAM (in GB)")
plt.show()

# Hard_Drive
print(data["Hard_Drive"].unique())
plt.hist(data["Hard_Drive"])
plt.title("Distribution of Hard Drive Size (in GB)")
plt.show()

# GPU_Type
print(data["GPU_type"].nunique()) # 196 different GPU descriptions given
print(data["GPU_type"].isna().sum()) # only 2 NaN responses

#GPU_Cores
print(data["GPU_Cores"].unique())
plt.hist(data["GPU_Cores"])
plt.title("Distribution of Number of GPU Cores")
plt.show()