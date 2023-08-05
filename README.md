# Prodigy_Ds_Task1
Here's a breakdown of what the code does:

The code imports the necessary libraries: pandas for data manipulation and matplotlib.pyplot for data visualization.

The code loads an csv file named "Car_sales.csv" into a DataFrame using pd.read_excel(). The DataFrame will hold the data for the chart.

The code extracts the necessary data from the DataFrame for the bar chart. It assigns the values from the 'manufacturer' column to the variable x and the values from the 'sales' column to the variable y.

The code creates a new figure with a size of 10x6 inches using plt.figure(figsize=(15, 10)).

The code generates a bar chart using plt.bar(manufacturer, sales). It uses the x values as the labels for the x-axis and the y values as the heights of the bars.

The code customizes the chart by setting labels for the x-axis, y-axis, and title using plt.xlabel(), plt.ylabel(), and plt.title() respectively. The x-axis is labeled as 'Manufacturer', the y-axis as 'Sales_in_thousands', and the chart is titled 'Bar Chart'.

The code displays the chart using plt.show(), which will open a separate window or display the chart directly in a Jupyter Notebook or similar environment.
