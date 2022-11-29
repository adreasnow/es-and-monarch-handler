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
    PySCFString  =  'from pyscf import gto, lib, mrpt, mcscf\n'
    PySCFString +=  'import numpy as np\n'
    PySCFString +=  'import matplotlib.pyplot as plt\n'
    PySCFString +=  'from matplotlib.colors import hsv_to_rgb\n'
    PySCFString +=  'from functools import reduce\n'
    PySCFString +=  'import os\n\n'

    PySCFString += f'lib.num_threads({job.procs})\n'
    PySCFString +=  'jobName = os.environ["SLURM_JOB_NAME"].split(".")[0]\n\n'

    PySCFString +=  'def evToNm(eV: float|list[float], error: float=0.0) -> float|tuple[float, float, float]:\n'
    PySCFString +=  '    def ev2nm(eV):\n'
    PySCFString +=  '        h = 4.135667e-15\n'
    PySCFString +=  '        c = 2.99792e8\n'
    PySCFString +=  '        return np.divide(np.multiply(h,c), np.multiply(eV,1e-9))\n\n'
    
    PySCFString +=  '    if type(eV) == float:\n'
    PySCFString +=  '        nm = ev2nm([eV, eV+error, eV-error])\n'
    PySCFString +=  '        if   error == 0:\n'
    PySCFString +=  '            return nm[0]\n'
    PySCFString +=  '        elif error != 0:\n'
    PySCFString +=  '            return (nm[0], nm[1], nm[2])\n\n'
    
    PySCFString +=  '    else:\n'
    PySCFString +=  '        nm = ev2nm(eV)\n'
    PySCFString +=  '        return nm\n\n'
    
    PySCFString +=  'def printXYZ(mol):\n'
    PySCFString +=  '    coords = f"{mol.natm}\\n\\n"\n'
    PySCFString +=  '    for i in range(mol.natm):\n'
    PySCFString +=  '        x, y, z = mol.atom_coord(i)\n'
    PySCFString +=  '        coords += f"{mol.atom_symbol(i)}    {x*0.529177: .10f}    {y*0.529177: .10f}    {z*0.529177: .10f}\\n"\n'
    PySCFString +=  '    print(coords)\n'
    PySCFString +=  '    return coords\n\n'

    PySCFString +=  'def m_diag(occ_ref:list[float]|np.ndarray, occ_no:list[float]|np.ndarray) -> float:\n'
    PySCFString +=  '    if type(occ_ref) == list: occ_ref = np.array(occ_ref)\n'
    PySCFString +=  '    if type(occ_no) == list: occ_no = np.array(occ_no)\n\n'

    PySCFString +=  '    docc = occ_no[np.equal(occ_ref, 2.)].tolist()\n'
    PySCFString +=  '    socc = occ_no[np.equal(occ_ref, 1.)].tolist()\n'
    PySCFString +=  '    uocc = occ_no[np.equal(occ_ref, 0.)].tolist()\n'
    PySCFString +=  '    soccm1 = np.abs(np.subtract(socc, 1))\n'
    PySCFString +=  '    m = 0.5*(2-min(docc)+np.sum(soccm1)+max(uocc))\n'
    PySCFString +=  '    return round(m, 3)\n\n'

    PySCFString +=  'def plot(mc, degeneracyTol:float=0.01, \n'
    PySCFString +=  '             annotateSize:int=6, \n'
    PySCFString +=  '             annotateOffset:float=0.5,\n'
    PySCFString +=  '             figSize:list[int,int]=[10, 5],\n'
    PySCFString +=  '             ymax:list[int,int]=[-2, 2]) -> plt.figure:\n\n'

    PySCFString +=  '    def makeDegeneracyList(orbitals:list[float], degeneracyTol:float) -> np.ndarray:\n'
    PySCFString +=  '        currentBin = []\n'
    PySCFString +=  '        bins = []\n'
    PySCFString +=  '        binNum = 0\n'
    PySCFString +=  '        maxDegeneracy = 0\n'
    PySCFString +=  '        for i in range(len(orbitals)):\n'
    PySCFString +=  '            if i == 0:\n'
    PySCFString +=  '                currentBin += [binNum] # set our intial bin number\n'
    PySCFString +=  '                binNum += 1\n'
    PySCFString +=  '            else:\n'
    PySCFString +=  '                if abs(orbitals[i] - orbitals[i-1]) <= degeneracyTol: # if the energy difference between this and the previous orbital is\n'
    PySCFString +=  '                    currentBin += [binNum] #                             witihin the degenracy tolerance, append to the current bin\n'
    PySCFString +=  '                    binNum += 1\n'
    PySCFString +=  '                else:\n'
    PySCFString +=  '                    bins += [currentBin]              # otherwise, append the previous bin to the bin list \n'
    PySCFString +=  '                    binNum = 0\n'
    PySCFString +=  '                    currentBin = [binNum]             # create a new bin with the new bin number\n'
    PySCFString +=  '                    binNum += 1\n'
    PySCFString +=  '                    if len(bins[-1]) > maxDegeneracy: # update the max bin size\n'
    PySCFString +=  '                        maxDegeneracy = len(bins[-1])\n'
    PySCFString +=  '        bins += [currentBin]\n\n'

    PySCFString +=  '        if len(bins[-1]) > maxDegeneracy:             # in case the last bin was degenerate, we want to update the bin size anyway\n'
    PySCFString +=  '            maxDegeneracy = len(bins[-1])\n\n'

    PySCFString +=  '        offsetBins = []\n'
    PySCFString +=  '        for i in bins:\n'
    PySCFString +=  '            if len(i)%2 != 0:\n'
    PySCFString +=  '                if len(i) != 1:\n'
    PySCFString +=  '                    newbin = np.subtract(i, (len(i)-1)/2)\n'
    PySCFString +=  '                else:\n'
    PySCFString +=  '                    newbin = i\n'
    PySCFString +=  '            else:\n'
    PySCFString +=  '                newbin = np.subtract(i, (len(i)-1)/2)\n'
    PySCFString +=  '                \n'
    PySCFString +=  '            offsetBins = np.append(offsetBins, newbin)\n'
    PySCFString +=  '        return offsetBins\n\n'

    PySCFString +=  '    figH, figW = figSize\n'
    PySCFString +=  '    ymin, ymax = ymax\n\n'

    PySCFString +=  '    fig, ax = plt.subplots(1,1, figsize=(figW,figH))\n\n'

    PySCFString +=  '    orbitals = mc.mo_energy.tolist()\n'
    PySCFString +=  '    occupation = np.round(mc.mo_occ, 3).tolist()\n'
    PySCFString +=  '    occupationCol = np.divide(np.add(np.multiply(np.divide(occupation, 2), 120), 240), 360)\n'
    PySCFString +=  '    occupationColOut = []\n'
    PySCFString +=  '    for i, val in enumerate(occupationCol):\n'
    PySCFString +=  '        r, g, b = hsv_to_rgb((val, 1, 1))\n'
    PySCFString +=  '        occupationColOut += [(r, g, b)]\n\n'

    PySCFString +=  '    occupationCol = occupationColOut\n\n'

    PySCFString +=  '    labels = [count for count, i in enumerate(orbitals)]\n\n'

    PySCFString +=  '    degen = makeDegeneracyList(orbitals, degeneracyTol)\n\n'

    PySCFString +=  '    ax.scatter(degen, orbitals, marker="_", s=2000, color=occupationCol)\n\n'

    PySCFString +=  '    for i, val in enumerate(labels):\n'
    PySCFString +=  '        ax.annotate(val, (degen[i]+annotateOffset, orbitals[i]), fontsize=annotateSize)\n'
    PySCFString +=  '    for i, val in enumerate(occupation):\n'
    PySCFString +=  '        if val < 1.999 and val > 0.001:\n'
    PySCFString +=  '            if val >= 1.95 or val <=0.05:\n'
    PySCFString +=  '                ax.annotate(val, (degen[i]-annotateOffset*2, orbitals[i]), fontsize=annotateSize, weight="bold", bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="magenta", lw=2))\n'
    PySCFString +=  '            else:\n'
    PySCFString +=  '                ax.annotate(val, (degen[i]-annotateOffset*2, orbitals[i]), fontsize=annotateSize, weight="bold", bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="green", lw=2))\n\n'

    PySCFString +=  '    ax.set_ylim((ymin, ymax))\n'
    PySCFString +=  '    ax.set_xlim((min(degen-0.5), max(degen+0.5)))\n'
    PySCFString +=  '    ax.set_ylabel(r"Energy ($eV$)")\n'
    PySCFString +=  '    ax.set_xticks([], [])\n'
    PySCFString +=  '    plt.close()\n'
    PySCFString +=  '    return fig\n\n'

    PySCFString +=  'def makedip(ci_id):\n'
    PySCFString +=  '    t_dm1 = mc_es.fcisolver.trans_rdm1(ss_state, mc_es.ci[ci_id], mc_es.ncas, mc_es.nelecas) # transform density matrix in MO representation\n'
    PySCFString +=  '    orbcas = orbital[:,mc_es.ncore:mc_es.ncore+mc_es.ncas] # transform density matrix to AO representation\n'
    PySCFString +=  '    t_dm1_ao = reduce(np.dot, (orbcas, t_dm1, orbcas.T)) # transition dipoles\n'
    PySCFString +=  '    return np.einsum("xij,ji->x", dip_ints, t_dm1_ao)\n\n'

    PySCFString +=  'def writeData(string:str) -> None:\n'
    PySCFString +=  '    with open(f"{jobName}-data.out", "a") as f:\n'
    PySCFString +=  '        f.write(f"{string}\\n")\n\n'

    PySCFString +=  'def resetData() -> None:\n'
    PySCFString +=  '    with open(f"{jobName}-data.out", "w+") as f:\n'
    PySCFString +=  '        f.write("")\n\n'

    PySCFString +=  'mol = gto.Mole()\n'
    PySCFString +=  'mol.atom = """ \n'
    for line in xyz:
        PySCFString += f'\n{line}'
    PySCFString += '\n"""\n\n'

    PySCFString += f'spin = {job.state.spin}\n'
    PySCFString += f'state = {job.state.root}\n'
    PySCFString += f'nstates = {job.nroots}\n'

    nelec, norbs = job.casscf
    PySCFString += f'norbs = {norbs}\n'
    PySCFString += f'nelec = {nelec}\n'
    PySCFString += f'sp_conv_e = 1e-10\n'
    PySCFString += f'opt_conv_e = 1e-8\n\n'

    PySCFString += f'mol.charge = {job.fluorophore.charge}\n'
    PySCFString += f'mol.spin = spin\n'
    PySCFString += f'mol.basis = "{job.basis.pyscf}"\n'
    PySCFString += f'mol.max_memory = {job.mem.total_mb}\n'
    PySCFString +=  'mol.verbose = 4\n'
    PySCFString +=  'mol.output = f"{jobName}.out"\n'
    PySCFString +=  'mol.build()\n\n'

    PySCFString +=  'weights_ss = np.zeros(nstates)\n'
    PySCFString +=  'weights_ss[state] = 1\n'
    PySCFString +=  'weights_sa = np.ones(nstates)/nstates\n\n'

    PySCFString +=  '# SS Opt Cycle\n'
    PySCFString +=  'mc_ss = mol.CASSCF(norbs, nelec).state_average(weights_ss)\n'
    PySCFString +=  'mc_ss.max_cycle_macro = 300\n'
    PySCFString +=  'mc_ss.max_cycle_micro = 20\n'
    PySCFString +=  'mc_ss.max_stepsize = 0.1\n'
    PySCFString +=  'mc_ss.conv_tol = opt_conv_e\n'
    PySCFString +=  'mc_ss.fix_spin_(ss=spin)\n'
    PySCFString +=  'new_mol = mc_ss.nuc_grad_method().as_scanner().optimizer().kernel()\n\n'

    PySCFString +=  'with open(f"{jobName}.xyz", "w+") as f:\n'
    PySCFString +=  '    f.write(printXYZ(new_mol))\n\n'

    PySCFString +=  '# Starting point\n'
    PySCFString +=  'mf = new_mol.RHF()\n'
    PySCFString +=  'mf.kernel()\n\n'

    PySCFString +=  '# SA-CASSCF to get optimal orbitals\n'
    PySCFString +=  'mc_sa = new_mol.CASSCF(norbs, nelec).state_average(weights_sa)\n'
    PySCFString +=  'mc_sa.max_cycle_macro = 500\n'
    PySCFString +=  'mc_sa.max_cycle_micro = 20\n'
    PySCFString +=  'mc_sa.max_stepsize = 0.1\n'
    PySCFString +=  'mc_sa.conv_tol = sp_conv_e\n'
    PySCFString +=  'mc_sa.fcisolver.nstates = nstates\n'
    PySCFString +=  'mc_sa.fix_spin_(ss=spin)\n'
    PySCFString +=  'mc_sa.kernel()\n\n'

    PySCFString +=  'orbital = mc_sa.mo_coeff\n\n'

    PySCFString += '# SS-CASSCF wavefunction.\n'
    PySCFString +=  'mc_ss = mcscf.CASCI(mf, norbs, nelec).state_specific_(state)\n'
    PySCFString +=  'mc_ss.kernel(orbital)\n'
    PySCFString +=  'ss_state = mc_ss.ci\n'
    PySCFString +=  'ss_e = mc_ss.e_tot\n\n'

    PySCFString +=  '# CASCI to get higher roots\n'
    PySCFString +=  'mc_es = mcscf.CASCI(mf, norbs, nelec)\n'
    PySCFString +=  'mc_es.fcisolver.nroots = nstates\n'
    PySCFString +=  'mc_es.conv_tol  = sp_conv_e\n'
    PySCFString +=  'mc_es.fix_spin_(ss=spin)\n'
    PySCFString +=  'mc_es.kernel(orbital)\n\n'

    PySCFString +=  'eList = mc_es.e_tot\n\n'

    PySCFString +=  '#NEVPT2 for each root\n'
    PySCFString +=  'nevptEnergy = []\n'
    PySCFString +=  'for root in range(nstates):\n'
    PySCFString +=  '    nevptEnergy += [mrpt.NEVPT(mc_es, root=root).kernel()]\n\n'

    PySCFString +=  '# transition density matrix and transition dipole\n'
    PySCFString +=  'charges = new_mol.atom_charges()\n'
    PySCFString +=  'coords = new_mol.atom_coords()\n'
    PySCFString +=  'nuc_charge_center = np.einsum("z,zx->x", charges, coords) / charges.sum()\n'
    PySCFString +=  'new_mol.set_common_orig_(nuc_charge_center)\n'
    PySCFString +=  'dip_ints = new_mol.intor("cint1e_r_sph", comp=3)\n\n'

    PySCFString +=  'resetData()\n\n'

    PySCFString +=  'writeData("\\n------------------------------------------------------------------------")\n'
    PySCFString +=  'writeData("------------------------------- CASSCF ---------------------------------")\n'
    PySCFString +=  'writeData("------------------------------------------------------------------------")\n'
    PySCFString +=  'writeData("\\n")\n'
    PySCFString +=  'writeData("Transition      E(Eh)      E (eV)      E(nm)    |Transition dipole|^2   ")\n'
    PySCFString +=  'writeData("------------------------------------------------------------------------")\n'
    PySCFString +=  'for i in range(nstates):\n'
    PySCFString +=  '    if i == state:\n'
    PySCFString +=  '        writeData(f"0 -> {i:<3}     {0.0:4.6f}    {0.0:4.6f}      {0.0:>7.2f}      {0.0:.6f}")\n'
    PySCFString +=  '    else:\n'
    PySCFString +=  '        eEh = abs(mc_es.e_tot[i] - mc_es.e_tot[state])\n'
    PySCFString +=  '        eEh = eEh\n'
    PySCFString +=  '        eeV = eEh * 27.2114\n'
    PySCFString +=  '        enm = evToNm(eeV)\n'
    PySCFString +=  '        dipole = np.linalg.norm(np.square(makedip(i)))\n'
    PySCFString +=  '        writeData(f"0 -> {i:<3}     {eEh:4.6f}    {eeV:4.6f}      {enm:>7.2f}      {dipole:.6f}")\n\n'

    PySCFString +=  'writeData("\\n\\n------------------------------------------------------------------------")\n'
    PySCFString +=  'writeData("------------------------------- NEVPT2 ---------------------------------")\n'
    PySCFString +=  'writeData("------------------------------------------------------------------------")\n'
    PySCFString +=  'writeData("\\n")\n'
    PySCFString +=  'writeData("Transition      E(Eh)      E (eV)      E(nm)    |Transition dipole|^2   ")\n'
    PySCFString +=  'writeData("------------------------------------------------------------------------")\n'
    PySCFString +=  'for i in range(nstates):\n'
    PySCFString +=  '    if i == state:\n'
    PySCFString +=  '        writeData(f"0 -> {i:<3}     {0.0:4.6f}    {0.0:4.6f}      {0.0:>7.2f}      {0.0:.6f}")\n'
    PySCFString +=  '    else:\n'
    PySCFString +=  '        eEh = abs((mc_es.e_tot[i]+nevptEnergy[i]) - (mc_es.e_tot[state]+nevptEnergy[state]))\n'
    PySCFString +=  '        eEh = eEh\n'
    PySCFString +=  '        eeV = eEh * 27.2114\n'
    PySCFString +=  '        enm = evToNm(eeV)\n'
    PySCFString +=  '        dipole = np.linalg.norm(np.square(makedip(i)))\n'
    PySCFString +=  '        writeData(f"0 -> {i:<3}     {eEh:4.6f}    {eeV:4.6f}      {enm:>7.2f}      {dipole:.6f}")\n\n'

    PySCFString +=  'writeData(f"\\nOrbital Occupations: {mc_es.mo_occ[~np.isin(mc_es.mo_occ, [2., 0.])].tolist()}")\n\n'

    PySCFString +=  'writeData(f"\\nM-Diagnostic: {m_diag(mf.mo_occ,mc_es.mo_occ)}")\n\n'

    PySCFString +=  'fig = plot(mc_es, degeneracyTol=0.01)\n'
    PySCFString +=  'fig.savefig(f"{jobName}-orbs.png", format="png", dpi=300)'




    pyscfSlmString = '#!/bin/bash\n'
    pyscfSlmString += '#SBATCH --time=24:00:00\n'
    pyscfSlmString += f'#SBATCH --ntasks={job.procs}\n'
    pyscfSlmString += '#SBATCH --cpus-per-task=1\n'
    pyscfSlmString += f'#SBATCH --ntasks-per-node={job.procs}\n'
    pyscfSlmString += f'#SBATCH --mem={job.mem.total_gb}GB\n'
    if job.partner == True: pyscfSlmString += '#SBATCH --qos=partner\n'
    pyscfSlmString += '#SBATCH --partition=comp,short\n\n'

    pyscfSlmString += 'export PROJECT="p2015120004"\n\n'

    pyscfSlmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "\'`echo $SLURM_JOB_NAME | cut -d\'.\' -f 1`\'" , "value2": "running", "value3": "MonARCH"}\' https://maker.ifttt.com/trigger/$JOBID/with/key/$JOBKEY > /dev/null\n\n'

    pyscfSlmString += 'source /mnt/lustre/projects/p2015120004/apps/pyscf/activate_pyscf_job.sh\n'
    pyscfSlmString += f'cd {job.path}\n\n'
    pyscfSlmString += f'/usr/bin/time -v python {job.name}.py > {job.name}.out 2>&1\n\n'

    pyscfSlmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "\'`echo $SLURM_JOB_NAME | cut -d\'.\' -f 1`\'" , "value2": "finished", "value3": "MonARCH"}\' https://maker.ifttt.com/trigger/$JOBID/with/key/$JOBKEY > /dev/null\n\n'

    return PySCFString, pyscfSlmString