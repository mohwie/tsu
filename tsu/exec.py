# Copyright (c) 2019, Cswl Coldwind <cswl1337@gmail.com
# This software is licensed under the MIT Liscense.
# https://github.com/cswl/tsu/blob/v3.x/LICENSE-MIT

import subprocess

from pathlib import Path
from . import consts

from .conlog import Conlog

conlog = Conlog(__name__, level=Conlog.DEBUG)


def linux_execve(cmd, args, env=None):
    exec = [cmd] + args
    subprocess.run(exec, env=env)


@conlog.fn
def magisk_call(console, shell, env):
    argv = ["su", "-s", shell]
    console.debug(argv)
    linux_execve(consts.MAGISK_BINARY, argv)


@conlog.fn
def su_call(console, su, shell, env):
    argv = ["su", "-s", shell]
    console.debug(argv)
    linux_execve(su, argv)


def su_params(shell, preserve=True):
    return f"-s {shell} --preserve-environment"
