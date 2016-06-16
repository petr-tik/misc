What is the difference between an inner join and an outer join?

An inner join produces an intersection of the 2 tables, only the rows they both have in common. Usually the default type of join in most RDBMSs. 
Similar to an intersection of 2 Sets on a Venn Diagram

Outer join (right, left, outer)
produces a logical union of the tables, where 
left will include all rows of the first table and common rows from the second,
right will include all rows of the second table and only common rows from the first, 
all - include inclusive OR of table columns. Some RDBMS only support LEFT OUTER JOINS, without any support for Right or Full outer joins. 

## Stored procedures

Stored procedures are subroutines stored in Relational Database Management Systems are used to save and exposes a frequently used set of quieries for a wide set of customers. The advantages include giving API endpoints and/or access rights to different people across the organisation. 

Precompilation and being stored in the database engine minimises overhead and network traffic respectively. The business advantages include: verbalising frequently used business logic for which you can provide an API endpoint and giving access rights to such procedures and/or endpoints for users, who, otherwise, have no access rights to the database. 

The disadvantages are mostly related to tooling, vendor-lock and migration. Different vendors provide different DSLs, debuggers and version control systems to write stored procedures, thus locking the system into the vendor's product line. Differences in syntax and functionality might only worsen the vendor lock-in.

When migrating to a different system a script needs to pull out all stored procedures and translate them to the new DSL (if different) manually, test them against the results of previous database QL and save it in the new database engine. 


## Temporary tables

Temporary tables is a feature in some RDBMS to store and process intermediate results of selection, update and join operations on usual SQL tables. They are started and terminated with each database connection and are not stored on server like stored procedures.

The advantage is the ability to create business logic on-the-fly without saving anything on the database engine. 

Systems Qs

2. Troubleshoot network connectivity

Windows and linux 
Linux - run a telnet test


Verify the website status with the telnet command to check # telnet IP_Address port. Also, run tracert to check the SPF and latency of the website.
Check whether FQDN is resolving by the DNS server with # nslookup IP_Address. Most of the time the DNS server will find the culprit and resolve the FQDN hostname.
Check the server for slow performance, or whether it’s running out of CPU, RAM, and Disk with the ‘top’ command.

4. How do you find out more information on Linux commands?
Use the unix terminal man command to find out more about different functions and their option flags. 

in terminal:
man <command> for the full page
eg. 
man man gives you information about the man command
or 
man <command> | grep "{pattern}" if you are looking for a particular keyword, regex pattern
eg. 
man man | grep -A 5 "-k" gives you information about the man command with -k flag (apropos)
