# write - overrides the content
# append - apparently appends ;D

text = 'new stuff sample text to save\nNew line!'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()
