#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename:
# Author:    E-mail:qingant@gmail.com
# Lisence: GPL-2.0 
from  Tkinter import *
import os

def main():
    root = Tk()
    def run():
        os.system(entry.get()+' &')
        root.quit()
        pass
    entry=Entry(root,width=20)
    entry.pack()
    entry.focus()
    entry.bind('<Return>',(lambda event:run()))
    entry.bind('<Tab>',(lambda event:root.quit()))
    root.mainloop()



if __name__=='__main__' :
    main()
