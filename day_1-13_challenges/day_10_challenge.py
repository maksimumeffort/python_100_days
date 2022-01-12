#calculator


#add
def add(a, b):
  return a + b 
#subtract
def subtract(a, b):
  return a - b
#multiply
def multiply(a, b):
  return a * b 
#divide
def divide(a, b):
  return a / b 

#dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

#recursion: having a function that calls itself
def calculator():
    
    num1 = float(input('What is the first number?: '))
    is_running = True
    while is_running:
        
        for op in operations:
          print(op)
        symbol = input('Pick an operation: ')
        
        num2 = float(input('What is the next number?: '))

        answer = operations[symbol](num1, num2)

        print(f'{num1} {symbol} {num2} = {answer}')
        
        new_game = input('Type \'y\' to continue calculating with 16, or type\'n\' to exit.: ')
        if new_game == 'n':
            is_running = False
            #function calling itself to keep the funciton running from the start
            calculator()
        else:
            num1 = answer

calculator()
        

