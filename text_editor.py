import datetime
import webbrowser
from tkinter import *
from tkinter import colorchooser, filedialog
# original source: https://gist.github.com/Enrix835/115589


def about():
    ab = Toplevel(root)
    txt = "This Python texteditor is an improved version of an outdated, \
italian Python 2 Github project. The maintainer of this current \
internationalized version is Felix."
    la = Label(ab, text=txt, foreground='blue')
    la.pack()


def background():
    (triple, color) = colorchooser.askcolor()
    if color:
        text.config(background=color)


def bold():
    text.config(font=("Arial", textsize, "bold"))


def clear():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)


def clearall():
    text.delete(1.0, END)


def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def date():
    data = datetime.date.today()
    text.insert(INSERT, data)


def decrease_textsize():
    global textsize
    if textsize >= 7:
        textsize -= 2
    text.config(font=("Arial", textsize))


def font():
    (triple, color) = askcolor()
    if color:
        text.config(foreground=color)


def increase_textsize():
    global textsize
    if textsize <= 42:
        textsize += 2
    text.config(font=("Arial", textsize))


def italic():
    text.config(font=("Arial", textsize, "italic"))


def kill():
    root.destroy()


def normal():
    text.config(font=("Arial", textsize))


def opn():
    text.delete(1.0, END)
    file = open(filedialog.askopenfilename(), 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT, txt)


def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except Exception:
        tkMessageBox.showerror("Error")


def save():
    filename = filedialog.asksaveasfilename()
    if filename:
        alltext = text.get(1.0, END)
        open(filename, 'w').write(alltext)


def underline():
    text.config(font=("Arial", textsize, "underline"))


textsize = 13

root = Tk()
root.title("Python Texteditor von Felix")
menu = Menu(root)
filemenu = Menu(root)
root.config(menu=menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save as...", command=save)
filemenu.add_command(label="Open...", command=opn)
filemenu.add_separator()
filemenu.add_command(label="Clear", command=clearall)
# should ask to save first
filemenu.add_command(label="Quit", command=kill)

formatmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=formatmenu)
formatmenu.add_radiobutton(label='Increase textsize',
                           command=increase_textsize)
formatmenu.add_radiobutton(label='Decrease textsize',
                           command=decrease_textsize)
# should only change highlighed text not everything, fix this
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal', command=normal)
formatmenu.add_radiobutton(label='Bold', command=bold)
formatmenu.add_radiobutton(label='Underline', command=underline)
formatmenu.add_radiobutton(label='Cursive', command=italic)
formatmenu.add_separator()
formatmenu.add_command(label="Change background color...", command=background)

insmenu = Menu(root)
menu.add_cascade(label="Features", menu=insmenu)
insmenu.add_command(label="Paste todays date", command=date)

helpmenu = Menu(menu)
menu.add_cascade(label="?", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

# these are the start settings
text = Text(root, height=30, width=60, font=("Arial", 13))

scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)

text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
text.pack()

root.resizable(0, 0)
root.mainloop()
# gestures like ctrl-c, ctrl-z, ... should be implemented
# add option to change font

'''
most important update will come soon:

make changes to text only locally to highlighted text.
increase size? only increase the size of the currently highlighted text..

also fix that the font size jumps back to standard 13 when making text
bold, cursive or underlined
'''
