from mstools.topology import Topology
from mstools.forcefield import ForceField, PaduaLJScaler
from mstools.simsys import System

scaler = PaduaLJScaler("CLPol-ljscale.ff")
ff = ForceField.open("cage4.zfp", "SWM4-NDP.zfp")
scaler.scale(ff)
top = Topology.open("data.lmp", improper_center=3)
top.generate_angle_dihedral_improper()
top.generate_drude_particles(ff)
top.generate_virtual_sites(ff)
top.assign_charge_from_ff(ff)
system = System(top, ff)

system.export_gromacs(gro_out="conf.gro", top_out="topol.top", mdp_out=None)
system.export_charmm(pdb_out=None, psf_out="topol.psf", prm_out="ff.prm")
