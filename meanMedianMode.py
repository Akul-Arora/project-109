import csv
import statistics
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
data=df["StudentsPerformance"].tolist()

varmean=statistics.mean(data)
varmedian=statistics.median(data)
std_deviation=statistics.stdev(data)
print("temp mean value :-",varmean,varmedian,std_deviation)

first_standard_deviation_start, first_standard_deviation_end = varmean-std_deviation, varmean+std_deviation
second_standard_deviation_start, second_standard_deviation_end = varmean-(2*std_deviation), varmean+(2*std_deviation)
third_standard_deviation_start, third_standard_deviation_end = varmean-(3*std_deviation), varmean+(3*std_deviation)

thin_1_std_deviation=[result for result in data if result > first_standard_deviation_start and first_standard_deviation_end]
thin_2_std_deviation=[result for result in data if result > second_standard_deviation_start and second_standard_deviation_end]
thin_3_std_deviation=[result for result in data if result > third_standard_deviation_start and third_standard_deviation_end]