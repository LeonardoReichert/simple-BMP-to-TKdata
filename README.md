# simple-BMP-to-TKdata
Convert BMP 1 bit into Tkinter Data string | Convierte una imagen de BMP de 1 bit a una string para insertar en Tkinter

Beneficios: no se necesita portar el archivo de imagen, si no que se introduce la string en el codigo y listo.

![image](https://user-images.githubusercontent.com/95723749/212911114-144b36f8-346d-4bf8-b98e-365d3c12c0ae.png)


## Usar el resultado:

``` Python
from tkinter import Tk, Button, BitmapImage;


root = Tk();

BITMAP_EXAMPLE = """#define image_width 28
#define image_height 28
static char image_bits[] = {
0xff,0xff,0xff,0x0f,0xff,0x0f,0xfe,0x0f,0xff,0x21,0xf0,0x0f,0x7f,0xb6,0xcd,
0x0f,0xbf,0xbb,0xbb,0x0f,0x5f,0xbd,0x57,0x0f,0xef,0xbc,0xe3,0x0e,0xf7,0x02,
0xec,0x0d,0x77,0xbf,0xdf,0x0d,0x7b,0xbf,0xdf,0x0b,0x7b,0xbf,0xdf,0x0b,0xbb,
0xbf,0xbf,0x0b,0xbd,0xbf,0xbf,0x07,0xbd,0xbf,0xbf,0x07,0x01,0x00,0x00,0x00,
0xbd,0xbf,0xbf,0x07,0xbd,0xbf,0xbf,0x07,0xbb,0xbf,0xbf,0x0b,0x7b,0xbf,0xdf,
0x0b,0x7b,0xbf,0xdf,0x0b,0xf7,0xbe,0xdf,0x0d,0xf7,0x02,0xe8,0x0d,0xef,0xbc,
0xe7,0x0e,0x5f,0xbd,0x57,0x0f,0xbf,0xbb,0xbb,0x0f,0x7f,0xb6,0xcd,0x0f,0xff,
0x21,0xf0,0x0f,0xff,0x0f,0xfe,0x0f
};"""


bpExample = BitmapImage("example", data=BITMAP_EXAMPLE);
#bpExample need exists on reference global | bpExample necesita existir globalmente y no ser liberado

btnExample = Button(root, image=bpExample,compound="left",bd=1,overrelief="ridge",
                            relief="flat",cursor="hand2",
                            );

btnExample.pack()

root.mainloop();

```
