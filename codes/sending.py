import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil

def open_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_paths:
        if len(file_paths) > 5:
            messagebox.showerror("Error", "You can only select up to 5 images.")
        else:
            try:
                # Copy each selected file to the data sharing folder
                destination = "data"  # Replace with the path to your data sharing folder
                for file_path in file_paths:
                    shutil.copy(file_path, destination)
                messagebox.showinfo("Success", "Files saved in data sharing folder!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save files: {str(e)}")

# Create the Tkinter window
root = tk.Tk()
root.title("Save Images to Data Sharing Folder")
root.geometry("500x400")  # Set window size to 300x200 pixels

# Create a button for selecting multiple image files
select_button = tk.Button(root, text="Select Images (Up to 5)", command=open_files)
select_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
