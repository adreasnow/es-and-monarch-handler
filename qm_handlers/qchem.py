from ..types.job import Job
from ..types.jobs import Jobs
from ..types.job import Solvents
from ..types.job import PCM

    # def pullEnergyQChem(self, file: str, state: int=0, roots: int=0) -> Union[None, tuple[Union[float, List[float]], Union[float, List[float]]]]:
    #     # e.g. /home/asnow/p2015120004/asnow/fluorophore-small/geoms/rb0-chcl3/orca-opt/rb0-chcl3-opt/rb0-chcl3-opt.out
    #     out, err = self.run(f'cat {file} | grep \'CIS_N_ROOTS\\|: excitation energy (eV) =\\|END OF GEOMETRY OPTIMIZER USING LIBOPT3\'')
    #     results = []
    #     excitations = []
    #     complete = False
    #     for line in out:
    #         if 'CIS_N_ROOTS' in line:   
    #             nroots = int(line.split()[1])
    #         elif ': excitation energy (eV) =' in line:
    #             results += [line]
    #         elif 'END OF GEOMETRY OPTIMIZER USING LIBOPT3' in line:
    #             complete = True

    #     for i in results[-nroots:]:
    #         excitations += [float(i.split()[7])]

    #     excitations = excitations[-nroots:]

    #     if roots != 0:
    #         excitations = excitations[-roots:]

    #     if state != 0:
    #         excitations = excitations[(state-1)]

    #     if complete == True:
    #         return excitations, evToNm(excitations)
    #     else:
    #         return


    # def buildQChemOptSMD(self, key: str, method: str, basis: str, charge: int, solvent: str, 
    #                      nroots: int=4, root: int=0, mult: int=1, singlets: bool=True, 
    #                      triplets: bool=False) -> str:
    #     qchemmethod = 'CAM-B3LYP' if method == 'cb3lyp' else 'WB97XD' if method == 'wb97x-d3' else method
    #     solvent = 'trichloromethane' if solvent == 'chloroform' else solvent[2:] if solvent[0:2] == 'n-' else solvent
    #     name = stripIllegal(f'{key}-qchem-smd-opt-{method}-{basis}-r{root}')

    #     QChemInput = f'$molecule\n'
    #     QChemInput += f'{charge} {1}\n'
    #     lines, err = self.run(f'cat "/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/crest/crest_best.xyz"')
    #     for line in lines[2:]:
    #         if len(line.split()) > 2:
    #             QChemInput += f'{line}\n'
    #     QChemInput +=  '$end\n\n'
    #     QChemInput +=  '$rem\n'
    #     QChemInput +=  '\tMEM_TOTAL          32768\n'
    #     QChemInput +=  '\tJOBTYPE            opt\n'
    #     QChemInput += f'\tMETHOD             {qchemmethod}\n'
    #     QChemInput += f'\tBASIS              {basis}\n'
    #     QChemInput +=  '\tGUI                2\n'
    #     if root != 0:
    #         QChemInput += f'\tCIS_N_ROOTS        {nroots}\n'
    #         QChemInput += f'\tCIS_SINGLETS       {singlets}\n'
    #         QChemInput += f'\tCIS_TRIPLETS       {triplets}\n'
    #         QChemInput += f'\tCIS_STATE_DERIV    {root}\n'
    #         QChemInput +=  '\tRPA                2\n'
    #     QChemInput +=  '\tXC_GRID            3\n'
    #     QChemInput +=  '\tSOLVENT_METHOD     SMD\n'
    #     QChemInput +=  '$end\n\n'
    #     QChemInput +=  '$smx\n'
    #     QChemInput += f'\tSOLVENT            {solvent}\n'
    #     QChemInput +=  '\tprint              2\n'
    #     QChemInput +=  '$end\n\n'

    #     if root == 0:
    #         QChemInput += '@@@\n\n'
    #         QChemInput +=  '$molecule\n'
    #         QChemInput +=  '   read\n'
    #         QChemInput +=  '$end\n\n'
    #         QChemInput +=  '$rem\n'
    #         QChemInput +=  '\tJOBTYPE            sp\n'
    #         QChemInput += f'\tMETHOD             {qchemmethod}\n'
    #         QChemInput += f'\tBASIS              {basis}\n'
    #         QChemInput +=  '\tGUI                2\n'
    #         QChemInput += f'\tCIS_N_ROOTS        {nroots}\n'
    #         QChemInput += f'\tCIS_SINGLETS       {singlets}\n'
    #         QChemInput += f'\tCIS_TRIPLETS       {triplets}\n'
    #         QChemInput +=  '\tRPA                2\n'
    #         QChemInput +=  '\tXC_GRID            3\n'
    #         QChemInput +=  '\tSOLVENT_METHOD     SMD\n'
    #         QChemInput +=  '$end\n\n'
    #         QChemInput +=  '$smx\n'
    #         QChemInput += f'\tSOLVENT            {solvent}\n'
    #         QChemInput +=  '\tprint              2\n'
    #         QChemInput +=  '$end\n\n'

    #     filename = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/{name}.inp'.replace('()', '')

    #     self.writeFile(QChemInput, filename)
    #     return filename