import os

def denary_to_binary(denary):
	value = []
	while (denary >= 1):
		value.append(denary % 2)
		denary = int(denary / 2)
	return value

def reverse_list(list):
	new_list = []
	for i in reversed(list):
		new_list.append(i)
	binary_num = ""
	for i in new_list:
		binary_num = binary_num + str(i)
	return binary_num

def full_num(num):
	os.system("cls")
	return reverse_list(denary_to_binary(num))

def binary_to_denary(num):
	total_sum = 0
	string = str(num)
	for i in range(1, len(string) + 1):
		current_val = int(num % (10 ** i) / (10 ** (i - 1)))
		total_sum = total_sum + (current_val * (2 ** (i - 1)))
	os.system("cls")
	return total_sum

def dec_to_hex(num):
	value = []
	while num >= 1:
		if num % 16 >= 10:
			if num % 16 == 10:
				value.append("A")
			elif num % 16 == 11:
				value.append("B")
			elif num % 16 == 12:
				value.append("C")
			elif num % 16 == 13:
				value.append("D")
			elif num % 16 == 14:
				value.append("E")
			elif num % 16 == 15:
				value.append("F")		
		else:
			value.append(num % 16)
		num = int(num / 16)
	new_val = []
	for i in reversed(value):
		new_val.append(i)
	string = ""
	for i in new_val:
		string = string + str(i)
	os.system("cls")
	return string

def hex_to_dec(num):
	total_sum = 0
	current_place = len(num) - 1
	for i in num:
		if i == "A":
			current_val = 10
		elif i == "B":
			current_val = 11
		elif i == "C":
			current_val = 12
		elif i == "D":
			current_val = 13
		elif i == "E":
			current_val = 14
		elif i == "F":
			current_val = 15
		else:
			current_val = int(i)
		total_sum = total_sum + (current_val * (16 ** current_place))
		current_place = current_place - 1
	os.system("cls")
	return total_sum


def main():
	exit = False
	while not exit:
		print("Binary <==> Decimal Conversion Tool")
		print("1. Convert Decimal to Binary")
		print("2. Convert Binary to Decimal")
		print("3. Convert Decimal to Hexadecimal")
		print("4. Convert Hexadecimal to Decimal")
		print("5. Exit")
		choice = input(">> ")
		if choice == "1":
			val = int(input("Number: "))
			print(full_num(val))
		elif choice == "2":
			val = int(input("Number: "))
			print(binary_to_denary(val))
		elif choice == "3":
			val = int(input("Number: "))
			print(dec_to_hex(val))
		elif choice == "4":
			val = input("Number: ")
			print(hex_to_dec(val))
		elif choice == "5":
			exit = True
		else:
			os.system("cls")
			print("Enter correct input type")
	
if __name__ == "__main__":
	main()
