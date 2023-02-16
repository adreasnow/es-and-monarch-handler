from ..types.job import Job


def buildCRESTOpt(job: Job) -> str:
    uhfString = '' if job.state.spin == 0 else f' --uhf {job.state.spin}'

    slmString = '#!/bin/bash\n'
    slmString += '#SBATCH --time=72:00:00\n'
    slmString += '#SBATCH --ntasks=16\n'
    slmString += '#SBATCH --cpus-per-task=1\n'
    slmString += '#SBATCH --ntasks-per-node=16\n'
    slmString += '#SBATCH --mem=32GB\n'
    slmString += '#SBATCH --partition=comp\n'

    if job.partner:
        slmString += '#SBATCH --qos=partner\n\n'

    slmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "CREST opt ' + job.fluorophore.name + '" , "value2": "started", "value3": "MonARCH"}\' https://maker.ifttt.com/trigger/$JOBID/with/key/$JOBKEY > /dev/null\n'

    slmString += '__conda_setup="$(\'/home/asnow/p2015120004/asnow/mambaforge/bin/conda\' \'shell.bash\' \'hook\' 2> /dev/null)"\n'
    slmString += 'if [ $? -eq 0 ]; then\n'
    slmString += '    eval "$__conda_setup"\n'
    slmString += 'else\n'
    slmString += '    if [ -f "/home/asnow/p2015120004/asnow/mambaforge/etc/profile.d/conda.sh" ]; then\n'
    slmString += '        . "/home/asnow/p2015120004/asnow/mambaforge/etc/profile.d/conda.sh"\n'
    slmString += '    else\n'
    slmString += '        export PATH="/home/asnow/p2015120004/asnow/mambaforge/bin:$PATH"\n'
    slmString += '    fi\n'
    slmString += 'fi\n\n'

    slmString += 'unset __conda_setup\n\n'
    slmString += 'ulimit -s unlimited\n'
    slmString += 'export OMP_STACKSIZE=4G\n'
    slmString += 'export OMP_NUM_THREADS=16,1\n'
    slmString += 'export OMP_THREAD_LIMIT=16\n'
    slmString += 'export OMP_MAX_ACTIVE_LEVELS=1\n'
    slmString += 'export MKL_NUM_THREADS=16\n'

    slmString += f'cd {job.path}\n'
    slmString += f'/usr/bin/time -v crest {job.fluorophore.name}.xyz --chrg {job.fluorophore.charge} --alpb {job.solv.xtb} {uhfString}\n\n'
    slmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "CREST opt ' + job.fluorophore.name + '" , "value2": "finished", "value3": "MonARCH"}\' https://maker.ifttt.com/trigger/$JOBID/with/job.fluorophore.name/$JOBKEY > /dev/null\n\n'

    return slmString
