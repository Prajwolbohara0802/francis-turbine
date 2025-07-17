import tkinter as t
from tkinter import Menu as m

root = t.Tk()
root.title("Franics_turbine_optimization")
root.iconbitmap("francis.ico")


#creating the menu barm

menubar = m(root)
#geometry
root.geometry("600x400")


#all the decleration related with the file menu

def new_file():
    print("New file has benn created")

def exit_app():
    root.quit()


#file
file_menu = m(menubar,tearoff=0)
file_menu.add_command(label="New Project",command=new_file)
file_menu.add_command(label="Open")
file_menu.add_command(label="Load Last Project")
file_menu.add_command(label="Insert Project")
file_menu.add_command(label="Close Project")
file_menu.add_separator()
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File",menu=file_menu)

#all the declearation related with the module 
def close_all():
    print("close all_file and go to inital page")
def blade_desgin():
    print("blade desgin started")

#module
module_menu = m(menubar, tearoff=0)
module_menu.add_command(label="Close all",command=close_all)
module_menu.add_separator()
module_menu.add_command(label="Blade_Desgin_Dimension",command=blade_desgin)
module_menu.add_command(label="Axial_View")
module_menu.add_command(label="Distribution")
module_menu.add_command(label="Radial_View")
module_menu.add_command(label="Blade_Thickness")
module_menu.add_command(label="Labyrinths")
module_menu.add_command(label="Runner_cascade")
module_menu.add_separator()
module_menu.add_command(label="Summary")
menubar.add_cascade(label="Module",menu=module_menu)


# all the decleration related with the option menu
def pef_file():
    print(".......")
def restore_file():
    print("reotre file")
def reset_file():
    print("reset_file")

#option
option_menu = m(menubar,tearoff=0)
option_menu.add_command(label="Peference",command=pef_file)
option_menu.add_separator()
option_menu.add_command(label="Restore toolbar",command=restore_file)
option_menu.add_separator()
option_menu.add_command(label="Reset Default Setting",command=reset_file)
menubar.add_cascade(label="Option",menu=option_menu)
#all the decleration related with help men
def release_file():
    print("version1.0.0")
def about_file():
    print("Francis_turbine optimization software in IOE thapathali campus")

#help
help_menu = m(menubar,tearoff=0)
help_menu.add_command(label="Releas Note",command=release_file)
help_menu.add_command(label="About",command=about_file)
menubar.add_cascade(label="?",menu=help_menu)

root.config(menu=menubar,bg="black")
root.mainloop()




