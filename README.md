# PyCidrNet

Python utility for exploring subnets

----

### Requirements

This script was written for Python 2.7 and requires the ipaddr module
`pip install ipaddr` (Requires sudo if not in virtualenv)

As of now this script has only been tested on Debian Jessie (8).

### Contributing

I am not accepting contributions just yet unless I personally know you. 

Issues, however, are welcomed and encouraged.

### Usage

This tool helps you determine how many smaller subnets can fit in a larger one, and those subnet's CIDRs.

Ex.

```
$ .pycidrnet.py 10.0.0.0/23
Subnets that fit into [10.0.0.0/23]:
===================================
[2] hosts with [/24] (diff of 1)
--10.0.0.0/24
--10.0.1.0/24
[4] hosts with [/25] (diff of 2)
--10.0.0.0/25
--10.0.0.128/25
--10.0.1.0/25
--10.0.1.128/25
[8] hosts with [/26] (diff of 3)
--10.0.0.0/26
--10.0.0.64/26
--10.0.0.128/26
--10.0.0.192/26
--10.0.1.0/26
--10.0.1.64/26
--10.0.1.128/26
--10.0.1.192/26
[16] hosts with [/27] (diff of 4)
--10.0.0.0/27
--10.0.0.32/27
--10.0.0.64/27
--10.0.0.96/27
--10.0.0.128/27
--10.0.0.160/27
--10.0.0.192/27
--10.0.0.224/27
--10.0.1.0/27
--10.0.1.32/27
--10.0.1.64/27
--10.0.1.96/27
--10.0.1.128/27
--10.0.1.160/27
--10.0.1.192/27
--10.0.1.224/27
```

Additionally you can use the `-d` argument to explore CIDRs that have a higher difference than `4` from the base CIDR. 

Ex.
```
$ .pycidrnet.py 10.0.0.0/23 -d 5
Subnets that fit into [10.0.0.0/23]:
===================================
[32] hosts with [/28] (diff of 5)
--10.0.0.0/28
--10.0.0.16/28
--10.0.0.32/28
--10.0.0.48/28
--10.0.0.64/28
--10.0.0.80/28
--10.0.0.96/28
--10.0.0.112/28
--10.0.0.128/28
--10.0.0.144/28
--10.0.0.160/28
--10.0.0.176/28
--10.0.0.192/28
--10.0.0.208/28
--10.0.0.224/28
--10.0.0.240/28
--10.0.1.0/28
--10.0.1.16/28
--10.0.1.32/28
--10.0.1.48/28
--10.0.1.64/28
--10.0.1.80/28
--10.0.1.96/28
--10.0.1.112/28
--10.0.1.128/28
--10.0.1.144/28
--10.0.1.160/28
--10.0.1.176/28
--10.0.1.192/28
--10.0.1.208/28
--10.0.1.224/28
--10.0.1.240/28
```

----
