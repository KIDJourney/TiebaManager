# TiebaManager

Auto manage tool for baidu tieba.

## Requirements

* Python3
* Requests module
* beautifulsoup4 module
* python redis module
* redis

Tested only in *linux*.

## Install

After you satisfy the requirements.
Make sure your Redis has the default configuration.

### Step 0

Clone the Repo.
```
$ git clone https://github.com/KIDJourney/TiebaManager
```

### Step 1
Edit ```config.example.ini``` to add your cookie and managed bar. Then rename to ```config.ini```.
```
$ gedit config.example.ini 
$ mv config.example.ini config.ini
```

### Step 2
Run the main file.
```
$ python3 main.py 
```
You can use ```Tmux``` or something similar to run it in backgroud.


## Feature

### Delete post

Use this tool to judge and delete post.

### Delete reply

Use this tool to judge and delete replies of post.

### Dynamic reload judge methods .

You can edit the methods you want to use while the program is running.

### Ban

This feature is not completely implemented , ban reply author may cause unexcpeted result.

## Judge Method

You can implement your own judge method in ```judgemethods.py```.

There are two kinds of methods you can write yourself.

### Post judge method

The method is implemented as a function . Accept a ```Post``` object as an argument.

Make sure you register your method with the ```post_method``` decorator.

### Reply judge method

The method is implemented as a function . Accept a ```Reply``` object as an argument.

Make sure you register your method with the ```reply_method``` decorator.

## Warning

The Project is still in develop , some of code may be refactored frequently.

## Licenses

[Apache licenses](http://choosealicense.com/licenses/apache-2.0/)