# Copyright (c) 2019, Cswl Coldwind <cswl1337@gmail.com
# This software is licensed under the MIT Liscense.
# https://github.com/cswl/tsu/blob/v3.x/LICENSE-MIT

import os
import sys

import shlex, subprocess
from pathlib import Path, PurePath
from docopt import docopt

from .conlog import Conlog
from .exec import magisk_call

from . import consts

conlog = Conlog(__name__, level=Conlog.DEBUG)


def cli():
    """
    tsu A su interface wrapper for Termux

    Usage: tsu
        tsu [ -s SHELL ]  [-pe]
        tsu [ -h | --help | --version ]

    Options:
    -s <shell>   Use an alternate specified shell.
    -h --help    Show this screen.
    --version    Show version.
    """
    args = docopt(cli.__doc__)
    print(args)
    env_copy = os.environ

    CONFIG_SHELL = args.get("-s")
    if args.get("-p"):
        NEW_PATH = add_to_path(ANDROIDSYSTEM_PATHS)
    shell = get_shell(CONFIG_SHELL)
    env_copy["HISTFILE"] = hist_file(shell)

    # Check if we are on a Magisk kernel.
    if consts.MAGISK_BINARY.exists():
        magisk_call(shell, env_copy)
    else:
        su_bin = next((p for p in consts.SU_BINARY if p.exists()), None)
        su_call(su_bin, shell, env_copy)
    pass


def hist_file(shell):
    shellname = PurePath(shell).name
    histfile = Path.home() / f"{shellname}_history_root"
    return str(histfile)


def get_shell(shell):
    #if [ -n "$USER_SHELL" ]; then
    # Expand //usr/ to /usr/
    #  root_shell="$USER_SHELL_EXPANDED"
    root_shell = "$PREFIX/bin/sh"
    USER_SHELL = Path(Path.home(), ".termux/shell")
    BASH_SHELL = Path(consts.TERMUX_PREFIX, "bin/bash")
    if shell == "system":
        root_shell = consts.SYS_SHELL
    # Check if user has set a login shell
    elif USER_SHELL.exists():
        root_shell = str(USER_SHELL.resolve())
    # Or at least installed bash
    elif BASH_SHELL.exists():
        root_shell = str(BASH_SHELL)
    return root_shell
