import sys
import paramiko
import socket
import os
import subprocess

upAddresses = []
ipAddressRange = "10.0.0."


def getIpAddresses():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for counter in range (1,255):
        address = ipAddressRange + str(counter)
        response = os.system('ping ' + str(address) + " -n 1 " + '| find '  + '"Reply" '  "> nul")
        if response == 0:
            upAddresses.append(counter)
    
    

def connect():
    for counter in range(0,len(upAddresses)):
        ipAddress = (ipAddressRange +  str(upAddresses[counter]))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ipAddress)
        client.exec_command('admin')
        client.exec_command('netlab')



def output():
    for counter in range(0,len(upAddresses)):
        print("up addresses", upAddresses[counter])

getIpAddresses()
#connect()
#output()

