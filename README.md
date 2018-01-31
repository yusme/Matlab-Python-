b# Matlab-Python

## Install engine Matlab Engine API for Python

### Technical requirements
  - Python and MATLAB R2014b or later. 
 - Find the path to the MATLAB folder: Start MATLAB and type matlabroot in the command window. 



### [Installation of Matlab engine API for Python](https://de.mathworks.com/help/matlab/matlab-engine-for-python.html) 


Once you checked out, run this in a Terminal window to go to the folder that contains the engine API,
and to install it:

```bash
cd %PROGRAMFILES%/MATLAB/R2015b/extern/engines/python
python setup.py build --build-base=%TEMP% install
```

###  


