# -*- coding:utf-8 -*-
import configparser

config = configparser.ConfigParser()
config.read('conf.ini',encoding='UTF-8')

def GetConfig():
  for i in config:
    for t in i:
      t = str(t)
  return config