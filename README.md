b# Matlab-Python

## Install engine Matlab Engine API for Python

### Technical requirements
 1 - Python and MATLAB R2014b or later.
 2-  Matlab engine API for Python 
 2-  Find the path to the MATLAB folder: Start MATLAB and type matlabroot in the command window. 
 

### Installation of engine API


Once you checked out, run this in a Terminal window to go to the folder that contains the engine API,
and to install it:

```bash
cd %PROGRAMFILES%/MATLAB/R2015b/extern/engines/python
python setup.py build --build-base=%TEMP% install
```

### Installation 

