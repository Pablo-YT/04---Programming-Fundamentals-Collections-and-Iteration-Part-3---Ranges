#If the number is a multiple of three, output the string "Bit". 
#For multiples of five, output "Maker".
#For numbers which are multiples of both three and five, output "BitMaker"
#Write a program that loops over the numbers from 1 to 100.




for n in range(1,101):
	while n <= 100:
		
		if n % 3 == 0 and n % 5 == 0:
			print("BitMaker")

		elif n % 3 == 0:
			print("Bit")

		elif n % 5 == 0:
			print("Maker")

		print(n)	
		n += 1

	else: 
		print('Goodbye') 
		break
