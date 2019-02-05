import datetime
from tkinter import (BOTH, colorchooser, filedialog, END, INSERT,
                     Label, Menu, Text, RIGHT, Scrollbar,
                     SEL_FIRST, SEL_LAST, Tk, Toplevel, Y)


def about():
    ab = Toplevel(root)
    txt = "This Python texteditor is programmed by Felix. \
I am a 21 year old CS student from Germany, I hope you enjoy \
using my Text Editor :D"
    la = Label(ab, text=txt, foreground='green')
    la.pack()


def background():
    (triple, color) = colorchooser.askcolor()
    if color:
        text.config(background=color)


def bold(e=None):
    global current_fontmode
    current_fontmode = "bold"
    text.config(font=(current_font, textsize, "bold"))


def change_font_arial(e=None):
    global current_font
    current_font = "Arial"
    if current_fontmode == "normal":
        text.config(font=(current_font, textsize))
    else:
        text.config(font=(current_font, textsize, current_fontmode))


def change_font_helvetica(e=None):
    global current_font
    current_font = "Helvetica"
    if current_fontmode == "normal":
        text.config(font=(current_font, textsize))
    else:
        text.config(font=(current_font, textsize, current_fontmode))


def change_font_timesnewroman(e=None):
    global current_font
    current_font = "Times New Roman"
    if current_fontmode == "normal":
        text.config(font=(current_font, textsize))
    else:
        text.config(font=(current_font, textsize, current_fontmode))


def clear():
    try:
        sel = text.get(SEL_FIRST, SEL_LAST)
        text.delete(SEL_FIRST, SEL_LAST)
    except Exception:
        return None


def clearall():
    text.delete(1.0, END)


def copy(e=None):
    try:
        text.clipboard_clear()
        text.clipboard_append(text.selection_get())
    except Exception:
        return None


def date():
    data = datetime.date.today()
    text.insert(INSERT, data)


def decrease_textsize(e=None):
    global textsize
    global current_fontmode
    if textsize >= 7:
        textsize -= 2
    if current_fontmode == "normal":
        text.config(font=(current_font, textsize))
    else:
        text.config(font=(current_font, textsize, current_fontmode))


def font():
    (triple, color) = askcolor()
    if color:
        text.config(foreground=color)


def highlight_all(e=None):
    text.tag_add('sel', '1.0', 'end')
    return "break"


def increase_textsize(e=None):
    global textsize
    global current_fontmode
    if textsize <= 42:
        textsize += 2
    if current_fontmode == "normal":
        text.config(font=(current_font, textsize))
    else:
        text.config(font=(current_font, textsize, current_fontmode))


def italic(e=None):
    global current_fontmode
    current_fontmode = "italic"
    text.config(font=(current_font, textsize, "italic"))


def kill():
    root.destroy()


def normal(e=None):
    global current_fontmode
    current_fontmode = "normal"
    text.config(font=(current_font, textsize))


def open_file(e=None):
    global opened_filename
    try:
        file = open(filedialog.askopenfilename(), 'r')
        if file != '':
            text.delete(1.0, END)
            txt = file.read()
            text.insert(INSERT, txt)
            opened_filename = file.name
    except Exception:
        return None


'''
isn't needed on most operating systems

def paste():
    try:
        selection = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, selection)
    except Exception:
        return None
'''


def save(e=None):
    if opened_filename == "":
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = text.get(1.0, END)
            open(filename, 'w').write(alltext)
    else:
        alltext = text.get(1.0, END)
        open(opened_filename, 'w').write(alltext)


def underline(e=None):
    global current_fontmode
    current_fontmode = "underline"
    text.config(font=(current_font, textsize, "underline"))


textsize = 13
opened_filename = ""
current_font = "Arial"
current_fontmode = "normal"

root = Tk()
root.title("Python Texteditor von Felix")
        
menu = Menu(root)
filemenu = Menu(root)
root.config(menu=menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save as...", command=save, accelerator="Ctrl-s")
root.bind('<Control-s>', save)
filemenu.add_command(label="Open...", command=open_file, accelerator="Ctrl-o")
root.bind('<Control-o>', open_file)
filemenu.add_separator()
filemenu.add_command(label="Copy selection", command=copy,
                     accelerator="Ctrl-c")
root.bind('<Control-c>', copy)
filemenu.add_command(label="Highlight text", command=highlight_all,
                     accelerator="Ctrl-a")
root.bind('<Control-a>', highlight_all)
filemenu.add_command(label="Clear selection", command=clear)
filemenu.add_command(label="Clear", command=clearall)
# should ask to save first, if saved should ask do u rly wanna quit?
filemenu.add_command(label="Quit", command=kill)

formatmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=formatmenu)
formatmenu.add_radiobutton(label='Increase textsize',
                           command=increase_textsize,
                           accelerator="Ctrl+")
root.bind('<Control-Key-plus>', increase_textsize)
formatmenu.add_radiobutton(label='Decrease textsize',
                           command=decrease_textsize,
                           accelerator="Ctrl-")
root.bind('<Control-Key-minus>', decrease_textsize)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Arial', command=change_font_arial)
formatmenu.add_radiobutton(label='Helvetica', command=change_font_helvetica)
formatmenu.add_radiobutton(label='Times New Roman',
                           command=change_font_timesnewroman)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal', command=normal, accelerator="Alt-n")
root.bind('<Alt-n>', normal)
formatmenu.add_radiobutton(label='Bold', command=bold, accelerator="Alt-b")
root.bind('<Alt-b>', bold)
formatmenu.add_radiobutton(label='Underline', command=underline,
                           accelerator="Alt-u")
root.bind('<Alt-u>', underline)
formatmenu.add_radiobutton(label='Italic', command=italic, accelerator="Alt-i")
root.bind('<Alt-i>', italic)
formatmenu.add_separator()
formatmenu.add_command(label="Change background color...", command=background)

insmenu = Menu(root)
menu.add_cascade(label="Features", menu=insmenu)
insmenu.add_command(label="Paste todays date", command=date)

helpmenu = Menu(menu)
menu.add_cascade(label="?", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

text = Text(root, height=30, width=60, font=(current_font, textsize))
scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
text.pack(fill=BOTH, expand=1)
root.resizable(True, True)
root.mainloop()
# add feature to change text color
