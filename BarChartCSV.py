import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file into a pandas dataframe
df = pd.read_csv('Random(log(1-x)).csv')

# Create a bar chart using Matplotlib
plt.bar(df['Range'], df['Frequency'])
plt.xlabel('Range')
plt.ylabel('Frequency')
plt.title('Bar Chart')
plt.show()