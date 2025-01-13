# jacob-os-version-check 
This package is designed for those who want to check their server version.                                              I will be updating this package to include features for Windows and Mac.                                                If anyone encounters issues with this package, please feel free to leave a message.
This version is clearer and more polished. Let me know if you need further adjustments!

# Development enviroment setting
``` bash

# install PDM
# git clone ... 
$ source .venv/bin/activate
$ pdm install
# $ vi .... (coding)

# TEST
$ pdm install
$ pdm test
$ pip install . 

$ git add  <file_name>
$ git commit -a
$ git push
$ pdm publish
```

# Usage
```python
$ pip install jacob_os_version_check
$ python
>>> from jacob_os_version_check.hi import hi
>>> hi()
```
