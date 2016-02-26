# TiebaManager
Auto manage tool for baidu tieba .

There are still many unexcept situations unhandled , just a simple and crude demo to do basic job.

## Requirements
* Python3
* Requests module
* beautifulsoup4 module
* python redis module
* redis

Tested in only *linux* .

## Install

After you satisfy the requirements .
Make sure your redis has default configure .

### Step 0
Clone the Repo .
```
$ git clone https://github.com/KIDJourney/TiebaManager
```
### Step 1
Edit ```config.example.ini``` to add your cookie and managed bar . Then
```
$ mv config.example.ini config.ini
```
### Step 2
```
$ python3 main.py 
```
You can use ```Tmux``` or something similar to run it in backgroud .

## Judge Method

You can implement your own judge method in ```judgemethods.py``` .

The method is implemented as a function . Accept a ```Post``` object as argument .

Make sure you register your method with the ```__enable_method``` decorator.

## Warning

The Project is still in develop , some of code may be refactored frequently.

## Licenses
[Apache licenses](http://choosealicense.com/licenses/apache-2.0/)