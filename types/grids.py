from .newenum import *
class Grids(NewEnum):
    def __init__(self, grid:tuple[int, int], gridString:str, orca4:str, orca:str, nwchem:str, qchem:str, psi4:str) -> None:
        self.grid       = grid
        self.gridString = gridString
        self.orca       = orca
        self.orca4      = orca4
        self.nwchem     = nwchem
        self.qchem      = qchem
        self.psi4       = psi4

    def __str__(self):
        return self.gridString

    #           grid     gridstring     orca4      orca                                  nwchem                   qchem               psi4 
    none     = (None, None),  'None',   '',      '',                                    '',                     '',             ''  
    # gx_50    = (  , 50),   '(  ,50)',   'grid1', '%method\n    AngularGrid 1\nend\n\n', 'grid lebedev    2',    '0000  000050', 'dft_radial_points         \ndft_spherical_points   50\n'  
    # gx_110   = (  , 110),  '(  ,110)',  'grid2', '%method\n    AngularGrid 2\nend\n\n', 'grid lebedev    5',    '0000  000110', 'dft_radial_points         \ndft_spherical_points   110\n'  
    g50_194  = (50, 194),  '(50,194)',  'grid3', '%method\n    AngularGrid 3\nend\n\n', 'grid lebedev 50 8',    '000050000194', 'dft_radial_points       50\ndft_spherical_points   194\n'  
    g75_302  = (75, 302),  '(75,302)',  'grid4', '%method\n    AngularGrid 4\nend\n\n', 'grid lebedev 75 11',   '000075000302', 'dft_radial_points       75\ndft_spherical_points   302\n'  
    # gxx_434  = (  , 434),  '(  ,434)',  'grid5', '%method\n    AngularGrid 5\nend\n\n', 'grid lebedev    13',   '0000  000590', 'dft_radial_points         \ndft_spherical_points   434\n'  
    g99_590  = (99, 590),  '(99,590)',  'grid6', '%method\n    AngularGrid 6\nend\n\n', 'grid lebedev 99 14',   '000099000590', 'dft_radial_points       99\ndft_spherical_points   590\n'  
    # g250_770 = (250, 770), '(250,770)', 'grid7', '%method\n    AngularGrid 7\nend\n\n', 'grid lebedev 250 54',  '000250000770', 'dft_radial_points       250\ndft_spherical_points   770\n'    

