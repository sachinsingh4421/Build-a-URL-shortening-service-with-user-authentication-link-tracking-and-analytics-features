import tkinter as tk
from tkinter import messagebox
from utils import valid_url, name_available, add_url, get_url
import webbrowser

class URLShortenerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("URL Shortener")
        
        self.label_name = tk.Label(self, text="Short Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_url = tk.Label(self, text="URL:")
        self.label_url.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_url = tk.Entry(self)
        self.entry_url.grid(row=1, column=1, padx=10, pady=10)
        
        self.button_submit = tk.Button(self, text="Shorten URL", command=self.shorten_url)
        self.button_submit.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.label_redirect = tk.Label(self, text="Redirect using Short Name:")
        self.label_redirect.grid(row=3, column=0, padx=10, pady=10)
        
        self.entry_redirect = tk.Entry(self)
        self.entry_redirect.grid(row=3, column=1, padx=10, pady=10)
        
        self.button_redirect = tk.Button(self, text="Redirect", command=self.redirect_url)
        self.button_redirect.grid(row=4, column=0, columnspan=2, pady=10)
    
    def shorten_url(self):
        short_name = self.entry_name.get()
        url = self.entry_url.get()
        
        if 'http' not in url:
            url = f'http://{url}'
        
        if valid_url(url):
            if name_available(short_name) is None:
                add_url(short_name, url)
                messagebox.showinfo("Success", f"URL shortened successfully! Short name: {short_name}")
            else:
                messagebox.showerror("Error", "Short name not available")
        else:
            messagebox.showerror("Error", "Invalid URL")
    
    def redirect_url(self):
        short_name = self.entry_redirect.get()
        url = get_url(short_name)
        if url is None:
            messagebox.showerror("Error", "Invalid Short Name")
        else:
            webbrowser.open(url.url)

if __name__ == "__main__":
    app = URLShortenerApp()
    app.mainloop()
