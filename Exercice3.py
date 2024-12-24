import customtkinter as ctk
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

plotframe = ctk.CTkFrame(master=root, fg_color="#576574")
plotframe.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(1, weight=2)

toolbar = ctk.CTkFrame(master=plotframe, fg_color="#222f3e", height=50)
toolbar.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

graph = Graph(plotframe)
graph.update()
#----------------------------------------------

root.mainloop()