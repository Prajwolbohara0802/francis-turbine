import tkinter as t
from tkinter import ttk
from tkinter import Menu as m
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Main Window ---
root = t.Tk()
root.title("Francis Turbine Optimization")
root.geometry("1000x700")
root.iconbitmap("francis.ico")

# --- Create Tabbed Notebook ---
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# --- Blade Design Tab ---
blade_tab = t.Frame(notebook)
notebook.add(blade_tab, text="Blade Design")

t.Label(blade_tab, text="Blade Angle (°):").grid(row=0, column=0, padx=10, pady=10)
angle_entry = t.Entry(blade_tab)
angle_entry.grid(row=0, column=1)

t.Label(blade_tab, text="Chord Length (cm):").grid(row=1, column=0, padx=10, pady=10)
chord_entry = t.Entry(blade_tab)
chord_entry.grid(row=1, column=1)

t.Label(blade_tab, text="Max Thickness (cm):").grid(row=2, column=0, padx=10, pady=10)
thick_entry = t.Entry(blade_tab)
thick_entry.grid(row=2, column=1)

result_label = t.Label(blade_tab, text="", fg="green")
result_label.grid(row=3, columnspan=2)

def render_foil_chart():
    try:
        angle = float(angle_entry.get())
        chord = float(chord_entry.get())
        thickness = float(thick_entry.get())

        x_vals = [i * chord / 10 for i in range(11)]
        y_vals = [thickness * 0.5 * (1 - ((2 * i / 10 - 1) ** 2)) for i in range(11)]

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x_vals, y_vals, label="Foil Profile", color="steelblue")
        ax.set_title("Blade Foil Visualization")
        ax.set_xlabel("Chord (cm)")
        ax.set_ylabel("Thickness (cm)")
        ax.grid(True)
        ax.legend()

        # Clear previous charts
        for widget in blade_tab.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        chart = FigureCanvasTkAgg(fig, master=blade_tab)
        chart.draw()
        chart.get_tk_widget().grid(row=5, columnspan=2, pady=10)
        result_label.config(text="Foil chart generated.", fg="green")

    except ValueError:
        result_label.config(text="Enter valid numeric values.", fg="red")

t.Button(blade_tab, text="Render Foil", command=render_foil_chart).grid(row=4, columnspan=2, pady=10)

# --- Distribution Tab Placeholder ---
dist_tab = t.Frame(notebook)
notebook.add(dist_tab, text="Distribution")
t.Label(dist_tab, text="Distribution analysis coming soon...").pack(pady=40)

# --- Axial View Tab Placeholder ---
axial_tab = t.Frame(notebook)
notebook.add(axial_tab, text="Axial View")
t.Label(axial_tab, text="Axial view visualization module in progress...").pack(pady=40)

# --- Menu Bar (Optional) ---
menubar = m(root)
root.config(menu=menubar)

# File Menu
file_menu = m(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.mainloop()