import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def receive_updates(client_socket, text_widget):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print("[DEBUG] Received update from server:", data)
                text_widget.config(state=tk.NORMAL)
                text_widget.delete(1.0, tk.END)
                text_widget.insert(tk.END, data)
                text_widget.config(state=tk.DISABLED)
        except Exception as e:
            print("[ERROR] An error occurred while receiving updates:", e)
            break

def on_text_change(event, client_socket, text_widget):
    text_widget.edit_modified(True)  # Set modified flag
    text_widget.after(200, lambda: send_update(client_socket, text_widget))  # Delayed update to avoid excessive sending

def send_update(client_socket, text_widget):
    text = text_widget.get(1.0, tk.END)  # Get the entire content
    client_socket.send(text.encode('utf-8'))

# Setup client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter server IP address: ")
port = int(input("Enter server port: "))
client_socket.connect((host, port))
print("[INFO] Connected to server.")

# Setup GUI
root = tk.Tk()
root.title("Collaborative Text Editor")

text_widget = ScrolledText(root, wrap=tk.WORD)
text_widget.pack(expand=True, fill=tk.BOTH)
text_widget.bind("<KeyRelease>", lambda event: on_text_change(event, client_socket, text_widget))

# Start the thread to receive updates
receive_thread = threading.Thread(target=receive_updates, args=(client_socket, text_widget))
receive_thread.start()

root.mainloop()
