#!/usr/bin/env python
'''
  Quick subnet calculator
 
  Charles Corbett <nafredy@gmail.com>
'''

try:
  from ipaddr import IPNetwork
except ImportError:
  print "Please run (pip install ipaddr)"
import argparse

parser = argparse.ArgumentParser(description="Quick IP CIDR calculator using ipaddr & IPNetwork modules.")

parser.add_argument('CIDR', help="ex. 10.0.0.0/16")
parser.add_argument('-d', '--diff', type=int, help="If you need to see more than +4 from your starting CIDR, enter it here. ex if you are using 10.0.0.0/23 and want to see /28 enter [5].")

args = parser.parse_args()

def calcSubnet(cidr, positional=1):
  net = IPNetwork(args.CIDR)
  try:
    subnet = list(net.subnet(positional))
  except ValueError:
    finalcidr = int(cidr.split('/')[1]) + positional
    print "[%s] is out of range with [%s] positions away (A /%s, seriously?). Cannot calculate." % (cidr, positional, finalcidr)
    raise SystemExit

  newcidr = subnet[0].prefixlen
  count = len(subnet)

  print "[%s] hosts with [/%s] (diff of %s)" % (count, newcidr, positional)
  for i in subnet:
    print "--%s" % i





print "Subnets that fit into [%s]:" % (args.CIDR)
print '='*35

if args.diff:
  calcSubnet(args.CIDR, args.diff)
else:
  inc = 1
  while inc <= 4:
    calcSubnet(args.CIDR, inc)
    inc += 1

