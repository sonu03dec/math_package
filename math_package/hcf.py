# Python code to illustrate the Modules
class Hcf:
   
    # A normal print function
    def compute_hcf(x, y):

	# choose the smaller number
	    if x > y:
	        smaller = y
	    else:
	        smaller = x
	    for i in range(1, smaller+1):
	        if((x % i == 0) and (y % i == 0)):
	            hcf = i 
	    return hcf