# it comes with 3.x out of the box. However in 2.x you have to use some thir party lib
import statistics

example_list = [3, 2, 3, 3, 2, 3, 5, 5, 4, 6, 5, 6, 5, 3]

mean = statistics.mean(example_list)
stdev = statistics.stdev(example_list)
median = statistics.median(example_list)

print('mean is ', mean)
print('standard deviation is ', stdev)
print('median is ', median)
