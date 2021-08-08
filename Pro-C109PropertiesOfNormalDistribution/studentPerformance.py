from os import name
import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as pg

df=pd.read_csv("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C109PropertiesOfNormalDistribution/StudentsPerformance.csv")
list=df['reading score'].to_list()

mean=statistics.mean(list)
mode=statistics.mode(list)
median=statistics.median(list)
standard_deviation=statistics.stdev(list)

first_standard_deviation_start,first_standard_deviation_end=mean-standard_deviation, mean+standard_deviation
second_standard_deviation_start, second_standard_deviation_end=mean-(2*standard_deviation), mean+(2*standard_deviation)
third_standard_deviation_start,third_standard_deviation_end=mean-(3*standard_deviation), mean+(3*standard_deviation)

fig=ff.create_distplot([list],["Reading Scores"], show_hist=False)
fig.add_trace(pg.Scatter(x=[mean,mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pg.Scatter(x=[first_standard_deviation_start, first_standard_deviation_start], y=[0,0.17], name="1 STANDARD DEVIATION", mode="lines"))
fig.add_trace(pg.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0,0.17], name="1 STANDARD DEVIATION", mode="lines"))
fig.add_trace(pg.Scatter(x=[second_standard_deviation_start, second_standard_deviation_start], y=[0,0.17], name="2 STANDARD DEVIATION", mode="lines"))
fig.add_trace(pg.Scatter(x=[second_standard_deviation_end, second_standard_deviation_end], y=[0,0.17], name="2 STANDARD DEVIATION", mode="lines"))
fig.add_trace(pg.Scatter(x=[third_standard_deviation_start, third_standard_deviation_start], y=[0,0.17], name="3 STANDARD DEVIATION", mode="lines"))
fig.add_trace(pg.Scatter(x=[third_standard_deviation_end, third_standard_deviation_end], y=[0,0.17], name="3 STANDARD DEVIATION", mode="lines"))
fig.show()

list_of_data_with_1_standard_deviation=[result for result in list if result>first_standard_deviation_start and result<first_standard_deviation_end]
list_of_data_with_2_standard_deviation=[result for result in list if result>second_standard_deviation_start and result<second_standard_deviation_end]
list_of_data_with_3_standard_deviation=[result for result in list if result>third_standard_deviation_start and result<third_standard_deviation_end]

print("Mean of the data: ", mean)
print("Median of the data: ", median)
print("Mode of the data: ", mode)
print("Standard Deviation of the data: ", standard_deviation)

print("{}% is of data lies within 1 standard deviation".format(len(list_of_data_with_1_standard_deviation)*100.0/len(list)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_with_2_standard_deviation)*100.0/len(list)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_with_3_standard_deviation)*100.0/len(list)))