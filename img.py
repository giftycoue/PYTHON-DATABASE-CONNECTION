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
        self.nav_frame = tk.Frame(master, bg="lightgray", height=30)
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Initialize a placeholder frame for pages
        self.current_page_frame = tk.Frame(master, bg="black")
        self.current_page_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Show the initial page (you can customize this based on your needs)
        self.show_page1()

    def show_page1(self):
        self.clear_current_page()
        page_label = tk.Label(self.current_page_frame, text="FOOD ALLERGEN DETECTOR", font=("Helvetica",20), bg="black", fg="white")
        page_label.pack(pady=20)

        # Add "Press Start" button
        start_button = tk.Button(self.current_page_frame, text="Press Start", command=self.start_detection, font=("Helvetica", 14), bg="green", fg="white")
        start_button.pack(pady=10)

    def start_detection(self):
        # Clear the screen
        self.clear_current_page()
        
    
        choice = print("ENTER YOUR CHOICE(1-19) FOR DETECTION:")
        user=input()
        
        hello_label = tk.Label(self.current_page_frame, text="CHOICE:", font=("Helvetica", 16), bg="black", fg="white")
        hello_label.pack(pady=10)

        # Print the list of foods
        foods = ["1.Rice", "2.Olive Oil", "3.Salmon", "4.Sweet Potato", "5.Avocado","6.Turkey","7.Blueberries","8.Quinoa","9.Wheat","10.Milk","11.Eggs","12.Fish","13.Mustard","14.Peanut","15.Shellfish","16.Sesame Seeds","17.Soy","18.Broccoli","19.Oats"]
        for food in foods:
            food_label = tk.Label(self.current_page_frame, text=food, font=("Helvetica", 12), bg="black", fg="white")
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
