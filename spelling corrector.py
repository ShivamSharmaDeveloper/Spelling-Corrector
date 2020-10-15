from textblob import TextBlob

file1=open("write your file name here", "r+")
a=file1.read()

print("Original Text: "+str(a))

b=TextBlob(a)

print("Corrected Text: "+str(b.correct()))

d=open("write the same name here", "w") #For example- demo.txt
d.write(str(b.correct()))
d.close()

