#epoch = a date and time from which a computer measures system time. ie., when your computer thinks time began

import time

print(time.ctime(0)) #convert a time expressed in seconds since epoch to a readable string

print(time.ctime(1000000)) #if we pass in a value of 1,000,000, it will return a time 1M seconds since epoch

print(time.time()) #return current seconds since epoch

print(time.ctime(time.time())) #by passing in the number of seconds since epoch to the ctime we get the current date and time (basically epoch + seconds since epoch = current time)

time_object = time.localtime() #a time object is made up of a number of time arguments
print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #see the Python documentation for a listing of time format directives
print(local_time)

#Parse time from a string format to a time object
time_string = "20 April, 2023"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

#Create a string based on a time tuple
#(year, month, day, hours, minutes, seconds, #day of week, #day of year, dst)
time_tuple = (1975, 4, 25, 6, 53, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)
