import customtkinter as ctk

def on_click(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Curve Generator")
root.geometry("1200x800")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(fg_color = "#222f3e")
root.update()

#-------------------------------------------
settings = ctk.CTkFrame(master=root, fg_color="#576574")
settings.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")

plotframe = ctk.CTkFrame(master=root, fg_color="#576574")
plotframe.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
plotframe.columnconfigure(0, weight=1)
plotframe.rowconfigure(0, weight=1)

root.mainloop()