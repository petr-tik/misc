## What is the difference between an inner join and an outer join?

An inner join produces an intersection of the 2 tables, only the rows they both have in common. Usually the default type of join in most RDBMSs. 
Similar to an intersection of 2 Sets on a Venn Diagram

Outer join (right, left, outer)
produces a logical union of the tables, where 
left will include all rows of the first table and common rows from the second,
right will include all rows of the second table and only common rows from the first, 
all - include inclusive OR of table columns. Some RDBMS only support LEFT OUTER JOINS, without any support for Right or Full outer joins. 

## What are stored procedures? How are they used and when are they good and bad?

Stored procedures are subroutines stored in Relational Database Management Systems are used to save and exposes a frequently used set of queries for a wide set of customers. The advantages include giving API endpoints and/or access rights to different people across the organisation. 

Precompilation and being stored in the database engine minimises overhead and network traffic respectively. The business advantages include: verbalising frequently used business logic for which you can provide an API endpoint and giving access rights to such procedures and/or endpoints for users, who, otherwise, have no access rights to the database. 

The disadvantages are mostly related to tooling, vendor lock-in and difficulty in migrating to different db providers. Different vendors provide different DSLs, debuggers and version control systems to write stored procedures, thus locking the system into the vendor's product line. Differences in syntax and functionality might only worsen the vendor lock-in.

When migrating to a different system a script needs to pull out all stored procedures and translate them to the new DSL (if different) manually, test them against the results of previous database QL and save it in the new database engine. 


## What are temporary tables? How are they used and when are they good and bad?

Temporary tables is a feature in some RDBMS to store and process intermediate results of selection, update and join operations on usual SQL tables. They are started and terminated with each database connection and are not stored on server like stored procedures.

The advantage is the ability to create business logic on-the-fly without saving anything on the database engine. Using the same sort, select, filter and join functionality without the logging and locking overhead means temporary tables allow exploratory work with the db, without worrying about overwriting in the main database. 

Temporary tables are an exploratory tool, which disallows the user to update the table (no update, insert or delete statements). 

## What is the transaction log and why is it important? 

A transaction log inside a RDBMS is a linked-list like plaintext file that records changes to the database, which might need to be reviewed in case of crashes and/or hardware failures. Due to SQL design and ACID compliance transaction log is a compulsory part of most RDBMS with different implementation. PostgreSQL postmaster spins up a different process for write-ahead logging (WAL), which only changes data files after the upcoming changes have been logged. Even if a transaction fails, the logs have already recorded what was going to happen, so a playback can be started.

Transaction logs are important, because they keep enough information to track and undo database changes in chronological order. This, combined with the db data file, allows rolling back and recovering back to any recorded state of the database. 

## What is an index? How are they used and why are they important? 

A database index is a data structure that improves the speed of data retrieval operations on a database table but takes up additional writes and storage space to maintain the index record. 

You can sort a number of records on multiple fields with a precomputed index. Creating an index on a field in a table creates another data structure which holds the field value, and pointer to the record it relates to. This index structure is then sorted, allowing searching over it and retrieve records in less time. They are an important way to speed up frequent retrieval operations, when the number of writes and disk space the index takes up is compensated by the speed increase. 

Systems Qs

## 1 How do you look at the disk utilisation on a Linux host? 

Use the df command in terminal. 

df -a 
gives information about all file systems
df -h
gives information in human readable form


## 2. Troubleshoot network connectivity

Windows and linux 
Linux - run a telnet test


Verify the website status with the telnet command to check # telnet IP_Address port. Also, run tracert to check the SPF and latency of the website.
Check whether FQDN is resolving by the DNS server with # nslookup IP_Address. Most of the time the DNS server will find the culprit and resolve the FQDN hostname.
Check the server for slow performance, or whether it’s running out of CPU, RAM, and Disk with the ‘top’ command.

## 3. What is the difference between a full, incremental and differential (cumulative differential) backup and why/when would you use them?

Full back up - complete copy of the entire data. Provide the biggest protection, but require most time and disk space

Incremental back up - the time optimised alternative to a full back up. Only back up the files that have been changed since the last back up (full or partial). Quicker and less data to write, which gives time precision and granularity and makes it time consuming to restore, need to start from the data point and go to the desired time point in sequential manner. 

Differential back up - A differential backup backs up only the files that changed since the last full back. This writes more data per backup than an incremental method, but makes restores possible from 2 data points: last full backup + a differential backup between day X and the last full back up.  


## 4. How do you find out more information on Linux commands?

in terminal:
man <command> for the full page
<command> --help  - provides a cheat sheet of different flag options

eg. 
man man gives you information about the man command
or 
man <command> | grep "{pattern}" if you are looking for a particular keyword, regex pattern
eg. 
man man | grep -A 5 "-k" gives you information about the man command with -k flag (apropos)
