# Resources module

This module is a bit of an esoteric one, but it's designed to let me interface with HPC clusters from my local machines to:

* Push files
* Pull files
* Run commands remotely
* Build job scripts
* Check on the status of jobs

I mostly created it in order to be able handle remote connections without worrying about spamming the cluster with every call, so it's written mostly to be used as a context manager.

```python
import resources as r
with r.monarchhandler() as mon:
    mon.do_something()
```

This eventually got extended to provide a few dataclasses and enum types in order to be able to more easily/reliably pass informations between functions in a single object. The big one of these is the `r.Job` object that stores a huge amount of information, and automatically builds paths and filenames:

```python
job = r.Job(r.Software.orca, r.Fluorophores.az, r.Solvents.gas, r.Methods.wb97xd, r.Basis.augccpvdz, r.PCM.none, r.PCM.Eq.none, r.Fluorophores.az.root, r.Jobs.opt)
```

This project is also a big learning experience for me to be able to better my skills with python typehinting and OOP. I'm aware that I'm not following PEP8 stying or anyhting like that, but I'm trying to keep things tidy in my own way :)