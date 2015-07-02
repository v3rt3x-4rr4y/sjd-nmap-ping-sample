#!/usr/bin python

'''
    File name          : sjd-nmap-ping-sample.py
    Author             : Spencer Drayton
    Date created       : 02 July 2015 14:30:23
    Date last modified : 02 July 2015 14:30:23
    Python Version     : 2.7
    Dependencies       : libnmap (https://github.com/savon-noir/python-libnmap)
    Description        : Generate a randomised sample of live host IP addresses from the supplied \
                         network range, e.g: python sjd-nmap.py -p 10 -s test -r 192.168.0.0/24 \
'''


import os
import sys
import argparse
import random
from time import sleep
from datetime import datetime

# Sanity check
try:
        
        from libnmap.process import NmapProcess
        from libnmap.parser import NmapParser
except ImportError:
        print "ERROR: Cannot import libnmap - is it installed ? Exiting..."
        sys.exit(0)

# Parse supplied arguments
parser = argparse.ArgumentParser(description="Generate a randomised sample of live host IP addresses from the supplied \
                                              network range, e.g: python sjd-nmap.py -p 10 -s test -r 192.168.0.0/24")
parser.add_argument("-p","--percentage", help="percentage of total hosts required (integer)", required=True)
parser.add_argument("-s","--prefix", help="The string to prefix the generated filenames with", required=True)
parser.add_argument("-r","--range", help="The network range to scan", required=True)
args = vars(parser.parse_args())
samplepc = None
try:
        samplepc = float(args["percentage"])
except:
        print "ERROR: Can't parse %s as a percentage, exiting..." % (args["percentage"])
        sys.exit(0)
if not samplepc or samplepc < 1 or samplepc > 100:
        print "ERROR: invalid percentage value, exiting..."
        sys.exit(0)

# Start the scan - ping sweep, no DNS
print "Nmap ping sweep: %s..." % (args["range"])
nmap_proc = NmapProcess(targets=args["range"], options="-sP -n")
nmap_proc.run_background()
while nmap_proc.is_running():
        print "...%s%% done" % (nmap_proc.progress)
        sleep(2)
print nmap_proc.summary

# Parse the results
nmap_report = NmapParser.parse(nmap_proc.stdout)
if nmap_report.hosts_up < 1:
        print "No hosts up ! Exiting..."
        sys.exit(0)

sample_size = int(round(nmap_report.hosts_up * 0.01 * samplepc))
up_hosts = [host for host in nmap_report.hosts if host.is_up()]
sample_hosts = [up_hosts[i] for i in sorted(random.sample(xrange(len(up_hosts)), sample_size))]

# Write out the master and sample host lists to disk
print "Writing files...",
suffix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
master_filename = os.path.join(os.getcwd(), "%s_pingsweep-master-%s.txt" % (args["prefix"], suffix))
sample_filename = os.path.join(os.getcwd(), "%s_pingsweep-sample-%s.txt" % (args["prefix"], suffix))
try:
        master_outfile = open(master_filename,"w")
        for up_host in up_hosts:
                master_outfile.write("%s\n" % up_host.ipv4)
        master_outfile.close()
        sample_outfile = open(sample_filename,"w")
        for sample_host in sample_hosts:
                sample_outfile.write("%s\n" % sample_host.ipv4)
        sample_outfile.close()
        print "done."
        print "Sample host list written to: %s" % (sample_filename)
        print "Master host list written to: %s" % (master_filename)
except IOError:
        print "ERROR: cannot write file to disk, exiting..."
        sys.exit(0)
