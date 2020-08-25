README.txt

Every Domain has something called an Answer (A) record, it is the IP address assigned to a domain,
this IP address must be within the companies IP range.

An IP range is a dedicated range a company buys to host devices and services inside of the range to 
prove it belongs to them.

typical IP range example: 11.134.0.2 -> 11.134.0.255

typical DNS A record example: 11.134.0.74 (resides within the range)

bad example of DNS A record: 156.55.85.245 (outside the range - untrusted host.)

Security issues:
1. This can allow attackers to manipulate the domain to trick users
2. Make malicious changes (inject skimmers, JS or Malware)
3. Damage the reputation of the organization.

Fixes: Create an automation system that automatically checks to see if the DNS A record is in range
and alert the person in charge if it ever falls out of range. - This is what my program does.

This code was uploaded to AWS Lambda and used with CloudWatch as well as Simple Notification service (SNS)
to send me emails whenever it falls out of range.