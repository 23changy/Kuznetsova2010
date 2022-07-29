from neuron import h
h.load_file("stdlib.hoc")
h.load_file("nrngui.hoc")

print("Kuznetsova et al. 2010")

fig = input("Which figure do you want to run? 2a2, 2b2, 2f2, or 6: ")

if fig[0] == '6':
    ftype = input("Do you want dashed or solid? ")
    exec(open(f"Fig6a_{ftype}.py").read())
else:
    exec(open(f"Fig{fig}.py").read())
    


