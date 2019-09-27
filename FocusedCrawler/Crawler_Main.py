import Focused_Crawler as fc
import Crawler as c

print("\n\n\n--------------------------------------------------------------------------------")
print("Please select whether you want to do: ")
print("\n\n")
print("Type '1' for Focused Crawling")
print("Type '2' for Full Crawling")
print("\n\nNOTE: Enter one of the above two choices as a number(Integer).")
choice = int(input("Enter a number: "))
print("\n\n--------------------------------------------------------------------------------\n\n")
if(choice == 1):
	seed = input("\nEnter Seed URL: ")
	key = input("\nEnter the Keyword: ")
	print("\n\nStarting...\n\n")
	fc.initiate(seed, key)

elif(choice == 2):
	seed = input("\nEnter Seed URL: ")
	print("\n\nStarting...\n\n")
	c.initiate(seed)
else:
	print("\n\nInvalid Input. Please run the program again!")


print("\n\n--------------------------------------------------------------------------------\n\n")