import filesImports as fi

root = fi.tkinter.Tk()
root.geometry("300x400")
root.title("url shortener")
root.configure(bg="#333333")

frame = fi.tkinter.Frame(bg="#333333")

def run():
    resultEntry.insert(0, fi.func.shorten(longUrlEntry.get()))

headerLabel = fi.tkinter.Label(frame, text="Shortener URL", bg="#333333", fg="white", font=("arial", 15))
headerLabel.grid(row="0", column="0", columnspan="2", sticky="news", pady="40")

longUrlLabel = fi.tkinter.Label(frame, text="Enter long URL", fg="#FFFFFF", bg="#333333", font=("arial", 12))
longUrlLabel.grid(row="1", column="0")

longUrlEntry = fi.tkinter.Entry(frame, width=35)
longUrlEntry.grid(row="2", column="0")

shortedUrlLabel = fi.tkinter.Label(frame, text="Result", fg="#FFFFFF", bg="#333333", font=("arial", 12))
shortedUrlLabel.grid(row="3", column="0")

resultEntry = fi.tkinter.Entry(frame, width=35)
resultEntry.grid(row="4", column="0")

startBtn = fi.tkinter.Button(frame, text="Start", bg="#F12", fg="#FFF", width="15", command=run)
startBtn.grid(row="5", column="0", pady="10")

frame.pack()
root.mainloop()

# https://www.youtube.com/watch?v=NvzIGaEOKCk&list=PLs3IFJPw3G9IiHm9PEP1UaMtuvACmxVMj&index=2