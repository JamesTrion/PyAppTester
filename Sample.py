import tkinter as tk
from tkinter import ttk

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import pylightxl as xl

from CustomLib import GeneralDefInfo
#from CustomLib import *

'''
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
'''

objCurParam=GeneralDefInfo.PrimaryParam(CenterFreq=700000)
print(objCurParam.CenterFreq)


def PlaceWndInTheCenter(wndTarget,width,height):
    # wndTarget:    window to be positioned
    # width:        window's width
    # height:       window's height
    screen_width=wndTarget.winfo_screenwidth()
    screen_height=wndTarget.winfo_screenheight()
    posLeft=int((screen_width-width)/2)
    posTop=int((screen_height-height)/2)
    wndTarget.geometry(f'{width}x{height}+{posLeft}+{posTop}')

window=tk.Tk()

window.title('Filter Application')

#position window in the center of screen
PlaceWndInTheCenter(window,800,500)

top_frame=ttk.Frame(window,width=800,height=130,relief=tk.GROOVE,borderwidth=10)
top_frame.pack_propagate(False)
top_frame.pack()

#create left pane label controls and positions
lblOrder=ttk.Label(top_frame,text='Order',anchor='e',justify='right')
lblCenterFreq=ttk.Label(top_frame,text='Center Freq',anchor='e',justify='right')
lblBandwidth=ttk.Label(top_frame,text='Bandwidth',anchor='e',justify='right')
lblSamplingFreq=ttk.Label(top_frame,text='Sampling Freq(fs)',anchor='e',justify='right')

lblOrder.place(x=41,y=8-5,width=107,height=21)
lblCenterFreq.place(x=41,y=36-5,width=107,height=21)
lblBandwidth.place(x=41,y=64-5,width=107,height=21)
lblSamplingFreq.place(x=41,y=92-5,width=107,height=21)

#create left pane entry controls and positions
orderVal=tk.StringVar()
orderVal.set(value=3)
CenterFreqVal=tk.StringVar()
CenterFreqVal.set(value=objCurParam.CenterFreq)
BandwidthVal=tk.StringVar()
BandwidthVal.set(value=20000)
fsVal=tk.StringVar()
fsVal.set(value=16000000)

entryOrder=ttk.Entry(top_frame,textvariable=orderVal,justify='right')
entryCenterFreq=ttk.Entry(top_frame,textvariable=CenterFreqVal,justify='right')
entryBandwidth=ttk.Entry(top_frame,textvariable=BandwidthVal,justify='right')
entryFS=ttk.Entry(top_frame,textvariable=fsVal,justify='right')

entryOrder.place(x=148+8,y=3,width=76,height=21)
entryCenterFreq.place(x=148+8,y=36-5,width=76,height=21)
entryBandwidth.place(x=148+8,y=64-5,width=76,height=21)
entryFS.place(x=148+8,y=92-5,width=76,height=21)

#create middle pane labels controls
lblDisturbRunTimes=ttk.Label(top_frame,text='Run Times',anchor='e',justify='right')
lblSignalStrength=ttk.Label(top_frame,text='Signal Strength',anchor='e',justify='right')
lblSignalStrengthN=ttk.Label(top_frame,text='Signal Strength N',anchor='e',justify='right')
lblProgress=ttk.Label(top_frame,text='Progress',anchor='e',justify='right')

lblDisturbRunTimes.place(x=274,y=8-5,width=107,height=21)
lblSignalStrength.place(x=274,y=36-5,width=107,height=21)
lblSignalStrengthN.place(x=274,y=64-5,width=107,height=21)
lblProgress.place(x=274,y=92-5,width=107,height=21)

#create middle pane entry controls
RunTimesVal=tk.StringVar()
RunTimesVal.set(value=10000)
SignalStrengthVal=tk.StringVar()
SignalStrengthVal.set(value=1)
SignalStrengthNVal=tk.StringVar()
SignalStrengthNVal.set(value=0.01)
ProgressVal=tk.StringVar()
ProgressVal.set(value=0)

entryRunTimes=ttk.Entry(top_frame,textvariable=RunTimesVal,justify='right')
entrySigStrength=ttk.Entry(top_frame,textvariable=SignalStrengthVal,justify='right')
entrySigStrengthN=ttk.Entry(top_frame,textvariable=SignalStrengthNVal,justify='right')
lblProgressPercentage=ttk.Label(top_frame,textvariable=ProgressVal,anchor='e',justify='right')

entryRunTimes.place(x=374+20,y=8-5,width=107,height=21)
entrySigStrength.place(x=374+20,y=36-5,width=107,height=21)
entrySigStrengthN.place(x=374+20,y=64-5,width=107,height=21)
lblProgressPercentage.place(x=374+20,y=92-5,width=107,height=21)

#create desc label controls
lblSigSTRDesc=ttk.Label(top_frame,text='( 0.1 ~ 1)')
lblNSigSTRDesc=ttk.Label(top_frame,text='( 0.001 ~ 1)')
lblPercentageSign=ttk.Label(top_frame,text='%')

lblSigSTRDesc.place(x=394+107+5,y=36-5,height=21)
lblNSigSTRDesc.place(x=394+107+5,y=64-5,height=21)
lblPercentageSign.place(x=394+107+5,y=92-5,height=21)

def RunButton_Click():
    if (CenterFreqVal=="" or str.isnumeric(CenterFreqVal)==False):
        return
    
    print('run button clicked')

#creat button control
btnRun=ttk.Button(top_frame,text='Run',command=RunButton_Click)
btnRun.place(x=618,y=45,width=75,height=25)




''' #marked by Trion on 2023/08/17
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)

def create_right_frame(container):

    #create left frame with controls
    frame=ttk.Frame(container)

    frame.columnconfigure(0,weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_left_frame(container):

    return frame

right_button_frame=create_right_frame(top_frame)
right_button_frame.grid(row=0,column=2)
'''

window.mainloop()