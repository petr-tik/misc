What is the difference between an inner join and an outer join?

An inner join produces an intersection of the 2 tables, only the rows they both have in common. 
Similar to an intersection of 2 Sets on a Venn Diagram

Outer join (right, left, outer)
produces a logical union of the tables, where 
left will include all rows of the first table and common rows from the second,
right will include all rows of the second table and only common rows from the first, 



Systems Qs

2. Troubleshoot network connectivity

Windows and linux 
Linux - run a telnet test


Verify the website status with the telnet command to check # telnet IP_Address port. Also, run tracert to check the SPF and latency of the website.
Check whether FQDN is resolving by the DNS server with # nslookup IP_Address. Most of the time the DNS server will find the culprit and resolve the FQDN hostname.
Check the server for slow performance, or whether it’s running out of CPU, RAM, and Disk with the ‘top’ command.

4. How do you find out more information on Linux commands?

in terminal:
man <command> for the full page
eg. 
man man gives you information about the man command
or 
man <command> | grep "{pattern}" if you are looking for a particular keyword, regex pattern
eg. 
man man | grep -A 5 "-k" gives you information about the man command with -k flag (apropos)
