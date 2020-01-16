from tkinter import *
from tkinter import filedialog
from src import create_cfg, file_ops

class frontend:

    def __init__(self):

        cc=create_cfg.ConfigMaker()
        fo=file_ops.BrowsersAndCollectors()
        window=Tk()
        window.wm_title("VinaConfigurator")

        try:
            window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file="icon.png"))
        except TclError:
            pass

        def exitwindow():
            window.destroy()

        # Label & Button list
        # Primary buttons - choice of pdbqt files

        Button1 = Button(window, text="Choose receptor", command=fo.browse_receptor).grid(row=0,
                                                                                                             column=0)
        Button2 = Button(window, text="Choose flexible residues ", command=fo.browse_flexres).grid(
            row=1, column=0)
        Button3 = Button(window, text="Choose ligand", command=fo.browse_ligand).grid(row=2,
                                                                                                         column=0)
        Label4 = Label(window, text="X coord").grid(row=3)
        xc = Entry(window)
        xc.grid(row=3, column=1)
        Label5 = Label(window, text="Y coord").grid(row=4)
        yc = Entry(window)
        yc.grid(row=4, column=1)
        Label6 = Label(window, text="Z coord").grid(row=5)
        zc = Entry(window)
        zc.grid(row=5, column=1)
        Label7 = Label(window, text="X dim").grid(row=6)
        xd = Entry(window)
        xd.grid(row=6, column=1)
        Label8 = Label(window, text="Y dim").grid(row=7)
        yd = Entry(window)
        yd.grid(row=7, column=1)
        Label9 = Label(window, text="Z dim").grid(row=8)
        zd = Entry(window)
        zd.grid(row=8, column=1)
        Label10 = Label(window, text="CPU number").grid(row=9)
        cpu = Entry(window)
        cpu.grid(row=9, column=1)
        Label11 = Label(window, text="Models (1-10k)").grid(row=10)
        mod_num = Entry(window)
        mod_num.grid(row=10, column=1)
        Label12 = Label(window, text="Energy range (kcal)").grid(row=11)
        er = Entry(window)
        er.grid(row=11, column=1)
        Label13 = Label(window, text="Output pdbqt and log filename").grid(row=12)
        outnameg = Entry(window)
        outnameg.grid(row=12, column=1)
        Label14 = Label(window, text="Config filename").grid(row=13)
        filenameg = Entry(window)
        filenameg.grid(row=13, column=1)
        Button15 = Button(window, text="Exit", command=exitwindow).grid(row=18, column=1)


        def utils():
            collect = Button(window, text="Collect data", command=fo.collect_data).grid(row=14, column=1)
            exe= Button(window, text="Save cfg file", command=cc.create_conf_file).grid(row = 15, column = 1)

            class collector:

                def collect_data(self):

                    def browse_receptor():
                        recfile = filedialog.askopenfilename(filetypes=[("Receptor file", "*.pdbqt")])
                        print("Receptor chosen:", recfile)
                        Label1 = Label(window, text=recfile).grid(row=0, column=1)
                        return recfile

                    def browse_flexres():

                        flexfile = filedialog.askopenfilename(filetypes=[("Flexible residues file", "*.pdbqt")])
                        print("Receptor chosen:", flexfile)
                        Label2 = Label(window, text=flexfile).grid(row=1, column=1)
                        return flexfile

                    def browse_ligand():

                        ligfile = filedialog.askopenfilename(filetypes=[("Ligand file", "*.pdbqt")])
                        print("Ligand chosen:", ligfile)
                        Label3 = Label(window, text=ligfile).grid(row=2, column=1)

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
                    print(outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename)
                    return create_cfg.ConfigMaker(outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename)
        window.mainloop()


