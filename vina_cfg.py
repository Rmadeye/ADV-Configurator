from tkinter import *
from tkinter import filedialog
#import vinareader as vr
import os

window=Tk()
window.wm_title("VinaConfigurator")
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file="icon.png"))

#def window_commands():
def browse_receptor():
    global recfile
    recfile=filedialog.askopenfilename(filetypes=[("Receptor file","*.pdbqt")])
    print("Receptor chosen:",recfile)
    Label1=Label(window, text=recfile).grid(row=0,column=1)
    return recfile
def browse_flexres():
    global flexfile
    flexfile=filedialog.askopenfilename(filetypes=[("Flexible residues file","*.pdbqt")])
    print("Receptor chosen:",flexfile)
    Label2=Label(window, text=flexfile).grid(row=1,column=1)
    return flexfile
def browse_ligand():
    global ligfile
    ligfile=filedialog.askopenfilename(filetypes=[("Ligand file","*.pdbqt")])
    print("Ligand chosen:",ligfile)
    Label3 = Label(window, text=ligfile).grid(row=2, column=1)
    return ligfile


# Label & Button list
# Primary buttons - choice of pdbqt files
Button1=Button(window, text="Choose receptor", command=browse_receptor).grid(row=0,column=0)
Button2=Button(window, text="Choose flexible residues ", command=browse_flexres).grid(row=1,column=0)
Button3=Button(window, text="Choose ligand", command=browse_ligand).grid(row=2,column=0)
Label4 = Label(window, text="X coord").grid(row=3)
xc=Entry(window)
xc.grid(row=3, column = 1)
Label5 = Label(window, text="Y coord").grid(row=4)
yc=Entry(window)
yc.grid(row=4, column =1)
Label6 = Label(window, text="Z coord").grid(row=5)
zc=Entry(window)
zc.grid(row=5, column =1)
Label7 = Label(window, text="X dim").grid(row=6)
xd=Entry(window)
xd.grid(row=6, column=1)
Label8 = Label(window, text="Y dim").grid(row=7)
yd=Entry(window)
yd.grid(row=7, column =1)
Label9 = Label(window, text="Z dim").grid(row=8)
zd = Entry(window)
zd.grid(row=8, column =1)
Label10 = Label(window, text="CPU number").grid(row=9)
cpu = Entry(window)
cpu.grid(row=9, column =1)
Label11 = Label(window, text="Models (1-10k)").grid(row=10)
mod_num = Entry(window)
mod_num.grid(row=10, column=1)
Label12 = Label(window, text="Energy range (kcal)").grid(row=11)
er=Entry(window)
er.grid(row=11, column =1)
Label13=Label(window, text="Output pdbqt and log filename").grid(row=12)
outnameg=Entry(window)
outnameg.grid(row=12, column = 1)
Label14=Label(window, text="Config filename").grid(row=13)
filenameg=Entry(window)
filenameg.grid(row=13, column = 1)

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
    outname=outnameg.get()
    ncpu = cpu.get()
    nmod = mod_num.get()
    energy = er.get()
    filename=str(filenameg.get())
    print(outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename)
    return outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename

#def create_conf_file(recfile, flexfile, ligfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy):
def create_conf_file():
    outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename = collect_data()
    with open(filename+'.txt', 'w+') as cfg:
        cfg.write("receptor = ") # receptor add
        cfg.write(recfile)
        cfg.write("\n")
        try:
            print(flexfile)
            cfg.write("flex = ") # flexres add
            cfg.write(flexfile)
        except NameError:
            pass
        cfg.write("\n")
        cfg.write("ligand = ")
        cfg.write(ligfile)
        cfg.write("\n")
        cfg.write("\n")
        cfg.write("out = ")
        cfg.write(outname)
        cfg.write(".pdbqt")
        cfg.write("\n")
        cfg.write("\n")
        cfg.write("center_x = ")
        cfg.write(str(ox))
        cfg.write("\n")
        cfg.write("center_y = ")
        cfg.write(str(oy))
        cfg.write("\n")
        cfg.write("center_z = ")
        cfg.write(str(oz))
        cfg.write("\n")
        cfg.write("size_x =c")
        cfg.write(str(dx))
        cfg.write("\n")
        cfg.write("size_y = ")
        cfg.write(str(dy))
        cfg.write("\n")
        cfg.write("size_z = ")
        cfg.write(str(dz))
        cfg.write("\n")
        cfg.write("\n")
        cfg.write("log = ")
        cfg.write(outname)
        cfg.write('.txt')
        cfg.write("\n")
        cfg.write("cpu = ")
        cfg.write(str(ncpu))
        cfg.write("\n")
        cfg.write("num_modes = ")
        cfg.write(str(nmod))
        cfg.write("\n")
        cfg.write("energy_range = ")
        cfg.write(str(energy))


def main():
    collect = Button(window, text="Collect data", command=collect_data).grid(row=14, column=1)
    exe= Button(window, text="Save cfg file", command=create_conf_file).grid(row = 15, column = 1)
    if create_conf_file == True:
        Label14=Label(window, text="Saved").grid(row=15,column=0)

#main()
#window_desc()

main()

window.mainloop()
