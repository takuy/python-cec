#!/usr/bin/env python

from distutils.core import setup, Extension

# Remove the "-Wstrict-prototypes" compiler option, which isn't valid for C++.
import distutils.sysconfig
cfg_vars = distutils.sysconfig.get_config_vars()
if "CFLAGS" in cfg_vars:
    cfg_vars["CFLAGS"] = cfg_vars["CFLAGS"].replace("-Wstrict-prototypes", "")
if "OPT" in cfg_vars:
    cfg_vars["OPT"] = cfg_vars["OPT"].replace("-Wstrict-prototypes", "")

python_cec = Extension('cec', sources = [ 'cec.cpp', 'device.cpp'], 
                        include_dirs=['include'],
                        library_dirs = ['C:\\Program Files (x86)\\Pulse-Eight\\USB-CEC Adapter'],
                        library = ['cec'])

setup(name='cec', version='0.2.7',
      description="Python bindings for libcec",
      license='GPLv2',
      data_files=['COPYING'],
      ext_modules=[python_cec])
