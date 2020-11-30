g_5 = [1]
g_7 = [5, 3]
title = ["one", "two"]
lovely = "text goes here you know"

#word_count = g_5 + g_7 + title

#word_count = len(lovely.split())

#print(len(word_count))

#print(word_count)

#word_count = title.count
#print(len(title))

sourceFile=open('demo.txt', 'w')
print(lovely, file = sourceFile)
sourceFile.close()