import tkinter as tk

class SimpleNavigationBarApp:
    def __init__(self, master):
        self.master = master
        master.title("FOOD ALLERGEN DETECTOR")

        # Set the background color to black
        master.configure(bg="black")

        # Create a Canvas widget for the background image
        self.canvas = tk.Canvas(master, width=600, height=300, bg="black")
        self.canvas.pack(side=tk.TOP)

        # Load the background image
        self.background_image = tk.PhotoImage(file="food.png")

        # Add the background image to the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Create and configure the navigation bar frame
        self.nav_frame = tk.Frame(master, bg="lightgray", height=17)
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Initialize a placeholder frame for pages
        self.current_page_frame = tk.Frame(master, bg="black")
        self.current_page_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create an empty list to store the retrieved foods
        self.food_list = []

        # Show the initial page (you can customize this based on your needs)
        self.show_page1()

    def show_page1(self):
        self.clear_current_page()
        page_label = tk.Label(self.current_page_frame, text="FOOD ALLERGEN DETECTOR", font=("Helvetica", 20), bg="black", fg="white")
        page_label.pack(pady=20)

        # Add "Press Start" button
        start_button = tk.Button(self.current_page_frame, text="Press Start", command=self.start_detection, font=("Helvetica", 11), bg="green", fg="white")
        start_button.pack(pady=10)

    def start_detection(self):
        # Clear the screen
        self.clear_current_page()

        # Add a text heading for the program
        heading_label = tk.Label(self.current_page_frame, text="Choices:", font=("Helvetica", 16), bg="black", fg="white")
        heading_label.pack(pady=20)

        # Simulate the retrieved data (you should replace this with your actual database query)
        retrieved_data = [
         (1, '1.Rice', 'ALLERGEN -FREE', True),
            (2, '2.Olive Oil', 'ALLERGEN -FREE', True),
            (3, '3.Salmon', 'ALLERGEN -FREE', True),
            (4, '4.Sweet Potato', 'ALLERGEN -FREE', True),
            (5, '5.Avocado', 'ALLERGEN -FREE', True),
            (6, '6.Turkey', 'ALLERGEN -FREE', True),
            (7, '7.Blueberries', 'ALLERGEN -FREE', True),
            (8, '8.Quinoa', 'ALLERGEN -FREE', True),
            (9, '9.Wheat', 'Common Allergens', False),
            (10, '10.Milk', 'Common Allergens', False),
            (11, '11.Eggs', 'Common Allergens', False),
            (12, '12.Fish', 'Common Allergens', False),
            (13, '13.Mustard', 'Common Allergens', False),
            (14, '14.Peanut', 'Common Allergens', False),
            (15, '15.Shellfish', 'Common Allergens', False),
            (16, '16.Sesame Seeds', 'Common Allergens', False),
            (17, '17.Soy', 'Common Allergens', False),
            (18, '18.Broccoli', 'ALLERGEN -FREE', True),
            (19, '19.Oats', 'ALLERGEN -FREE', True)
        ]

        # Extract food names and add them to the food_list
        for data in retrieved_data:
            food_names = [food.strip() for food in data[1].split('\n')]
            self.food_list.extend(food_names)

        # Print the list of foods
        for food in self.food_list:
            food_label = tk.Label(self.current_page_frame, text=food, font=("Helvetica",14), bg="black", fg="blue")
            food_label.pack()

    def clear_current_page(self):
        for widget in self.current_page_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNavigationBarApp(root)

    # Allow the window to be resizable
    root.resizable(True, True)

    root.mainloop()
