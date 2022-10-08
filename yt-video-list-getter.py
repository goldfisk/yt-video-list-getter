import re
import csv

print('hello, members videos!')

with open('/Users/macbook/Projects/youtube-video-list-getter/concat-list1.txt') as video_list_file2:
    data = video_list_file2.read()

n = re.findall('watch\?v=(.*?)\\\\",', data)
#print(n)
n2 = re.findall('\}\]\},\\\\\"title\\\\\":\{\\\\\"runs\\\\\":\[\{\\\\\"text\\\\\":\\\\\\"(.*?)\\\\\"\}\]', data)
#print(n2)

# remove the random one which is not a video id
# and add rest of yt link
n1 = []
for x in n:
    if len(x)<=20:
        n1.append('https://www.youtube.com/watch?v='+x)

# put into 2d array and trim off extra titles
arr1 = [n1, n2[5:]]

# flip array diagonally so spreadsheet will be right way around
arr2 = list(zip(*arr1[::-1]))

# remove duplicates (eg if video posted then sent again as a community message)
arr3 = []
for x in arr2:
    if x not in arr3:
        arr3.append(x)

#write to csv
with open('/Users/macbook/Projects/youtube-video-list-getter/output5.csv', 'w+') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(arr3)
