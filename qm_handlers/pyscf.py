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

def pyscfCasscfOpt(job:Job, xyz:str) -> tuple[str, str]:
    pyscfString = 'import numpy as np\n'
    pyscfString += 'from pyscf import gto, lib\n'
    pyscfString += 'import matplotlib.pyplot as plt\n'
    pyscfString += 'from matplotlib.colors import hsv_to_rgb\n\n'

    pyscfString += 'def printXYZ(mol):\n'
    pyscfString += '    coords = f"{mol.natm}\\n"\n'
    pyscfString += '    for i in range(mol.natm):\n'
    pyscfString += '        x, y, z = mol.atom_coord(i)\n'
    pyscfString += '        coords += f"\\n{mol.atom_symbol(i)}    {x*0.529177: .10f}    {y*0.529177: .10f}    {z*0.529177: .10f}"\n'
    pyscfString += '    print(coords)\n'
    pyscfString += '    return coords\n\n'


    pyscfString += 'def plot(mc, degeneracyTol:float=0.01, \n'
    pyscfString += '             annotateSize:int=6, \n'
    pyscfString += '             annotateOffset:float=0.5,\n'
    pyscfString += '             figSize:list[int,int]=[10, 5],\n'
    pyscfString += '             ymax:list[int,int]=[-2, 2]) -> plt.figure:\n\n'

    pyscfString += '    def makeDegeneracyList(orbitals:list[float], degeneracyTol:float) -> np.ndarray:\n'
    pyscfString += '        currentBin = []\n'
    pyscfString += '        bins = []\n'
    pyscfString += '        binNum = 0\n'
    pyscfString += '        maxDegeneracy = 0\n'
    pyscfString += '        for i in range(len(orbitals)):\n'
    pyscfString += '            if i == 0:\n'
    pyscfString += '                currentBin += [binNum]\n'
    pyscfString += '                binNum += 1\n'
    pyscfString += '            else:\n'
    pyscfString += '                if abs(orbitals[i] - orbitals[i-1]) <= degeneracyTol:\n'
    pyscfString += '                    currentBin += [binNum]\n'
    pyscfString += '                    binNum += 1\n'
    pyscfString += '                else:\n'
    pyscfString += '                    bins += [currentBin]\n'
    pyscfString += '                    binNum = 0\n'
    pyscfString += '                    currentBin = [binNum]\n'
    pyscfString += '                    binNum += 1\n'
    pyscfString += '                    if len(bins[-1]) > maxDegeneracy:\n'
    pyscfString += '                        maxDegeneracy = len(bins[-1])\n'
    pyscfString += '        bins += [currentBin]\n\n'

    pyscfString += '        if len(bins[-1]) > maxDegeneracy:\n'
    pyscfString += '            maxDegeneracy = len(bins[-1])\n\n'

    pyscfString += '        offsetBins = []\n'
    pyscfString += '        for i in bins:\n'
    pyscfString += '            if len(i)%2 != 0:\n'
    pyscfString += '                if len(i) != 1:\n'
    pyscfString += '                    newbin = np.subtract(i, (len(i)-1)/2)\n'
    pyscfString += '                else:\n'
    pyscfString += '                    newbin = i\n'
    pyscfString += '            else:\n'
    pyscfString += '                newbin = np.subtract(i, (len(i)-1)/2)\n\n'
                
    pyscfString += '            offsetBins = np.append(offsetBins, newbin)\n'
    pyscfString += '        return offsetBins\n\n'

    pyscfString += '    figH, figW = figSize\n'
    pyscfString += '    ymin, ymax = ymax\n\n'

    pyscfString += '    fig, ax = plt.subplots(1,1, figsize=(figW,figH))\n\n'

    pyscfString += '    orbitals = mc.mo_energy.tolist()\n'
    pyscfString += '    occupation = np.round(mc.mo_occ, 3).tolist()\n'
    pyscfString += '    occupationCol = np.divide(np.add(np.multiply(np.divide(occupation, 2), 120), 240), 360)\n'
    pyscfString += '    occupationColOut = []\n'
    pyscfString += '    for i, val in enumerate(occupationCol):\n'
    pyscfString += '        r, g, b = hsv_to_rgb((val, 1, 1))\n'
    pyscfString += '        occupationColOut += [(r, g, b)]\n\n'

    pyscfString += '    occupationCol = occupationColOut\n'
    pyscfString += '    labels = [count for count, i in enumerate(orbitals)]\n'
    pyscfString += '    degen = makeDegeneracyList(orbitals, degeneracyTol)\n'
    pyscfString += '    ax.scatter(degen, orbitals, marker="_", s=2000, color=occupationCol)\n\n'

    pyscfString += '    for i, val in enumerate(labels):\n'
    pyscfString += '        ax.annotate(val, (degen[i]+annotateOffset, orbitals[i]), fontsize=annotateSize)\n'
    pyscfString += '    for i, val in enumerate(occupation):\n'
    pyscfString += '        if val < 1.999 and val > 0.001:\n'
    pyscfString += '            if val >= 1.95 or val <=0.05:\n'
    pyscfString += '                ax.annotate(val, (degen[i]-annotateOffset*2, orbitals[i]), fontsize=annotateSize, weight="bold", bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="magenta", lw=2))\n'
    pyscfString += '            else:\n'
    pyscfString += '                ax.annotate(val, (degen[i]-annotateOffset*2, orbitals[i]), fontsize=annotateSize, weight="bold", bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="green", lw=2))\n\n'

    pyscfString += '    ax.set_ylim((ymin, ymax))\n'
    pyscfString += '    ax.set_xlim((min(degen-0.5), max(degen+0.5)))\n'
    pyscfString += '    ax.set_ylabel(r"Energy ($eV$)")\n'
    pyscfString += '    ax.set_xticks([], [])\n'
    pyscfString += '    plt.close()\n'
    pyscfString += '    return fig\n\n'

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

    orbs, elec = job.casscf
    pyscfString += f'norbs = {orbs}\n'
    pyscfString += f'nelec = {elec}\n\n'

    pyscfString += 'mc = mol.CASSCF(norbs, nelec)\n'
    pyscfString += 'mc.max_cycle_macro = 1000\n'
    pyscfString += 'mc.max_cycle_micro = 20\n'
    pyscfString += 'mc.max_stepsize = 0.0005\n'
    pyscfString += 'mc.natorb = True\n'
    pyscfString += 'mc.fcisolver.nstates = nstates\n'
    pyscfString += 'mc.state_specific_(state=state)\n'
    pyscfString += 'mc.kernel()\n\n'

    pyscfString += 'try:\n'
    pyscfString += '    mol_opt = mc.nuc_grad_method().as_scanner().optimizer().kernel()\n'
    pyscfString += 'except Exception as e:\n'
    pyscfString += '    if "not converged" in str(e.args):\n'
    pyscfString += '        mc.max_stepsize = 0.01\n'
    pyscfString += '        try:\n'
    pyscfString += '            mol_opt = mc.nuc_grad_method().as_scanner().optimizer().kernel()\n'
    pyscfString += '        except Exception as e:\n'
    pyscfString += '            if "not converged" in str(e.args):\n'
    pyscfString += '                mc.max_stepsize = 0.001\n'
    pyscfString += '                try:\n'
    pyscfString += '                    mol_opt = mc.nuc_grad_method().as_scanner().optimizer().kernel()\n'
    pyscfString += '                except Exception as e:\n'
    pyscfString += '                    if "not converged" in str(e.args):\n'
    pyscfString += '                        mc.max_stepsize = 0.0001\n'
    pyscfString += '                        mol_opt = mc.nuc_grad_method().as_scanner().optimizer().kernel()\n'
    pyscfString += '                    else:\n'
    pyscfString += '                        raise Exception(e)\n'
    pyscfString += '            else:\n'
    pyscfString += '                raise Exception(e)\n'
    pyscfString += '    else:\n'
    pyscfString += '        raise Exception(e)\n\n'

    pyscfString += 'printXYZ(mol_opt)\n'
    pyscfString += 'print(mc.mo_occ[~np.isin(mc.mo_occ, [2., 0.])].tolist())\n\n'

    pyscfString += 'plot(mc).savefig("orbs.png", format="png", dpi=300)\n\n'


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