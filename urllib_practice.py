import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#why these two for loop cannot be processed at the same time?

#counts = dict()
#for line in fhand:
#    words = line.decode().split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#print(counts)
