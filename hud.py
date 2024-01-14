import customtkinter
from customtkinter import *
import player

# Complete visual settings of programme

# Resolution and interface of programme
aplictaion = CTk()
aplictaion.geometry("600x600")
state = "Play"
set_appearance_mode("dark")

# Buttons functions and placement

button = customtkinter.CTkButton(aplictaion, text=state, command=player.state_of_music)
button.place(anchor="center", relx=0.5, rely=0.6)
button2 = customtkinter.CTkButton(aplictaion, text="End", command=player.end)
button2.place(anchor="center", relx=0.5, rely=0.7)
button3 = customtkinter.CTkButton(aplictaion, text="Choose music, that you want to play", command=player.add_music)
button3.place(anchor="center", relx=0.5, rely=0.8)
aplictaion.mainloop()
