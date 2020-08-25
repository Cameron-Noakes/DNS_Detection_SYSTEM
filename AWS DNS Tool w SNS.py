
import dns.resolver
import ipaddress
import boto3

def handler(a,b):

    client = boto3.client(
        "sns",
        aws_access_key_id = "<my secret key>",
        aws_secret_access_key = "<my secret key>",
        region_name = "us-east-2"
        )
        
    client.publish(
        TopicArn = "arn:aws:sns:us-east-2:686688756380:dns_tooling",
        Message = "Warning! <domain name> A record is outside of range."
        )

    IP_range1_start = ipaddress.ip_address('23.185.0.0')
    IP_range1_end = ipaddress.ip_address('23.185.0.255')


    IP_range1 = []

    while IP_range1_start != IP_range1_end:
        IP_range1_start +=1
        IP_range1.append(IP_range1_start)


    # A records
    A = dns.resolver.resolve("<domain name>", 'A')
    for i in A.response.answer:
        for j in i.items:
            A_record = j.to_text() #to test recieve emails: ipaddress.ip_address('23.185.1.1')
            print ("IP Answer (A) record:",A_record)
        
        

    for item in IP_range1:
        if A_record == item:
            print ("The DNS A record for the domain is in the IP address range. ")
            break
    
        elif A_record == "23.185.0.1":
            print ("The DNS A record for the domain is in the IP address range. ")
            break

        else:
            print ("WARNING! DNS A record isn't in the range - hosted elsewhere...")
            break


