import tkinter
import numpy as np

root = tkinter.Tk()
root.title("Coordinate Converter")

# Create function(s)
def calculate_rx() :
    r = float(entry_r.get())
    t = float(entry_t.get())
    RX = (round(r*np.cos(t*(np.pi/180)), 3))
    label_result['text'] = f'{RX}'

def calculate_ty() :
    r = float(entry_r.get())
    t = float(entry_t.get())
    TY = (round(r*np.sin(t*(np.pi/180)), 3))
    label_result['text'] = f'{TY}'

def calculate_xr1() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    XR1 = (round(np.sqrt(x**2+y**2), 3))
    label_result['text'] = f'{XR1}'

def calculate_yt1() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    YT1 = (round(np.arctan(y/x)/(np.pi/180)), 3)
    label_result['text'] = f'{YT1}'

def calculate_xr2() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    XR2 = (round(np.sqrt(x**2+y**2), 3))
    label_result['text'] = f'{XR2}'

def calculate_yt2() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    YT2 = (round(np.arctan(y/x)/(np.pi/180)+2*np.pi), 3)
    label_result['text'] = f'{YT2}'

def calculate_xr3() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    XR3 = (round(-(np.sqrt(x**2+y**2)), 3))
    label_result['text'] = f'{XR3}'

def calculate_yt3() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    YT3 = (round(np.arctan(y/x)/(np.pi/180)-np.pi), 3)
    label_result['text'] = f'{YT3}'

def calculate_xr4() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    XR4 = (round(-(np.sqrt(x**2+y**2)), 3))
    label_result['text'] = f'{XR4}'

def calculate_yt4() :
    x = float(entry_x.get())
    y = float(entry_y.get())
    YT4 = (round(np.arctan(y/x)/(np.pi/180)+np.pi), 3)
    label_result['text'] = f'{YT4}'

# Create GUI
label_r = tkinter.Label(root, text="RADIUS : ")
label_r.grid(column=0, row=0)

entry_r = tkinter.Entry(root)
entry_r.grid(column=1, row=0)

label_t = tkinter.Label(root, text="THETA : ")
label_t.grid(column=0, row=1)

entry_t = tkinter.Entry(root)
entry_t.grid(column=1, row=1)

label_x = tkinter.Label(root, text="X-AXIS : ")
label_x.grid(column=0, row=2)

entry_x = tkinter.Entry(root)
entry_x.grid(column=1, row=2)

label_y = tkinter.Label(root, text="Y-AXIS : ")
label_y.grid(column=0, row=3)

entry_y = tkinter.Entry(root)
entry_y.grid(column=1, row=3)

rx_cal = tkinter.Button(root, text="R-X", command=calculate_rx)
rx_cal.grid(column=2, row=0)

ty_cal = tkinter.Button(root, text="T-Y", command=calculate_ty)
ty_cal.grid(column=3, row=0)

xr1_cal = tkinter.Button(root, text="XR1", command=calculate_xr1)
xr1_cal.grid(column=2, row=1)

yt1_cal = tkinter.Button(root, text="YT1", command=calculate_yt1)
yt1_cal.grid(column=3, row=1)

xr2_cal = tkinter.Button(root, text="XR2", command=calculate_xr2)
xr2_cal.grid(column=2, row=2)

yt2_cal = tkinter.Button(root, text="YT2", command=calculate_yt2)
yt2_cal.grid(column=3, row=2)

xr3_cal = tkinter.Button(root, text="XR3", command=calculate_xr3)
xr3_cal.grid(column=2, row=3)

yt3_cal = tkinter.Button(root, text="YT3", command=calculate_yt3)
yt3_cal.grid(column=3, row=3)

xr4_cal = tkinter.Button(root, text="XR4", command=calculate_xr4)
xr4_cal.grid(column=2, row=4)

yt4_cal = tkinter.Button(root, text="YT4", command=calculate_yt4)
yt4_cal.grid(column=3, row=4)

result = tkinter.Label(root, text="RESULT :")
result.grid(column=0, row=4)

label_result = tkinter.Label(root, text="")
label_result.grid(column=1, row=4)

root.mainloop()
