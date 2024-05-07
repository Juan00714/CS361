import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

beam_images = {
    "Beam 1": "beam1.png",
    "Beam 2": "beam2.png"
}

def calculate_results():
    # Display message indicating that results are being computed
    results_text.config(state=tk.NORMAL)
    results_text.delete("1.0", tk.END)
    results_text.insert(tk.END, "Results are being computed. Please wait...\n")
    results_text.config(state=tk.DISABLED)
    
    # Add a delay of 5 seconds
    time.sleep(5)
    
    # Retrieve values entered by the user
    E_value = float(E_entry.get())  # Convert to float since it's a decimal value
    I_value = float(I_entry.get())
    L1_value = float(L1_entry.get())
    L2_value = float(L2_entry.get())
    l1_value = float(l1_entry.get())
    l2_value = float(l2_entry.get())
    P_value = float(P_entry.get())
    W_value = float(W_entry.get())
    w_value = float(w_entry.get())
    x_value = float(x_entry.get())

    # Placeholder calculations
    max_shear = E_value + I_value
    max_moment = 5000
    max_deflection = 0.25
    shear_at_location = 800
    moment_at_location = 4000
    deflection_at_location = 0.2
    
    # Display results
    results_text.config(state=tk.NORMAL)
    results_text.insert(tk.END, f"Max shear: {max_shear} lbs\n")
    results_text.insert(tk.END, f"Max moment: {max_moment} lbf-ft\n")
    results_text.insert(tk.END, f"Max deflection: {max_deflection} inches\n\n")
    results_text.insert(tk.END, f"@ Location x:\n")
    results_text.insert(tk.END, f"Shear: {shear_at_location} lbs\n")
    results_text.insert(tk.END, f"Moment: {moment_at_location} lbf-ft\n")
    results_text.insert(tk.END, f"Deflection: {deflection_at_location} inches\n")
    results_text.config(state=tk.DISABLED)

def save_option():
    spans = spans_var.get()
    loads = loads_var.get()
    beam_type = beam_type_var.get()
    beam_index = beam_type_options.index(beam_type)
    
    # Section 3 - Inputs
    E = E_entry.get()
    I = I_entry.get()
    L1 = L1_entry.get()
    L2 = L2_entry.get()
    l1 = l1_entry.get()
    l2 = l2_entry.get()
    P = P_entry.get()
    W = W_entry.get()
    w = w_entry.get()
    x = x_entry.get()
    
    # Here you can save the selected options and inputs to a file or perform calculations
    messagebox.showinfo("Saved", f"Step 1 - Number of spans: {spans}\nType of loads: {loads}\nStep 2 - Type of beam: {beam_type}\n\nSection 3 - Inputs:\nE: {E} psi\nI: {I} inches^4\nL1: {L1} ft\nL2: {L2} ft\n(l1): {l1} inches\n(l2): {l2} inches\nP: {P} lbs\nW: {W} lbs\nw: {w} lbs/in\nx: {x} inches saved successfully!")

def update_image(selected_beam):
    selected_beam = beam_type_var.get()
    image_path = beam_images[selected_beam]
    img = Image.open(image_path)
    img = img.resize((200, 200))  # Resize the image as needed
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection

def lock_inputs():
    # If spans is 1, disable L2_entry and l2_entry
    if spans_var.get() == "1":
        L2_entry.config(state=tk.DISABLED)
        l2_entry.config(state=tk.DISABLED)
    else:
        L2_entry.config(state=tk.NORMAL)
        l2_entry.config(state=tk.NORMAL)

def clear_all():
    # Display confirmation message before clearing inputs
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to clear all inputs?")
    if confirm:
        # Clear all entry fields
        E_entry.delete(0, tk.END)
        I_entry.delete(0, tk.END)
        L1_entry.delete(0, tk.END)
        L2_entry.delete(0, tk.END)
        l1_entry.delete(0, tk.END)
        l2_entry.delete(0, tk.END)
        P_entry.delete(0, tk.END)
        W_entry.delete(0, tk.END)
        w_entry.delete(0, tk.END)
        x_entry.delete(0, tk.END)
        
        # Lock or unlock inputs based on the number of spans
        lock_inputs()

def spans_dropdown_changed(*args):
    # Lock or unlock inputs based on the number of spans
    lock_inputs()

# Create the main window
root = tk.Tk()
root.title("Form")

