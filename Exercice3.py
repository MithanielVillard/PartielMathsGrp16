import customtkinter as ctk
from customtkinter import CTkFrame

from Graph import Graph

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Curve Generator")
root.geometry("1200x800")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.configure(fg_color = "#222f3e")
root.update()

#-------------------------------------------
settings = ctk.CTkFrame(master=root, fg_color="#576574")
settings.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
settings.grid_propagate(False)

pos_text = ctk.CTkLabel(master=settings, text="", font=("Arial", 30))
pos_text.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

#Derivative ------------------------------------------------------
derivative_frame = CTkFrame(master=settings, fg_color="#576574")
derivative_frame.grid(row=1, column=0 , sticky="nsew", padx=20, pady=10)

derivative_text = ctk.CTkLabel(master=derivative_frame, text="f'(x) = ", font=("Arial", 25))
derivative_text.grid(row=0, column=0, sticky="nsew")

derivative_text_input = ctk.CTkEntry(master=derivative_frame, placeholder_text="", font=("Arial", 25), width=90)
derivative_text_input.grid(row=0, column=1, sticky="nsew")
#------------------------------------------------------------------

#Derivative Second-------------------------------------------------
derivative_second_frame = CTkFrame(master=settings, fg_color="#576574")
derivative_second_frame.grid(row=2, column=0 , sticky="nsew", padx=20, pady=10)

derivative_second_text = ctk.CTkLabel(master=derivative_second_frame, text="f''(x) = ", font=("Arial", 25))
derivative_second_text.grid(row=0, column=0, sticky="nsew")

derivative_second_text_input = ctk.CTkEntry(master=derivative_second_frame, placeholder_text="", font=("Arial", 25), width=86)
derivative_second_text_input.grid(row=0, column=1, sticky="nsew")
#------------------------------------------------------------------

plotframe = ctk.CTkFrame(master=root, fg_color="#576574")
plotframe.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(1, weight=2)

toolbar = ctk.CTkFrame(master=plotframe, fg_color="#222f3e", height=50)
toolbar.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

#Toolbar -------------------------------------------------

x_input_min = ctk.CTkEntry(master=toolbar, placeholder_text="taille axe x", font=("Arial", 25), width=80)
x_input_min.insert(0, "-10")
x_input_min.grid(row=0, column=1, padx=(0,5), pady=10, sticky="ns")

x_input_max = ctk.CTkEntry(master=toolbar, placeholder_text="taille axe x", font=("Arial", 25), width=80)
x_input_max.insert(0, "10")
x_input_max.grid(row=0, column=2, padx=(0,10), pady=10, sticky="ns")

y_input_min = ctk.CTkEntry(master=toolbar, placeholder_text="taille axe y", font=("Arial", 25), width=80)
y_input_min.insert(0, "-10")
y_input_min.grid(row=0, column=3, padx=(10,0), pady=10, sticky="ns")

y_input_max = ctk.CTkEntry(master=toolbar, placeholder_text="taille axe y", font=("Arial", 25), width=80)
y_input_max.insert(0, "10")
y_input_max.grid(row=0, column=4, padx=(5,5), pady=10, sticky="ns")
#---------------------------------------------------------

graph = Graph(plotframe, pos_text, derivative_text_input, derivative_second_text_input, x_input_min, x_input_max, y_input_min, y_input_max)

mirror_btn = ctk.CTkSwitch(master=toolbar, text="🪞", font=("Arial", 18), command=graph.on_mirror_click)
mirror_btn.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ns")

graph.update()

root.mainloop()
