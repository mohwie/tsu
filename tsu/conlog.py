# Copyright (c) 2019, Cswl Coldwind <cswl1337@gmail.com
# This software is licensed under the MIT Liscense.
# https://github.com/cswl/tsu/blob/v3.x/LICENSE-MIT

import logging
import subprocess

import functools
"""
 Conlog : A console.log for Python

conlog = Conlog(__name, enabled=True)

 @conlog.fn
 def cli(console) :
    console.log("Hello world");

"""


class Conlog():
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NONE = 0

    def fn(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            console = self
            console.debug = functools.partial(self.__debug, func.__name__)
            val = func(console, *args, **kwargs)
            return val

        return wrapper

    def __init__(self, module, enabled=True, level=NONE):
        self.module = module
        self.enabled = enabled
        self.level = level
        self.logger = logging.getLogger(module)
        self.logger.setLevel(level)
        self.sh = logging.StreamHandler()
        self.logger.addHandler(self.sh)

    def __debug(self, func, msg):
        format = f"{self.module}:{func}  {msg}"
        self.logger.debug(format)
