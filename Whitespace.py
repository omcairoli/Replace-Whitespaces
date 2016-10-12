# Whitespace Program
# Method to replace all whitespaces with %20
# Written by: Oscar Cairoli
# Python 2.7


def main():

	print("Welcome! Hit Ctrl-C to quit program at any time.")
	print("")

	while(True):

		print("Enter a sentence with spaces: ")
		
		user_input = raw_input(">> ")
		space_filler = "%20"

		if ' ' in user_input:
			user_input = user_input.split(" ")
			newString = space_filler.join(user_input)
			print(newString)

		else:
			print("No spaces found in sentence!")
			print("")



if __name__ == "__main__":
	main()