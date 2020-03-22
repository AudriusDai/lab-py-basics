# write - overrides the content
# append - apparently appends ;D

appendMe = 'New bit of information!'

appendFile = open('exampleFile.txt', 'a')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()
