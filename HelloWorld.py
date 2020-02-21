print("Hello World")
abc=lambda a,b:a+b
c=abc(1,2)
print("c="+str(c))
a,b = 1,2
c=a if a<b else b
print(c)