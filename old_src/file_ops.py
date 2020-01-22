from tkinter import filedialog


class BrowsersAndCollectors:

    def __init__(self):
        pass

    def browse_receptor(self):
        self.recfile = filedialog.askopenfilename(filetypes=[("Receptor file", "*.pdbqt")])
        print("Receptor chosen:", self.recfile)
        return self.recfile

    def browse_flexres(self):
        self.flexfile = filedialog.askopenfilename(filetypes=[("Flexible residues file", "*.pdbqt")])
        print("Receptor chosen:", self.flexfile)
        return self.flexfile

    def browse_ligand(self):
        self.ligfile = filedialog.askopenfilename(filetypes=[("Ligand file", "*.pdbqt")])
        print("Ligand chosen:", self.ligfile)
        return self.ligfile

    def collect_data(self):
        global outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname
        outfile = self.recfile.strip(".pdbqt") + self.ligfile
        logfile = self.recfile + self.ligfile + ".txt"
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
        return outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename
