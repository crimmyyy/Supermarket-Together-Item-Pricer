# Author - crimmyyy
# Name - Supermarket Together Item Pricer
# Date - August 12 - August 13th (last updated)
# Description - A Python script that reads and writes to a JSON file, storing information to keep track of original market values, along with the suggested price for them to be adjusted to.


# Import libraries
import json
import time  # For simulating a time delay for the progress bar
import sys

# The following script has only been confirmed to work with difficulty number 2. Feel free to adjust the calculations to your liking for the applicable mode you are playing on, and update the repository if the method is proven to work.

def print_progress_bar(iteration, total, prefix='', length=50, fill='█', print_end='\r'):
    """
    Print a progress bar to the console.
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()

def save_data_with_progress(data, filename):
    # Simulate a progress bar for saving data
    total_steps = 10  # Number of steps in progress bar
    for step in range(total_steps):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        time.sleep(0.1)  # Simulate a delay to visualize progress bar
        print_progress_bar(step + 1, total_steps, prefix=' Saving data...! ')

def display_data(filename):
    # Load and display data from the JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("\nStored Items:")
            print("-" * 40)
            for item in data:
                print(f"Name: {item['Name']}")
                print(f"Market Value: {item['Market Value']}")
                print(f"Suggested Price: {item['Final Price']}")
                print("-" * 40)
    except FileNotFoundError:
        print(" Error - No data found. The JSON file does not exist. ")

# Ask if the user wants to see the list printed from the JSON file at the beginning
initial_display_choice = input("Do you want to display the stored results before proceeding? (Y/N): ").strip().upper()
if initial_display_choice == 'Y'.upper():
    display_data('items.json')

while True:
    try:
        # Input for item name
        Item = input("Enter the item name: ").strip().upper()

        if Item == "N".upper():
            sys.exit()
        
        # Input for market value
        Diff2 = input("Market value price: ")
        print()
        
        # Convert input to float
        Diff2 = float(Diff2)
        print()
        
        # Perform calculation
        FinalTwo = (Diff2 * 2) - 0.5
        
        # Round FinalTwo to 2 decimal places
        FinalTwo = round(FinalTwo, 2)
        
        # Print the rounded result
        print("Final result:", FinalTwo)
        
        # Prepare data to be written to JSON
        ItemList = {
            "Name": Item,
            "Market Value": Diff2,
            "Final Price": FinalTwo
        }
        
        # Load existing data from the JSON file
        try:
            with open('items.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        
        # Add new item data
        data.append(ItemList)
        
        # Save data to the JSON file with a progress bar
        save_data_with_progress(data, 'items.json')
        
        print("Data saved successfully.")
        
        # Ask if the user wants to display the stored results
        display_choice = input("Do you want to display the stored results? (Y/N): ").strip().upper()
        
        if display_choice == 'Y'.upper():
            display_data('items.json')
    
    except ValueError:
        # Handle the case where conversion to float fails
        print("Invalid input. Please enter a numeric value.")
        print()  # Add a blank line for better readability
