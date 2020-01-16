class ConfigMaker:

    def create_conf_file(self,  outfile, logfile, ox, oy, oz, dx, dy, dz, ncpu, nmod, energy, outname, filename):
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
            cfg.write("size_x = ")
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
