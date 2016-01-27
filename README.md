# TiebaManager
Auto manage tool for baidu tieba .

There are still many unexcept situations unhandled , just a simple and crude demo to do basic job.

## Requirements
* Python3
* Requests module
* beautifulsoup4 module
* redis
* python redis module

Tested in only linux .

## Install

After you satisfy the requirements

### Step 0
```
$ git clone https://github.com/KIDJourney/TiebaManager
```
### Step 1
Edit config.ini to add your cookie and bar . Then
```
$ mv config.example.ini config.ini
```
### Step 2
```
$ python3 main.py 
```