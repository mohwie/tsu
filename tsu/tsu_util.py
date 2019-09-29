# Copyright (c) 2019, Cswl Coldwind <cswl1337@gmail.com
# This software is licensed under the MIT Liscense.
# https://github.com/cswl/tsu/blob/v3.x/LICENSE-MIT

import os


def add_to_path(path):
    cur_path = os.environ["PATH"]
    new_path = path + os.pathsep + cur_path
    return new_path
