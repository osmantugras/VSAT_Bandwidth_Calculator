import tkinter as tk

def calculate_bandwidth():
    # Retrieve input values from the entry fields
    fec_rate = float(fec_rate_entry.get())
    data_rate = float(data_rate_entry.get())
    modulation_order = float(modulation_order_entry.get())
    roll_off_factor = float(roll_off_factor_entry.get())

    # Calculate the symbol rate
    symbol_rate = data_rate / (modulation_order * fec_rate)
    
    # Calculate the bandwidth in MHz
    bandwidth = (symbol_rate * (1 + roll_off_factor)) / 1000
    
    # Update the symbol rate and bandwidth labels with the results
    symbol_rate_label.config(text=f"Symbol Rate: {symbol_rate} Msps")
    bandwidth_label.config(text=f"Bandwidth: {bandwidth} MHz")
    
# Create the main application window
window = tk.Tk()
window.title("VSAT Bandwidth Calculator")

# Create labels and entry fields
fec_rate_label = tk.Label(window, text="FEC Rate (0.5-0.95):")
fec_rate_label.pack()

fec_rate_entry = tk.Entry(window)
fec_rate_entry.pack()

data_rate_label = tk.Label(window, text="Data Rate (kbps):")
data_rate_label.pack()

data_rate_entry = tk.Entry(window)
data_rate_entry.pack()

modulation_order_label = tk.Label(window, text="Modulation Order (1:BPSK, 2:QPSK, 3:8PSK, 4:16QAM, 6:64QAM):")
modulation_order_label.pack()

modulation_order_entry = tk.Entry(window)
modulation_order_entry.pack()

roll_off_factor_label = tk.Label(window, text="Roll-off Factor (0.20-0.50):")
roll_off_factor_label.pack()

roll_off_factor_entry = tk.Entry(window)
roll_off_factor_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_bandwidth)
calculate_button.pack()

# Create the symbol rate and bandwidth labels
symbol_rate_label = tk.Label(window, text="Symbol Rate:")
symbol_rate_label.pack()

bandwidth_label = tk.Label(window, text="Bandwidth:")
bandwidth_label.pack()

# Start the application loop
window.mainloop()
