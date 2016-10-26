# ReadComicsTV
It's a Python3 script for downloading whole comics from http://www.readcomics.tv/

## Requirements
requests - http://docs.python-requests.org/en/master/

## Usage
Open main.py in Python3.  
You have to write comic name as it is in the URL (right click on the image->View Image...).

For ex. if you want to download Deadpool 2016 issues:
```
>> python3 main.py
>> ReadComicsTV Download
>> Give comic URL name (ex. old-man-logan): deadpool-2016
```
Then you have to specify number or range of issues to download:
* 17 - downloads first 17 issues
* 5-10 - downloads issues from 5 to 10

You can then find the downloaded images inside ``downloads/comic_name/issue_number/`` folder
