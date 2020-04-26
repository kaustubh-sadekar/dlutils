# dlutils
This repository contains a small collection of utility functions.

# Installing the library in colab
```shell
!git clone https://github.com/kaustubh-sadekar/dlutils.git
!sudo python3 dlutils/setup.py install
```

# Example code for testing in colab
```python
import sys
sys.path.append("dlutils/")
import kdlutils
input_dim = (1,600,800)
layersList = [{'conv':(1,7,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(7,14,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(14,30,3,1,1,1)},{'mp':(2,2,0,1)}]
out = kdlutils.kdlutils.getOutShape(input_dim,layersList)
print(out)
```
Documentation and new codes will be uploaded soon.
