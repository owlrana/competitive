# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

# open the file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# find out the hour and make counts for it
count = 0
hour = dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        #print(line)
        words = line.split()
        full_times = words[5].split(':')
        time = full_times[0]
        hour[time] = hour.get(time, 0) + 1
        


print(hour)