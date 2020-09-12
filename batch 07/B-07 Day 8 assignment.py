def getInput(calculate_arg_fun):
    def wrap_function():
        print("Hey people enter two numbers =")
        a = int(input("Enter your first Number - "))
        b = int(input("Enter your second Number - "))
        calculate_arg_fun(a,b)   
    return wrap_function
@getInput
def fibonacciSeries(x,y):
  
   while y<50:
     print(y)
     x,y = y,x+y
fibonacciSeries()


#assignment 2
try:
  file=open('sample.py','r')
  file.write('hi baby')
  file.close()
except Exception as e:
    print(e)



