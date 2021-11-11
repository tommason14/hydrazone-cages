# ms-tools/scripts/ffconv.py cage4_my_charges.ff phos_chelpg.ff no3.ff cage4_alpha.ff -o cage4.zfp

packmol < pack_mod.inp
fftool 1 cage4.xyz 1 phos.xyz 4 no3.xyz 500 dmso.zmat 2000 water.zmat -b 54 -l
python3 parse.py
