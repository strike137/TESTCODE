"""
**Input Prompt**: Generate Python code for the following: The code creates an array of strings called vehicles. 
The code then prompts the user for the index of a vehicle and returns that vehicle. The code then loops through the 
array and prints out each vehicle.

**Intention**: The purpose of this code is to allow the user to interactively select a vehicle from a predefined 
array of vehicles using an index, and subsequently print out all vehicles in the list.

**Functionality**: The code initializes an array of strings containing vehicle names. It then asks the user to input 
an index to select a vehicle. It checks if the input index is valid and returns the vehicle at that index, if valid. 
Finally, it iterates through the entire list of vehicles and prints each vehicle to the console.
"""
def main():
    vehicles = ["Car", "Bike", "Truck", "Van", "Bus"]

    try:
        index = int(input("Enter the index (0-4) of the vehicle you want to select: "))
        if 0 <= index < len(vehicles):
            print(f"Selected vehicle: {vehicles[index]}")
        else:
            print("Invalid index. Please enter a number between 0 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    print("All vehicles:")
    for vehicle in vehicles:
        print(vehicle)

if __name__ == "__main__":
    main()