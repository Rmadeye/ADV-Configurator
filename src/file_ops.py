from tkinter import filedialog


class BrowsersAndCollectors:
    def browse_receptor():
        global recfile
        recfile = filedialog.askopenfilename(filetypes=[("Receptor file", "*.pdbqt")])
        print("Receptor chosen:", recfile)
        Label1 = Label(window, text=recfile).grid(row=0, column=1)
        return recfile

    def browse_flexres():
        global flexfile
        flexfile = filedialog.askopenfilename(filetypes=[("Flexible residues file", "*.pdbqt")])
        print("Receptor chosen:", flexfile)
        Label2 = Label(window, text=flexfile).grid(row=1, column=1)
        return flexfile

    def browse_ligand():
        global ligfile
        ligfile = filedialog.askopenfilename(filetypes=[("Ligand file", "*.pdbqt")])
        print("Ligand chosen:", ligfile)
        Label3 = Label(window, text=ligfile).grid(row=2, column=1)
        return ligfile

    def collect_data():
        global outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname
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
        return outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename
