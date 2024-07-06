import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# Configure the API key for the generative AI model
genai.configure(api_key="AIzaSyBc-NEWMFUWZw0uhVoGSXq6K_CSC1Moo2g")

# Set up the generation configuration
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}

# Initialize the generative model
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

# Function to get a response from the model
def get_bot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Function to handle user input and generate response
def send_message(event=None):
    user_input = entry.get()
    if user_input.lower() in ['exit', 'quit']:
        root.quit()
    if user_input:
        chat_area.configure(state='normal')
        chat_area.insert(tk.END, f"USER: {user_input}\n")
        chat_area.configure(state='disabled')
        chat_area.yview(tk.END)
        
        bot_response = get_bot_response(user_input)
        chat_area.configure(state='normal')
        chat_area.insert(tk.END, f"BOT: {bot_response}\n\n")
        chat_area.configure(state='disabled')
        chat_area.yview(tk.END)
        
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Chat area (scrollable)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50)
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# User input entry
entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Bind the Enter key to send_message function
root.bind('<Return>', send_message)

# Start the main loop
root.mainloop()
