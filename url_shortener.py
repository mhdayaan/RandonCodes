from tkinter import *
import pyshorteners
import clipboard

windowOb = Tk()

# Set default window size
windowOb.geometry("500x300") 

# Make window size fixed 
windowOb.resizable(False,False)

# Give Title to app
windowOb.title("URL SHORTENER")

# Create an url input field
urlIP = Entry(windowOb, font=("Arial", "20")) 
urlIP.grid(row=1,column=2,pady=10)

#Label shortened
stringUrl = StringVar(windowOb)
shortUrl = Label(windowOb, textvariable=stringUrl, font=("Arial", "20"), fg="#fff", bg="#1abc9c")
shortUrl.grid(row=3, column=2, pady=10)

# copy function
def copy_url():
    try:
        clipboard.copy(stringUrl.get())
        print("Url copied!!")
    except:
        stringUrl.set("Something went wrong...")    
# copy button
copy_button = Button(windowOb, text="Copy", highlightbackground='green', fg="black", font=("Arial", "20"), activebackground="red", command=copy_url)
copy_button.grid(row=3, column=3, pady=10, padx=4)

# short_Url function
def short_Url():
    try:
        s = pyshorteners.Shortener()
        url = urlIP.get()
        final=s.tinyurl.short(url)
        stringUrl.set(final)
        urlIP.delete(0, END)
    except:
        stringUrl.set("Enter Url")



# Button
button = Button(windowOb, text="Shorten Url", padx=8, pady=4, highlightbackground='#24A0ED', fg="black", font=("Arial", "20"), activebackground="red", command=short_Url)
button.grid(row=2, column=2, pady=10)

windowOb.mainloop()