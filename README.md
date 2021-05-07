# openconfig-xpaths-dump

## steps to get all dumps

* install pyang

`pip3 install pyang`

* clone openconfig repo and go to 

`git clone https://github.com/openconfig/public` 

`cd public/release/models`

* mkdir plugins

`mkdir plugins`

* get plugin in from https://github.com/NSO-developer/pyang-xpath

`Copy content of https://raw.githubusercontent.com/NSO-developer/pyang-xpath/master/xpath.py to plugins/xpath.py`

* run script in current folder

`python3 script.py`

