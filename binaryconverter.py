import os

#Decimal -> Binary
def dec_to_bin(num):
	binary = bin(num)
	os.system("cls")
	return binary[2:]

#Binary -> Decimal
def bin_to_dec(num):
	decimal = int(num, 2)
	os.system("cls")
	return decimal

#Decimal -> Hexadecimal
def dec_to_hex(num):
	hexadecimal = hex(num)
	os.system("cls")
	return hexadecimal[2:]

#Hexadecimal -> Decimal  
def hex_to_dec(num):
	decimal = int(num, 16)
	os.system("cls")
	return decimal

#Binary -> Hexadecimal
def bin_to_hex(num):
	decimal = int(num, 2)
	hexadecimal = hex(decimal)
	os.system("cls")
	return hexadecimal[2:]

#Hexadecimal -> Binary
def hex_to_bin(num):
	decimal = int(num, 16)
	binary = bin(decimal)
	os.system("cls")
	return binary[2:]

def main():
	os.system("cls")
	exit = False
	while not exit:
		print("Binary <==> Decimal <==> Hexadecimal Conversion Tool")
		print("1. Convert Decimal to Binary")
		print("2. Convert Binary to Decimal")
		print("3. Convert Decimal to Hexadecimal")
		print("4. Convert Hexadecimal to Decimal")
		print("5. Convert Binary to Hexadecimal")
		print("6. Convert Hexadecimal to Binary")
		print("7. Exit")
		choice = input(">> ")
		if choice == "1":
			value = input("Number: ")
			print(dec_to_bin(value))			
		elif choice == "2":
			value = input("Number: ")
			print(bin_to_dec(value))	
		elif choice == "3":
			value = input("Number: ")
			print(dec_to_hex(value))	
		elif choice == "4":
			value = input("Number: ")
			print(hex_to_dec(value))	
		elif choice == "5":
			value = input("Number: ")
			print(bin_to_hex(value))	
		elif choice == "6":
			value = input("Number: ")
			print(hex_to_bin(value))	
		elif choice == "7":
			exit = True
		else:
			os.system("cls")
			print("Enter correct input type")
	
if __name__ == "__main__":
	main()
