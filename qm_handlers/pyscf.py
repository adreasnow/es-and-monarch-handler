from ..types.job import Job
from ..types.methods import Methods


def pyscfCasscfScan(job:Job, xyz:str) -> tuple[str, str]:
    pyscfString = 'import numpy as np\n'
    pyscfString += 'from pyscf import gto, lib\n'

    pyscfString += 'with open("occupations.csv", "w+") as f:\n'
    pyscfString += '    f.write("level,total_energy,cas_energy\\n")\n'
    pyscfString += 'with open("occupations", "w+") as f:\n'
    pyscfString += '    f.write("")\n\n'

    pyscfString += 'def writeOccupations(string):\n'
    pyscfString += '    with open("occupations", "a") as f:\n'
    pyscfString += '        f.write(f"{string}\\n")\n\n'

    pyscfString += 'def writeEnergy(string):\n'
    pyscfString += '    with open("energy.csv", "a") as f:\n'
    pyscfString += '        f.write(f"{string}\\n")\n\n'

    pyscfString += 'def printXYZ(mol):\n'
    pyscfString += '    coords = f"{mol.natm}\\n"\n'
    pyscfString += '    for i in range(mol.natm):\n'
    pyscfString += '        x, y, z = mol.atom_coord(i)\n'
    pyscfString += '        coords += f"\\n{mol.atom_symbol(i)}    {x*0.529177: .10f}    {y*0.529177: .10f}    {z*0.529177: .10f}"\n'
    pyscfString += '    print(coords)\n'
    pyscfString += '    return coords\n\n'

    pyscfString += f'lib.num_threads({job.procs})\n'

    pyscfString += 'mol = gto.Mole()\n'
    pyscfString += f'mol.atom = """\n'
    for line in xyz:
        pyscfString += f'\n{line}'
    pyscfString += '\n"""\n\n'

    pyscfString += f'mol.charge = {job.fluorophore.charge}\n'
    pyscfString += 'mol.build()\n'
    pyscfString += f'mol.basis = "{job.basis.pyscf}"\n'
    pyscfString += f'state = {job.state.root}\n'
    pyscfString += f'mol.max_memory = {job.mem.total_mb}\n'
    pyscfString += 'mol.verbose = 4\n'
    pyscfString += f'nstates = {job.nroots}\n\n'
    
    start, a = job.casscf
    end, a = job.casscfend
    pyscfString += f'cas_start = {start}\n'
    pyscfString += f'cas_end = {end}\n\n'

    pyscfString += 'for active in range(cas_start, cas_end+2, 2):\n'
    pyscfString += '    mc = mol.CASSCF(active, active)\n'
    pyscfString += '    mc.max_cycle_macro = 500\n'
    pyscfString += '    mc.max_cycle_micro = 10\n'
    pyscfString += '    mc.max_stepsize = 0.001\n'
    pyscfString += '    mc.natorb = True\n'
    pyscfString += '    mc.fcisolver.nstates = nstates\n'
    pyscfString += '    mc.state_specific_(state=state)\n'
    pyscfString += '    mc.kernel() \n'
    pyscfString += '    occupations = mc.mo_occ[~np.isin(mc.mo_occ, [2., 0.])].tolist()\n\n'

    pyscfString += '    writeOccupations(f"({active},{active}) {occupations}")\n'
    pyscfString += '    writeEnergy(f"({active},{active}),{mc.e_tot},{mc.e_cas}")\n\n'

    pyscfSlmString = '#!/bin/bash\n'
    pyscfSlmString += '#SBATCH --time=24:00:00\n'
    pyscfSlmString += f'#SBATCH --ntasks={job.procs}\n'
    pyscfSlmString += '#SBATCH --cpus-per-task=1\n'
    pyscfSlmString += f'#SBATCH --ntasks-per-node={job.procs}\n'
    pyscfSlmString += f'#SBATCH --mem={job.mem.total_gb}GB\n'
    if job.partner == True: pyscfSlmString += '#SBATCH --qos=partner\n'
    pyscfSlmString += '#SBATCH --partition=comp,short\n\n'

    pyscfSlmString += 'export PROJECT="p2015120004"\n\n'

    pyscfSlmString += 'source /mnt/lustre/projects/p2015120004/apps/pyscf/activate_pyscf_job.sh\n'
    pyscfSlmString += f'cd {job.path}\n\n'
    pyscfSlmString += f'/usr/bin/time -v python {job.name}.py > {job.name}.out 2>&1\n\n'


    return pyscfString, pyscfSlmString
