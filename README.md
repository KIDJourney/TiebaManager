# TiebaManager
Auto manage tool for baidu tieba .

There are still many unexcept situations unhandled , just a simple and crude demo to do basic job.

## Requirements
* Python3
* Requests moudle
* beautifulsoup4
* configparser
* lxml

Tested in only linux .
## Install

### Step 0
```
$ git clone https://github.com/KIDJourney/TIebaManager
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

## Judge Method

You can implement your own judge method in judgemethod.py or your own file .
Be Sure you class implement judge method of judgemethod.JudgeBase .

## Warning

The Project is still in develop , some of code may be refactored frequently.