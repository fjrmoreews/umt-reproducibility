



# Slurm and Singularity



Slurm is a cluster job scheduler than enables the access to computation power of a cluster.

Singularity is a container manager, dedicated to cluster, compatible with the docker image format, with a security model adapted to multi-user environment.  

We show here how we can simply combine the both tools to enable

 on High Power Computing  reproductible and flexible environment adapted to Data Science.

You will  execute  a python script within a docker image envionment on a computation cluster.



### Connection 
Use SSH in command line to access to the cluster 'master' server 
Follow the dedicated tutorial is needed..
 

### Slurm : Listing availables nodes
```
sinfo -N -O nodelist,partition,cpusstate,memory,allocmem,freemem
```

### Slurm Creating a job

You can launch a shell on a computing node using:

```
srun --pty bash
```

You can submit a job with the `sbatch` command:
```
sbatch my_script.sh
```

### Singularity : Create the  job scripts

Create a bash script named test.sh with the following content:
```
#!/bin/bash
. /softs/local/env/envsingularity-3.5.2.sh
IMAGENAME=fjrmore/pax2graphml
singularity run -B $PWD:/workdir docker://$IMAGENAME python3 /workdir/test.py
```

Create a python script named test.py with the following content:
```
import pax2graphml  as p2g
import timeit
start = timeit.default_timer()
print(p2g.__version__)
stop = timeit.default_timer()
print("Time: %.2f s"%(  stop - start) ) 
```

### Singularity : RUn the jobs

To run the script, you have 2 possibilities:


option 1
```
#access to a computation node
srun --pty bash
#then, on the computation node,
bash test.sh
```

option 2
```
sbatch test.sh
```











