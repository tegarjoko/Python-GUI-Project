from tkinter import *

class MenuUtama:
    def __init__(self,root):
        self.root = root
        root.geometry('700x500')
        root.title('Menu Utama')
        bg = PhotoImage(file='Menu.png')
        label1 = Label(root, image = bg)
        label1.place(x = 0, y = 0)

        #Tombol
        Button(root, text = 'Halo').grid(row=0, column=0)

if __name__ == '__main__':

    root = Tk()
    application = MenuUtama(root)
    root.mainloop()