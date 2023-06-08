import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    if ( 0.2*x-0.1 > abs(y-0.5)):
        return 0, 0, 1
    elif (x-0.5)**2 + (y-0.5)**2 <0.10 and \
       not ((x-0.6)**2 +( y-0.30)**2 < 0.005)\
       and 1:
        return 1, 1, 0
    else:
        return 0, 0, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
