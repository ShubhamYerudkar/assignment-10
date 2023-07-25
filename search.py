import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry widget
entry = tk.Entry(root, font=("Calibri (Body)", 30), width=30)
entry.grid(row=0, column=0)

l1 = tk.Label(root, font=("Calibri (Body)", 20))
l1.grid(row=1, column=0)
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text="Navigating to yahoo...")        
        wb.open(f"https://www.yahoo.com/search?q={search}")
    else:
        print("Invalid input")

search_button = tk.Button(root, text="Search", font=("Calibri (Body)", 20),bg="white", activebackground="white", command=display)
search_button.grid(row=3, column=0)

close_button = tk.Button(root, text="Close", font=("Calibri (Body)", 20),bg="white", activebackground="white", command=root.destroy)
close_button.grid(row=6, column=0)
root.mainloop()