# log-analysis-project
this is a python program that run reports against a psql database which is located on a virtualmachine.

## Prerequisites
 Download the following softwares and files
 - download the lates version of python form [here](https://www.python.org/downloads/)
 - download the latest version of virtual box from [here](https://www.virtualbox.org/wiki/Downloads)
 - download the latest version of vagrant from[here](https://www.vagrantup.com/downloads.html)
 - download the vm configuraion [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
 - download the database file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 - download newsanalysis.py file.
 ## how to setup the environment
 - open the terminal
 - go to the directory vm configuration downloaded file.
 - go to vagrant folder
 - then```vagrant up
          vagrant ssh```
          
 ## how to run
 - After starting up Vagrant navigate to the location of your newsdata.sql file. you will now  load all the tables in the database. 
   Run this command:
   ` psql -d news -f newsdata.sql`
 - now run the file 
   `python newsanalysis.py`
  
  
  
  
  
  
 ### The output of running that command will produce three reports that answer the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

 


