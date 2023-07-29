import os
import re
import tkinter as tk
import subprocess

def clone_sherlock_repository():
    if not os.path.exists("sherlock"):
        output_text.delete(1.0,tk.END)
        output_text.insert(tk.END,"\nCloning Repository ...")
        print("Cloning Repository ...")
        subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock.git"])
        output_text.insert(tk.END, "\nCloning Complete", "Sherlock repository cloned successfully!")
        print("Cloning Complete", "Sherlock repository cloned successfully!")
        os.chdir("sherlock")
        subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])
        os.chdir("..\\")


    else:
        output_text.delete(1.0, tk.END)
        #output_text.insert(tk.END, "\nStarting Execution!")
        #print("Start Execution!")
def run_sherlock(username):
    sherlock_script = os.path.abspath(os.path.join("sherlock/sherlock", "sherlock.py"))
    command = ["python", sherlock_script, "--timeout", "0.3", username]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command executed successfully.")
        print("Standard output:")
        print(result.stdout)

        output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result.stdout)
        output_text.insert(tk.END, output)
    else:
        print(f"Command failed with return code: {result.returncode}")
        print("Standard error:")
        print(result.stderr)

        output_text.insert(tk.END, f"Command failed with return code: {result.returncode}\n")
        output_text.insert(tk.END, "Standard error:\n")
        output_text.insert(tk.END, result.stderr)

def search_username():
    username = input_entry.get()
    if not username.strip():
        output_text.insert(tk.END, "\n >> Error: Username cannot be empty!","red")
        return
    else:
        print("\nSarching for \' "+username+" \'")
        output_text.delete(1.0, tk.END)
        run_sherlock(username)

if __name__ == "__main__":


    app = tk.Tk()
    app.title("Sherlock GUI")
    app.geometry("600x500")

    # Input entry field
    input_label = tk.Label(app, text="Enter Username:")
    input_label.pack()

    input_entry = tk.Entry(app)
    input_entry.pack()

    # Search button
    search_button = tk.Button(app, text="Search", command=search_username)
    search_button.pack()

    # Output text box
    output_text = tk.Text(app, height=25, width=90)
    output_text.pack()

    #color tags
    output_text.tag_configure("red", foreground="red")

    clone_sherlock_repository()

    app.mainloop()
