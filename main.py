import matplotlib.pyplot as plt     # importing module 
try:                                # start of the try except block
	a = list(map(float,input('Enter the x axis inputs with space separated : ').split()))   # taking user input 
	b = list(map(float,input('Enter the y axis inputs with space separated : ').split()))
	if len(a) == len(b):
		plt.plot(a,b,color = 'green')   # plot along the a and b(user input) and selected color green
		plt.axis([0,max(a), 0, max(b)]) # selected axis upto the greatest value of the list
		plt.show()                      # for showing the final result 
	else :
		print('X axis input must be equal to Y axis input.')
except ValueError:
	print('Please enter a number.')   # if user input any charecter then it will excute
	
