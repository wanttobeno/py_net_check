
#coding:utf-8
import ping
import time
import socket
import os
import logging
import subprocess
import signal

out_ip = '100.100.2.136'
ip = '192.168.1.8'

def verbose_ping(dest_addr, timeout=2, count=4, psize=64):
    """
    Send `count' ping with `psize' size to `dest_addr' with
    the given `timeout' and display the result.
    """
    shell = 'ping  {} -c {} -w {}'.format(dest_addr, timeout, count)
    read = os.popen(shell).read()
    #print read
    read_list = read.split("\n")
    status = False
    for i in read_list :
        if 'time=' in i :
            status = True
    return status


def date_info():
  os.system('date "+%F %T"')  


def my_print(info,enable=True):
  if enable:
    print(info)

def route_info():
  # 执行成功 
  #info = os.popen('route -n').read()
  #print(info)
  # 测试成功
  os.system('route -n')


def route_restore():
  my_print('route restore')
  os.system('route del default')
  os.system('route add -net 0.0.0.0/0 gw 192.168.6.1 metric 100 dev enp2s0')


def route_add():
  my_print('route add')
  os.system('route add -net 192.168.1.0/24 gw 192.168.6.3 dev enp2s0')

def network_restore():
  my_print('network restore')
  os.system('systemctl restart network')


date_info()

status = verbose_ping(ip, timeout=4, count=3)
if status == False:
  #os.popen('route add default dev ppp0').read()
  print('net is error')
  # 添加成功
  #os.popen('route add -net 192.168.88.0/24 gw 192.168.6.3 dev enp2s0').read()
  route_info()
  route_restore()
  route_add()
  status = verbose_ping(ip, timeout=4, count=5)
  if status == False:
     network_restore()
     route_add()
     route_info()
else:
  # 测试成功
  print('net is ok')



