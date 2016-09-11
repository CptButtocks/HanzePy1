from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
#filename = "C:\\Users\\RonOS\\Documents\\hanze 2.1 literatuur\\Assignments\\Python\\astronaut.txt";

def show_result():
    analyze_file(filename.get())


def analyze_file(filename):
    try:
        infile = open(filename, "r")
        counts = [0] * 65;
        #counts = infile.readline();
        for line in infile:
            count_letters(line, counts);

        infile.close()

        # show histogram
        histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                       "File " + filename + " does not exist")
        # count each letter in the string


def count_letters(line, counts):
    #result = [0] * 66;
    #a = 97
    for letter in line:
        if letter.isalpha():
            counts.insert((ord(letter) - 65), (counts[ord(letter) - 65] + 1));
    return


def open_file():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


def histogram(counts):
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts)

    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts,
                                (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10,
                           text=chr(i + ord('a')))


window = Tk()
window.title("Occurrence of Letters Histogram")

frame1 = Frame(window)  # frmae for histogram
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)  # frame for buttons
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=40, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=open_file).pack(side=LEFT)
Button(frame2, text="Show Result", command=show_result).pack(side=LEFT)

window.mainloop()
