from tkinter import *
from tkinter import filedialog
from src import create_cfg, file_ops

class Application(Frame):


    def exit(self):
        self.quit()

    def browse_receptor(self):
        self.recfile = filedialog.askopenfilename(filetypes=[("Receptor file", "*.pdbqt")])
        self.rec_label = Label(self, text=str(self.recfile)).grid(row=0, column=1)

    def browse_flex(self):
        self.flex = filedialog.askopenfilename(filetypes=[("Flexible residues file", "*.pdbqt")])
        self.flex_label = Label(self, text=str(self.flex)).grid(row=1, column=1)

    def browse_ligand(self):
        self.lig = filedialog.askopenfilename(filetypes=[("Ligand file", "*.pdbqt")])
        self.lig_label = Label(self, text=str(self.lig)).grid(row=2, column=1)




    def create_widgets(self):
        self.button1 = Button(self, text="Choose receptor",
                         command=self.browse_receptor).grid(row=0, column=0)

        self.button2 = Button(self, text="Choose flexible residues",
                         command=self.browse_flex).grid(row=1, column=0)

        self.button3 = Button(self, text="Choose ligand",
                         command=self.browse_ligand).grid(row=2,column=0)

        self.label4 = Label(self, text="X coord").grid(row=3)

        self.xc = Entry(self)
        self.xc.grid(row=3, column=1)

        self.label5 = Label(self, text="Y coord").grid(row=4)

        self.yc = Entry(self)
        self.yc.grid(row=4, column=1)

        self.label6 = Label(self, text="Z coord").grid(row=5)

        self.zc = Entry(self)
        self.zc.grid(row=5, column=1)

        self.label7 = Label(self, text="X dim").grid(row=6)

        self.xd = Entry(self)
        self.xd.grid(row=6, column=1)

        self.label8 = Label(self, text="Y dim").grid(row=7)

        self.yd = Entry(self)
        self.yd.grid(row=7, column=1)

        self.label9 = Label(self, text="Z dim").grid(row=8)

        self.zd = Entry(self)
        self.zd.grid(row=8, column=1)

        self.label10 = Label(self, text="CPU number").grid(row=9)

        self.cpu = Entry(self)
        self.cpu.grid(row=9, column=1)

        self.label11 = Label(self, text="Models (1-10k)").grid(row=10)

        self.mod_num = Entry(self)
        self.mod_num.grid(row=10, column=1)

        self.label12 = Label(self, text="Energy range (kcal)").grid(row=11)

        self.er = Entry(self)
        self.er.grid(row=11, column=1)

        self.label13 = Label(self, text="Output pdbqt and log filename").grid(row=12)

        self.outnameg = Entry(self)
        self.outnameg.grid(row=12, column=1)

        self.label14 = Label(self, text="Config filename").grid(row=13)

        self.filenameg = Entry(self)
        self.filenameg.grid(row=13, column=1)

        self.exit_button = Button(self, text="Exit",
                                  command=self.exit).grid(row=18, column=1)

        self.collect_button = Button(self, text="Collect data",
                                     command=print("Henlo")).grid(row=14, column=1)

        self.execute_button = Button(self, text="Save cfg file",
                                     command=print("Henlo")).grid(row=15, column=1)




    def __init__(self):
        Frame.__init__(self, master = None)
        # apptools = ApplicationTools()
        self.pack()
        self.create_widgets()
        self.winfo_toplevel().title("Vina-DB")
        self.mainloop()


# class ApplicationTools(Application):
#
#
#     def exit(self):
#         self.quit()
