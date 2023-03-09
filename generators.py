#This program is made to demonstrate the working of Yield keyword...

def generator():

    for i in range(11):
        yield i


values = generator()
for i in values:
    print("Element: ", i)