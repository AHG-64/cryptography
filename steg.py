#!/bin/python3
import sys
from PIL import Image
from math import*
#()10 -----> ()2
def dec2bin(x):
	remainders = []
	binaryNumber = ''
	while x > 0:
		remainders.append(x%2)
		x = x//2
	remainders.reverse()
	for digit in range(len(remainders)):
		binaryNumber += str(remainders[digit])
	return binaryNumber
  
#()2 ------> ()10
def bin2dec(x):
	decimalNumber = 0
	listBinaryNumber = []
	binaryNumber = str(x)
	for digit in range(len(binaryNumber)):
		listBinaryNumber.append(binaryNumber[digit])
	listBinaryNumber.reverse()
	for digit in range(len(listBinaryNumber)):
		decimalNumber += int(pow(2,digit) * int(listBinaryNumber[digit]))
	return str(decimalNumber)

#(string) ------> (binary)
def str2bin():
	pass
#(binary) ------> (string)
def bin2str():
	pass

def setLSB(n,t):
	if t==0:
		if n%2==0:
			return n
		return n-1
	else:
		if n%2==0:
			return n+1
		return n

def encode(message,pix,width,height):
	code=str2bin(message)
	Point=0
	while point<len(code):
		i=point%width
		j=point//width
		temp=list(pix[i,j])
		temp[0]=setLSB(temp[0],int(code[p]))
		pix[i,j]=tuple(temp)
		point+=1
	# key
	# n8b : num of 8bits
	n8b=dec2bin(point//8).zfill(10)
	counter=0
	point=height*width-1
	while counter<10:
		i=point%width
		j=point//width
		temp=list(pix[i,j])
		temp[0]=setLSB(temp[0],int(n8b[counter]))
		pix[i,j]=tuple(temp)
		counter+=1
		point-=1
	print('completed!')
def decode():
	pass

def main(args):
	option=args[1]
	image=Image.open(args[2])
	pix=image.load()
	if option=='-e':
		print('Enter your message:')
		encode(sys.stdin.read(),pix,image.size[0],image.size[1])
		image.save('coded.png')
	elif option=='-d':
		print(decode())
if __name__=='__main__':
	main(sys.argv)
