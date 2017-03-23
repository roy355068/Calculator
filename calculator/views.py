from django.shortcuts import render
import math
# Create your views here.


digit = ["0","1","2","3","4","5","6","7","8","9"]
ops   = ['+', '-', '*', '/', '=']

def home(request):

	value = {"preVal": 0, "newVal": 0, "preOps": '+', 'display': 0}
	
	"""
	request.method is the method specified in the form tag of html
	request.POST is a dictionary using name attribute as key and the name value as value
	"""
	if request.method == "POST":
		for key in request.POST.keys():
			if key in digit:
				value = updateVal(request, key)
			elif key in ops:
				value = updateOps(request, key)
		
	return render(request, "calculator.html", value)


def updateVal(request, val):
	preVal = request.POST["preVal"]
	newVal = request.POST['newVal']
	preOps = request.POST['preOps']

	# Check if the preOps is equal sign, reset the preVal to 0 if yes
	if preOps == '=':
		preVal = 0
		preOps = "+"
	# end

	if newVal == "0":
		newVal = val
	else:
		newVal += val
	value = {'preVal': preVal, 'newVal': newVal, 'preOps': preOps, 'display': newVal}
	return value

def updateOps(request, val):
	try:
		x = int(request.POST["preVal"])
		y = int(request.POST['newVal'])
	except ValueError:
		value = {'preVal': 0, 'newVal': 0, 'preOps': "+", 'display': "Invalid number"}
		return value
	
	preOps = request.POST['preOps']

	if preOps != "=":
		display = 0
	else:
		display = x
	# In case !!!
	if preOps not in ops:
		display = "Invalid operation"
		value = {'preVal': 0, 'newVal': 0, 'preOps': "+", 'display': display}
		return value

	if preOps == "+":
		display = add(x, y)
	elif preOps == "-":
		display = sub(x, y)
	elif preOps == "*":
		display = mul(x, y)
	elif preOps == "/":
		display = divi(x, y)
		try:
			display = int(display)
		except ValueError:
			value = {'preVal': 0, 'newVal': 0, 'preOps': "+", 'display': display}
			return value
	
	value = {'preVal': display, 'newVal': 0, 'preOps': val, 'display': display}
	return value

	# if val == "=":
	# 	value = {'preVal': , 'newVal': 0, 'preOps': "=", 'display': display}
	# 	return value

	
# elementary arithmetics routines
def add(x, y):
	return x + y
def sub(x, y):
	return x - y
def mul(x, y):
	return x * y
def divi(x, y):
	if y == 0:
		return "Error, divided by 0"
	return int(math.floor(x / y))

