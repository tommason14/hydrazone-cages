# Files used in "Robust organic cages prepared using hydrazone condensation display sulfate/hydrogenphosphate selectivity in water"

## Example simulations

The scripts folder contains example simulation files and [OpenMM](https://openmm.org/) scripts
required for both simulated annealing and conventional MD simulations.

Ensure the OpenMM version is compiled with the [velocity-verlet plugin](https://github.com/z-gong/openmm-velocityVerlet) 
to enable the temperature-grouped Nose-Hoover thermostat.

Simulations were created via [Packmol](http://leandro.iqm.unicamp.br/m3g/packmol/home.shtml) and [fftool](https://github.com/paduagroup/fftool) to create a LAMMPS datafile containing the required topology. These were then converted to OpenMM-compatible simulation files 
via a [python script](scripts/build/parse.py) to add virtual sites and Drude particles, then also scale LJ terms. This is
explained in depth in the supporting information.

## Structures extracted from simulations 

Each subfolder within [cage-3](cage-3) and [cage-4](cage-4) contains the 5 lowest-energy structures extracted from 10 ns NVT
simulations, run after simulated annealing between 10 and 500 K over 5 steps.
