# Copyright (c) 2019, Cswl Coldwind <cswl1337@gmail.com
# This software is licensed under the MIT Liscense.
# https://github.com/cswl/tsu/blob/v3.x/LICENSE-MIT

from pathlib import Path

# Defaults in Termux and Android
TERMUX_FS = "/data/data/com.termux/files/"
TERMUX_PREFIX = f"{TERMUX_FS}/usr"
TERMUX_PATHS = f"{TERMUX_PREFIX}/bin:{TERMUX_PREFIX}=/bin/applets"
ROOT_HOME = "/data/data/com.termux/files/root"
SYS_SHELL = "/system/bin/sh"
ANDROIDSYSTEM_PATHS = "/system/bin:/system/xbin"

# Superuser config
MAGISK_BINARY = Path("/sbin/magisk")
SU_BINARY = [
    Path(p)
    for p in ['/su/bin/su'
              '/sbin/su'
              '/system/xbin/su'
              '/system/bin/su']
]
