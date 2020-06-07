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

def main():
	exit = False
	while not exit:
		print("Binary <==> Decimal Conversion Tool")
		print("1. Convert Decimal to Binary")
		print("2. Convert Binary to Decimal")
		print("3. Exit")
		choice = input(">> ")
		if choice == "1":
			val = int(input("Number: "))
			print(full_num(val))
		elif choice == "2":
			val = int(input("Number: "))
			print(binary_to_denary(val))
		elif choice == "3":
			exit = True
		else:
			os.system("cls")
			print("Enter correct input type")
	
if __name__ == "__main__":
	main()