# Step 1
step1_frame = tk.LabelFrame(root, text="Step 1", padx=10, pady=10)
step1_frame.pack(padx=10, pady=10, fill="both", expand="yes")

spans_label = tk.Label(step1_frame, text="Number of spans:")
spans_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spans_options = ["1", "2"]
spans_var = tk.StringVar(root)
spans_var.set(spans_options[0])
spans_var.trace("w", spans_dropdown_changed)  # Call spans_dropdown_changed whenever spans_var changes
spans_dropdown = tk.OptionMenu(step1_frame, spans_var, *spans_options)
spans_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")

loads_label = tk.Label(step1_frame, text="Type of loads:")
loads_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
loads_options = ["Point", "Uniform", "Triangular"]
loads_var = tk.StringVar(root)
loads_var.set(loads_options[0])
loads_dropdown = tk.OptionMenu(step1_frame, loads_var, *loads_options)
loads_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Step 2
step2_frame = tk.LabelFrame(root, text="Step 2", padx=10, pady=10)
step2_frame.pack(padx=10, pady=10, fill="both", expand="yes")

beam_type_label = tk.Label(step2_frame, text="Type of beam:")
beam_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
beam_type_options = ["Beam 1", "Beam 2"]
beam_type_var = tk.StringVar(root)
beam_type_var.set(beam_type_options[0])
beam_type_dropdown = tk.OptionMenu(step2_frame, beam_type_var, *beam_type_options, command=lambda selected_beam: update_image(selected_beam))
beam_type_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Section 3 - Inputs
section3_frame = tk.LabelFrame(root, text="Section 3 (Inputs)", padx=10, pady=10)
section3_frame.pack(padx=10, pady=10, fill="both", expand="yes")

E_label = tk.Label(section3_frame, text="E (psi):")
E_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
E_entry = tk.Entry(section3_frame)
E_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

I_label = tk.Label(section3_frame, text="I (in^4):")
I_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
I_entry = tk.Entry(section3_frame)
I_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

L1_label = tk.Label(section3_frame, text="L1 (ft):")
L1_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
L1_entry = tk.Entry(section3_frame)
L1_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

L2_label = tk.Label(section3_frame, text="L2 (ft):")
L2_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
L2_entry = tk.Entry(section3_frame)
L2_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

l1_label = tk.Label(section3_frame, text="(l1) (in):")
l1_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
l1_entry = tk.Entry(section3_frame)
l1_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

l2_label = tk.Label(section3_frame, text="(l2) (in):")
l2_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
l2_entry = tk.Entry(section3_frame)
l2_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

P_label = tk.Label(section3_frame, text="P (lbs):")
P_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
P_entry = tk.Entry(section3_frame)
P_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

W_label = tk.Label(section3_frame, text="W (lbs):")
W_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
W_entry = tk.Entry(section3_frame)
W_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

w_label = tk.Label(section3_frame, text="w (lbs/in):")
w_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
w_entry = tk.Entry(section3_frame)
w_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

x_label = tk.Label(section3_frame, text="x (in):")
x_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
x_entry = tk.Entry(section3_frame)
x_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

# Placeholder calculations
max_shear = 1000
max_moment = 5000
max_deflection = 0.25
shear_at_location = 800
moment_at_location = 4000
deflection_at_location = 0.2

# Section 4 - Results
section4_frame = tk.LabelFrame(root, text="Section 4 (Results)", padx=10, pady=10)
section4_frame.pack(padx=10, pady=10, fill="both", expand="yes")

results_text = tk.Text(section4_frame, height=10, width=50)
results_text.pack()

# Initial image display
initial_image_path = "beam1.png"  # Set initial image path
initial_img = Image.open(initial_image_path)
initial_img = initial_img.resize((200, 200))
initial_photo = ImageTk.PhotoImage(initial_img)
image_label = tk.Label(section4_frame, image=initial_photo)
image_label.pack()

# Button to calculate results
calculate_button = tk.Button(root, text="Calculate Results", command=calculate_results)
calculate_button.pack()

# Create a button to save the selected options and inputs
save_button = tk.Button(root, text="Save", command=save_option)
save_button.pack()

# Create a button to clear all inputs
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack()

# Lock or unlock inputs based on the number of spans
lock_inputs()

# Run the main event loop
root.mainloop()
