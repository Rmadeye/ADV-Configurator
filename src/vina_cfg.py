from tkinter import *
from tkinter import filedialog
from src import create_cfg, file_ops

class Application(Frame):
    
    def create_widgets(self):
        fo = file_ops.BrowsersAndCollectors()
        Button1 = Button(self, text="Choose receptor", command=fo.browse_receptor).grid(row=0,
                                                                                                             column=0)
        Button2 = Button(self, text="Choose flexible residues ", command=fo.browse_flexres).grid(
            row=1, column=0)
        Button3 = Button(self, text="Choose ligand", command=fo.browse_ligand).grid(row=2,
                                                                                                         column=0)
        Label4 = Label(self, text="X coord").grid(row=3)
        xc = Entry(self)
        xc.grid(row=3, column=1)
        Label5 = Label(self, text="Y coord").grid(row=4)
        yc = Entry(self)
        yc.grid(row=4, column=1)
        Label6 = Label(self, text="Z coord").grid(row=5)
        zc = Entry(self)
        zc.grid(row=5, column=1)
        Label7 = Label(self, text="X dim").grid(row=6)
        xd = Entry(self)
        xd.grid(row=6, column=1)
        Label8 = Label(self, text="Y dim").grid(row=7)
        yd = Entry(self)
        yd.grid(row=7, column=1)
        Label9 = Label(self, text="Z dim").grid(row=8)
        zd = Entry(self)
        zd.grid(row=8, column=1)
        Label10 = Label(self, text="CPU number").grid(row=9)
        cpu = Entry(self)
        cpu.grid(row=9, column=1)
        Label11 = Label(self, text="Models (1-10k)").grid(row=10)
        mod_num = Entry(self)
        mod_num.grid(row=10, column=1)
        Label12 = Label(self, text="Energy range (kcal)").grid(row=11)
        er = Entry(self)
        er.grid(row=11, column=1)
        Label13 = Label(self, text="Output pdbqt and log filename").grid(row=12)
        outnameg = Entry(self)
        outnameg.grid(row=12, column=1)
        Label14 = Label(self, text="Config filename").grid(row=13)
        filenameg = Entry(self)
        filenameg.grid(row=13, column=1)
        Button15 = Button(self, text="Exit", command=print("exit")).grid(row=18, column=1)
        collect = Button(self, text="Collect data", command=fo.collect_data).grid(row=14, column=1)
        exe = Button(self, text="Save cfg file", command=cc.create_conf_file).grid(row=15, column=1)
        # Label1 = Label(self, text=fo.recfile).grid(row=0, column=1)
        # Label2 = Label(self, text=fo.flexfile).grid(row=1, column=1)#"""Do widgets"""
        # Label3 = Label(self, text=fo.ligfile).grid(row=2, column=1)#"""Do widgets"""
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.winfo_toplevel().title("Vina-DB")
        self.mainloop()

    # def __init__(self):
    # 
    #     cc=create_cfg.ConfigMaker()
    #     fo=file_ops.BrowsersAndCollectors()
    #     self=Tk()
    #     self.wm_title("VinaConfigurator")
    # 
    #     try:
    #         self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file="icon.png"))
    #     except TclError:
    #         pass
    # 
    #     def exitself():
    #         self.destroy()
    # 
    #     # Label & Button list
    #     # Primary buttons - choice of pdbqt files




        def utils():
            collect = Button(self, text="Collect data", command=fo.collect_data).grid(row=14, column=1)
            exe= Button(self, text="Save cfg file", command=cc.create_conf_file).grid(row = 15, column = 1)

            class collector:

                def collect_data(self):

                    def browse_receptor():
                        recfile = filedialog.askopenfilename(filetypes=[("Receptor file", "*.pdbqt")])
                        print("Receptor chosen:", recfile)
                        Label1 = Label(self, text=recfile).grid(row=0, column=1)
                        return recfile

                    def browse_flexres():

                        flexfile = filedialog.askopenfilename(filetypes=[("Flexible residues file", "*.pdbqt")])
                        print("Receptor chosen:", flexfile)
                        Label2 = Label(self, text=flexfile).grid(row=1, column=1)
                        return flexfile

                    def browse_ligand():

                        ligfile = filedialog.askopenfilename(filetypes=[("Ligand file", "*.pdbqt")])
                        print("Ligand chosen:", ligfile)
                        Label3 = Label(self, text=ligfile).grid(row=2, column=1)

                        return ligfile

                    outfile = recfile.strip(".pdbqt") + ligfile
                    logfile = recfile + ligfile + ".txt"
                    ox = xc.get()
                    oy = yc.get()
                    oz = zc.get()
                    dx = xd.get()
                    dy = yd.get()
                    dz = zd.get()
                    outname = outnameg.get()
                    ncpu = cpu.get()
                    nmod = mod_num.get()
                    energy = er.get()
                    filename = str(filenameg.get())
                    # print(outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename)
                    # return create_cfg.ConfigMaker(outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename)


