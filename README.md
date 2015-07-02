# Description #

* Generates a randomised sample of live host IP addresses from the supplied network range.
* Writes out two files: one containing the master list of live hosts, one containing a random subset of live hosts of the requested sample size.

## Example ##

```
#!python

python sjd-nmap-ping-sample.py -p 10 -s test -r 192.168.0.0/24

-p 10 (provide a 10 percent sample of live hosts selected at random).
-s test (prefix the output files with the string 'test').
-r 192.168.0.0/24 (ping sweep the network range '192.168.0.0/24' with nmap).

sample output:

banana@monkey ~/Development/scratch/python/sjd-nmap-ping-sample $ python sjd-nmap-ping-sample.py -p 50 -s test -r 192.168.0.0/24
Nmap ping sweep: 192.168.0.0/24...
...0% done
...29.39% done
Nmap done at Thu Jul  2 15:41:11 2015; 256 IP addresses (6 hosts up) scanned in 2.34 seconds
Writing files... done.
Sample host list written to: /home/banana/Development/scratch/python/sjd-nmap-ping-sample/test_pingsweep-sample-02-07-2015_15:41:13.txt
Master host list written to: /home/banana/Development/scratch/python/sjd-nmap-ping-sample/test_pingsweep-master-02-07-2015_15:41:13.txt
banana@monkey ~/Development/scratch/python/sjd-nmap-ping-sample $ ls -al *.txt
-rw-r--r-- 1 banana banana 77 Jul  2 15:41 test_pingsweep-master-02-07-2015_15:41:13.txt
-rw-r--r-- 1 banana banana 39 Jul  2 15:41 test_pingsweep-sample-02-07-2015_15:41:13.txt
banana@monkey ~/Development/scratch/python/sjd-nmap-ping-sample $ cat test_pingsweep-master-02-07-2015_15\:41\:13.txt 
192.168.0.1
192.168.0.14
192.168.0.24
192.168.0.27
192.168.0.37
192.168.0.38
banana@monkey ~/Development/scratch/python/sjd-nmap-ping-sample $ cat test_pingsweep-sample-02-07-2015_15\:41\:13.txt 
192.168.0.14
192.168.0.24
192.168.0.37
```

## Dependencies ##
libnmap ([https://github.com/savon-noir/python-libnmap](https://github.com/savon-noir/python-libnmap))