from textblob import TextBlob

file1=open("input.text", "r+") # write your file name here For example- demo.txt
a=file1.read()

print("Original Text: "+str(a))

b=TextBlob(a)

print("Corrected Text: "+str(b.correct()))

d=open("demo.text", "w") # write your file name here For example- corrected.txt
d.write(str(b.correct()))
d.close()

