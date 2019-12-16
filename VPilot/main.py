# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:09:47 2019

@author: zhaoj
"""

import socket
import json

import client as clnt
import messages as msgs


target_host = 'localhost'
target_port = 8000
dataset_path = None#'./'

client = clnt.Client(ip=target_host, port=target_port, datasetPath=dataset_path)

def csend(*args, **kwargs):
    return client.sendMessage(*args, **kwargs)

def crecv(*args, **kwargs):
    return client.recvMessage(*args, **kwargs)

m_start_basic = msgs.Start()
m_start_longrange = msgs.Start(scenario=msgs.Scenario(camPos=[0, -18, 10], camRot=[0, 0, 0]))
m_start_cam = msgs.Start(scenario=msgs.Scenario(camPos=[0, -5, 9], camRot=[-13, 0, 0]))

m_stop = msgs.Stop()

m_cmd_static = msgs.Commands(0, 0, 0)
m_cmd_fw1 = msgs.Commands(1, 0, 0)
m_cmd_fw2 = msgs.Commands(2, 0, 0)
m_cmd_lt1 = msgs.Commands(1, 0, -0.5)
m_cmd_rt1 = msgs.Commands(1, 0, +0.5)
















































