# Kuznetsova2010
 
A python version of the hoc code from Kuznetsova et al, 2010. This version is hybrid - loads in the cell morphology from dopamine.hoc. Many other commands are issued in hoc using h(). Some are directly in python, as is plotting.

## Running the model

Make sure to compile the mechanisms first:

In the directory of the model code, compile the *.mod mechanisms by running the following command in a terminal:

On Windows, run `mknrndll`
On Mac and Linux, run `nrnivmodl`

Alternatively, open the NEURON Application folder (or program folder from the Start menu on Windows) and launch the mknrndll tool. When the gui appears, select the folder containing the code for Kuznetsova et al 2010. Then click the button to make nrnmech.dll.

After the mechanisms are successfully compiled, run `main.py` to receive a prompt asking which figure you would like to view.

You can also call the figure files directly (ex: `python Fig2a2.py`)
