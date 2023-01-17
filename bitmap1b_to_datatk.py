from PIL.BmpImagePlugin import BmpImageFile;
from tkinter import Tk, Canvas, BitmapImage, Message, Button, Text, Frame, Scrollbar;
from tkinter.filedialog import *


def GetBitmapFromImage(filename):
    fp = open(filename, "rb");
    
    img = BmpImageFile(fp=fp);
    img.load()

    bt = img.tobitmap();
    fp.close();
    img.close();

    return "BITMAP = \"\"\""+bt.decode()+"\"\"\"";
    

root = Tk();
root.geometry("420x220");

Message(root, width=400,
text="Convert image .BMP monochromatic (1bits) into a string data for Tkinter").grid(
    column=0,row=0);


bitmap = None;
def convert(filename):
    global bitmap;
    
    txtResult.delete("0.0", "end");

    try:
        BITMAP = GetBitmapFromImage(filename);
    except:
        txtResult.insert("0.0", "Error in conversion");
        return;
    
    bitmap = BitmapImage(data=BITMAP, foreground="white", background="black");
    
    c.configure(width=bitmap.width()+2, height=bitmap.height()+2);
    b = c.create_image(1, 1, image=bitmap, anchor="nw");
    #print("BITMAP = \"\"\""+BITMAP+"\"\"\"");

    txtResult.insert("0.0", BITMAP);
    


def selImg():
    #browse image
    fname = askopenfilename(parent=root, title="Select image BMP", filetypes=(("Image bmp 2 bits", "*.bmp"),));

    if fname:
        convert(fname);


def copy():
    string = txtResult.get("0.0", "end");
    
    root.clipboard_clear();
    root.clipboard_append(string);

    

c = Canvas(root, highlightthickness=0, relief="solid", bd=1, width=50, height=50);
c.grid(column=0, row=1);


Button(root, text="Select Image..", command=selImg).grid(column=0, row=2);


frameResult = Frame(root, width=10, height=10);
frameResult.columnconfigure((0,), weight=1);
frameResult.rowconfigure(0, weight=1);

txtResult = Text(frameResult, wrap="char");
txtResult.insert("0.0", "Result here");
sby = Scrollbar(frameResult, orient="vertical");
txtResult.grid(column=0, row=0, sticky="swne");
sby.grid(column=1, row=0, sticky="sn");

Button(frameResult, text="Copy", command=copy).grid(column=0, row=2, sticky="sn");

frameResult.grid(column=0, row=3);

root.columnconfigure(0, weight=1);
root.rowconfigure((0,1,2), weight=1);
root.rowconfigure(3, weight=30);


root.mainloop();


