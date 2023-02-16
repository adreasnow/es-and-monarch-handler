from .newenum import NewEnum


class Orbs(NewEnum):

    #              Method                          orca           nwchem           qchem        psi4         pyscf 
    can       = 'Canonical',                       None,           None,           None,         None,         None,
    nat       = 'Natural Orbitals',                None,           None,           None,         None,         None,
    nto       = 'Natural Transition Orbitals',     None,           None,           None,         None,         None,
    iao       = 'Intrinsic Atomic Orbitals',       None,           None,           None,         None,         None,
    ibo       = 'Intrinsic Bonding Orbitals',      None,           None,           None,         None,         None,