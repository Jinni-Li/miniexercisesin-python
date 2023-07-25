#PART 1 – API Exercise
# 1. Use this pokemon API (https://pokeapi.co/) in order to let a user give you a pokemon name and you then print the pokemon name, his type (electric, grass, etc.), his height and weight.
#2. Put that functionality into a graphical interface using tkinter or something else. Bonus point if you include the image of the pokemon and make it look like a pokedex.



import requests
import tkinter as tk

def get_pokemon_details():
  pokemon_name = entry.get().strip()
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
  response = requests.get(url) #get the data set

  if response.status_code == 200: # if everything works correctly do this
    pokemon_data = response.json() #get the data and transform it into a dictionary
    name = pokemon_data['name']
    types = [t['type']['name'] for t in pokemon_data['types']] #in case we have more than 1 types for a pokemon
    height = pokemon_data['height']
    weight = pokemon_data['weight']

    # widgets 
    name_label.config(text=f"Name: {name}")
    types_label.config(text=f"Type: {', '.join(types)}") #join all types a pokemon could have
    height_label.config(text=f"Height: {height}")
    weight_label.config(text=f"Weight: {weight}")


  else:
      # If the Pokemon details couldn't be retrieved, display an error message
    name_label.config(text="Pokemon not found.")
    types_label.config(text="")
    height_label.config(text="")
    weight_label.config(text="")

# Create the window
window = tk.Tk()
window.title("Pokedex")

# Create and place the widgets
label = tk.Label(window, text="Enter a Pokemon name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Search", command=get_pokemon_details)
button.pack()

#Allocate the informations
name_label = tk.Label(window, text="")
name_label.pack()

types_label = tk.Label(window, text="")
types_label.pack()

height_label = tk.Label(window, text="")
height_label.pack()

weight_label = tk.Label(window, text="")
weight_label.pack()

# Run the GUI window
window.mainloop()
