import tkinter as tk
import os

COUNTER_FILE = 'counter.txt'
OUTPUT_FILE = 'output.txt'

num_buttons = 24
num_columns = 3
num_rows = num_buttons // num_columns
ghostNames = ["Spirit", "Wraith", "Phantom",
             "Poltergeist", "Banshee", "Jinn",
             "Mare", "Revenant", "Shade",
             "Demon", "Yurei", "Oni",
             "Yokai", "Hantu", "Goryo",
             "Myling", "Onryo", "The Twins",
             "Raiju", "Obake", "The Mimic",
             "Moroi", "Deogen", "Thaye"]

mapNames = ["Tanglewood", "Edgefield", "Ridgeview", "Grafton", "Willow", "School", "Bleasdale",
            "Sunny Meadows", "Sunny Meadows Restricted", "Prison", "Maple Lodge", "Camp Woodwind"]
def load_counter():
    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, 'r') as file:
                return int(file.read().strip())
        except ValueError:
            return 0
    return 0

def save_counter(num):
    with open(COUNTER_FILE, 'w') as file:
        file.write(str(num))

def write_to_file(content):
    with open(OUTPUT_FILE, 'a') as file:
        file.write(content + "\n")

counter = load_counter()
evidence = "null"
map_name = "null"

def get_multiplier():
    # Get the text from the decimal entry field.
    decimal_text = decimal_entry.get().strip()
    try:
        # Try converting to float (this also allows integers).
        decimal_value = float(decimal_text)
        # Format the decimal value
        formatted_decimal = f"{decimal_value:.2f}"
    except ValueError:
        formatted_decimal = decimal_text

    return formatted_decimal

def update_counter_and_file(ghost):
    global counter, evidence, map_name
    # Get the text from the decimal entry field.
    formatted_decimal = get_multiplier()

    evidence = option1_var.get()
    map_name = option2_var.get()
    output_line = f"Game {counter} : {ghost} : Multiplier {formatted_decimal}x : {evidence} Evidence : {map_name}"
    write_to_file(output_line)

    counter += 1
    save_counter(counter)
    counter_label.config(text=f"Games Played: {counter}")

# Create the main window.
root = tk.Tk()
root.title("Phasmophobia data input")

# --- Top Frame for Options and Decimal Input ---
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# --- Evidence Buttons ---
option1_var = tk.StringVar(value="null")  # Default selection
option1_frame = tk.LabelFrame(top_frame, text="Evidence Amount")
option1_frame.grid(row=0, column=1, padx=10)
for i in range(0, 4):
    tk.Radiobutton(option1_frame, text=f"{i} Evidence", variable=option1_var, value=str(i)).pack(anchor="w")

# --- Map Buttons ---
option2_var = tk.StringVar(value="null")  # Default selection
option2_frame = tk.LabelFrame(top_frame, text="Map")
option2_frame.grid(row=0, column=0, padx=10)
for i in range(0, 12):  # 12 options
    tk.Radiobutton(option2_frame, text=f"{mapNames[i]}", variable=option2_var, value=str(mapNames[i])).pack(anchor="w")

# --- Decimal input field ---
input_frame = tk.Frame(top_frame)
input_frame.grid(row=1, column=1, padx=10)
decimal_label = tk.Label(input_frame, text="Enter Multiplier:")
decimal_label.pack()
decimal_entry = tk.Entry(input_frame, width=10)
decimal_entry.pack()

# Create a frame to hold the ghosts
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

for i in range(0, num_buttons):

    # Create a button with the appropriate label.
    btn = tk.Button(
        buttons_frame,
        text=f"{ghostNames[i]}",
        width=20,
        command=lambda idx=i: update_counter_and_file(ghostNames[idx])
    )
    # Position the button in the grid.
    row = i // num_columns
    col = i % num_columns
    btn.grid(row=row, column=col, padx=5, pady=5)



# Create and display a label for the counter.
counter_label = tk.Label(root, text=f"Games Played: {counter}", font=("Helvetica", 14))
counter_label.pack(pady=20)

# main loop
root.mainloop()
