import subprocess

args = [ 'yapf',  '-ir' , 'tsu/' ]
subprocess.run(args)

