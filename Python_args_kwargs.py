
 # 1. Default parameters.

# suppose you have a function which takes argument name. Now if you dont provide the name value while calling function it will throw error. So in order to deal with that error we can use default parameters. So what will happen is even if we dont pass the name parameter the default value will be picked.

def greet(name):
	print(f"Hello {name}")
	
greet(Bhargavi) 
greet() # throws error

 

def greet(name ='Guest'):
	print(f"Hello {name}")
	
greet(Bhargavi) 
greet()  # chooses default parameter

# 2. Positional arguments

# when we have multiple arguments/ parameters to be passed to a function. We can simply use *. It can be anything *bhar etc. but * args is standard practice in industry. So using *args we can pass multiple parameters without having to define it in the function.

def positional(*args):
	for i in args:
		print(i)
		
positional(1,2,3,4,"Bhargavi")

# 3. Keyword Arguments

# when we have many parameters but in the form of key value pairs then we can use this kwargs.

def keywords(*kwargs):
		for key,value in kwargs.items():
			print(f'{key}:{value}')

keywords(name ='Bhargavi', age =26, city = 'Dublin')

# We can combine the args and kwargs 

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')