import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

NashvilleHousing = pd.read_csv('/Users/miguelllorente/Downloads/Nashville Housing.csv').head(20)
NashvilleHousing

def show_data():
    x_axis = NashvilleHousing['SalePrice']
    y_axis = NashvilleHousing['SaleDate']
    bar_width = 0.6

    indices = np.arange(len(x_axis))

    plt.figure(figsize=(20, 6))

    plt.bar(indices, y_axis, width=bar_width)
    plt.title('Title Name')
    plt.xlabel('X-axis High')
    plt.ylabel('Y-axis Low')
    plt.xticks(indices, x_axis)

    plt.show()

show_data()
