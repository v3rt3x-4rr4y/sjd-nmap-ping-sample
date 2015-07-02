# Description #

* Generates a randomised sample of live host IP addresses from the supplied network range.
* Writes out two files: one containing the master list of live hosts, one containing a random subset of live hosts of the requested sample size.

## Example ##

```
#!python

python sjd-nmap.py -p 10 -s test -r 192.168.0.0/24

-p 10 (provide a 10 percent sample of live hosts selected at random).
-s test (prefix the output files with the string 'test').
-r 192.168.0.0/24 (ping sweep the network range '192.168.0.0/24' with nmap).
```

## Dependencies ##
libnmap ([https://github.com/savon-noir/python-libnmap](https://github.com/savon-noir/python-libnmap))