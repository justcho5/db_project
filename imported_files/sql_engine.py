#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:20:57 2018

@author: florian
"""

from sqlalchemy import create_engine
import logging


# import cx_Oracle

##oracle connection
# ip = 'diassrv2.epfl.ch'
# port = 1521
# SID = 'orcldias'
# dsn_tns = cx_Oracle.makedsn(ip, port, SID)
# db = cx_Oracle.connect('DB2018_G17', 'DB2018_G17', dsn_tns)

def get_engine():
    return get_engine_for_oracle_localhost()

def get_engine_sql_lite():
    # sqlalchemy engine for connection
    engine = create_engine('sqlite:///database.db');
    return engine


def get_engine_for_oracle():
    # sqlalchemy engine for connection
    # so that we see the sql statements
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    engine = create_engine(
        get_oracle_connection()
    )
    return engine


def get_engine_for_oracle_localhost():
    # sqlalchemy engine for connection
    # so that we see the sql statements
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    engine = create_engine(
        'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'.format(
            username='system',
            password='oracle',
            hostname='localhost',
            port='49161',
            database='xe',
        ))
    return engine


def get_oracle_connection():
    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'
    return oracle_connection_string.format(
        username='DB2018_G17',
        password='DB2018_G17',
        hostname='diassrv2.epfl.ch',
        port='1521',
        database='orcldias',
    )

def chunkify(lst,n):
    return [ lst[i::n] for i in range(n) ]

