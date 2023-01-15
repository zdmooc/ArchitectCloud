## ==================================================
## Utilisation de SQL Alchemy + SQLITE en RAM
## Usage de SQLAlchemy / csv 
## ==================================================

import os
import sys

from sqlalchemy import sql
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Numeric, BigInteger, Float
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
import datetime
import random
import csv

import psutil


## ===============================
## Creation BASE + DEFINITIONS 
## ===============================
Base = declarative_base()

class BASE_TABLE():
    " Classe commune a toute les autres"
    u_id = Column(Integer, primary_key=True)
    #d_cre = Column(DateTime, default = datetime.datetime.now() )
    #d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )
    #status = Column(String(5), default = "OK", nullable = False )

class Proc(Base, BASE_TABLE):
    "Table des Processes"
    __tablename__ = "PROC"
    pid                 = Column("pid", Integer)
    ppid                = Column("ppid", Integer)
    name                = Column("name", String(20))
    username            = Column("username", String(20))
    cmdline             = Column("cmdline", String(250))
    connections         = Column("connections", Text)
    cpu_affinity        = Column("cpu_affinity", String(20))
    cpu_num             = Column("cpu_num", Integer)
    cpu_percent         = Column("cpu_percent", Float)
    #cpu_times  = Table CPUTIME
    create_time         = Column("create_time", DateTime)
    cwd                 = Column("cwd", String(250))
    environ             = Column("environ", Text)
    exe                 = Column("exe", String(250))
    gids                = Column("gids", String(250))
    uids                = Column("uids", String(250))
    num_threads         = Column("num_treads", Integer)
    #threads => Table THREADS
    num_fds             = Column("num_fds", Integer)
    #'open_files' => Table OPENFILE
    #io_counters => Table PIO
    ionice              = Column("ionice", String(250))
    #'memory_full_info' => Table MEMORY
    #'memory_info'
    #'memory_maps'
    memory_percent      = Column("memory_percent", Float)
    nice                = Column("nice", Integer)
    num_ctx_switches    = Column("num_ctx_switches", String(250))
    status              = Column("status", String(20))
    terminal            = Column("terminal", String(20), default="<None>")

class OpenFile(Base, BASE_TABLE):
    "Table des valeurs OpenFile"
    __tablename__ = "OPENFILE"
    pid             = Column("pid", Integer)
    of_no           = Column("of_no", Integer)
    path            = Column("path", String(250))
    fd              = Column("fd", Integer)
    position        = Column("position", Integer)
    mode            = Column("mode", String(10))
    flags           = Column("flags", Integer)

class CpuTime(Base, BASE_TABLE):
    "Table des valeurs cpu_times"
    __tablename__ = "CPUTIME"
    pid             = Column("pid", Integer)
    user            = Column("user", Float)
    system          = Column("system", Float)
    children_user   = Column("children_user", Float)
    children_system = Column("children_system", Float)
    iowait          = Column("iowait", Float)

class Pio(Base, BASE_TABLE):
    "Table des valeurs PIO"
    __tablename__ = "PIO"
    pid         = Column("pid", Integer)
    read_count  = Column("read_count", Integer)
    write_count = Column("write_count", Integer)
    read_bytes  = Column("read_bytes", Integer)
    write_bytes = Column("write_bytes", Integer)
    read_chars  = Column("read_chars", Integer)
    write_chars = Column("write_chars", Integer)

class Memory(Base, BASE_TABLE):
    "Table des valeurs memoire"
    __tablename__ = "MEMORY"
    pid        = Column("pid", Integer)
    rss        = Column("rss", Integer)
    vms        = Column("vms", Integer)
    shared     = Column("shared", Integer)
    text       = Column("text", Integer)
    lib        = Column("lib", Integer)
    data       = Column("data", Integer)
    dirty      = Column("dirty", Integer)
    uss        = Column("uss", Integer)
    pss        = Column("pss", Integer)
    swap       = Column("swap", Integer)

class Thread(Base, BASE_TABLE):
    "Table des Threads"
    __tablename__ = "THREADS"
    pid             = Column("pid", Integer)
    t_no            = Column("t_no", Integer)
    t_id            = Column("t_id", Integer)
    user_time       = Column("user_time", Float)
    system_time     = Column("system_time", Float)

## ----------------------------
## Creation base en memoire
## ----------------------------

SQLITE_FILE_NAME = "PROCESS.dbf"
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME

engine = create_engine(BASE_NAME)

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


## ==========================
## Creation d'enregistrements 
## ==========================
for proc in psutil.process_iter():
    with proc.oneshot():
        p = Proc()
        pinfo = proc.as_dict(ad_value='ACCESS_DENIED')
        p.pid               = proc.pid
        p.ppid              = proc.ppid()
        p.name              = proc.name()
        p.username          = proc.username()
        p.cmdline           = str(proc.cmdline())
        p.cpu_num           = proc.cpu_num()
        p.cpu_percent       = proc.cpu_percent()
        p.create_time       = datetime.datetime.fromtimestamp(proc.create_time())
        p.cwd               = pinfo['cwd']
        p.exe               = pinfo['exe']
        p.terminal          = pinfo['terminal']
        p.status            = pinfo['status']
        p.nice              = pinfo['nice']
        p.environ           = str(pinfo['environ'])
        p.memory_percent    = pinfo['memory_percent']
        p.num_ctx_switches  = str(pinfo['num_ctx_switches'])
        p.num_threads       = pinfo['num_threads']
        p.num_fds           = pinfo['num_fds']
        if pinfo['num_fds'] != 'ACCESS_DENIED':
            if pinfo['num_fds'] > 0:
                if pinfo['open_files'] != 'ACCESS_DENIED':
                    for n, of in enumerate(pinfo['open_files']):
                        o = OpenFile()
                        o.pid               = pinfo['pid']
                        o.of_no             = n
                        o.path              = of.path
                        o.fd                = of.fd
                        o.position          = of.position
                        o.mode              = of.mode
                        o.flags             = of.flags
                        session.add(o)

        #p.io_counters       = str(pinfo['io_counters'])
        if pinfo['io_counters'] != 'ACCESS_DENIED':
            i = Pio()
            i.pid               = pinfo['pid']
            i.read_count        = pinfo['io_counters'][0]
            i.write_count       = pinfo['io_counters'][1]
            i.read_bytes        = pinfo['io_counters'][2]
            i.write_bytes       = pinfo['io_counters'][3]
            i.read_chars        = pinfo['io_counters'][4]
            i.write_chars       = pinfo['io_counters'][5]
            session.add(i)
        p.cpu_affinity      = str(pinfo['cpu_affinity'])
        if pinfo['num_threads'] > 0:
            if pinfo['threads'] != 'ACCESS_DENIED':
                for n, th in enumerate(pinfo['threads']):
                    t = Thread()
                    t.pid               = pinfo['pid']
                    t.t_no              = n + 1
                    t.t_id              = th.id
                    t.user_time         = th.user_time
                    t.system_time       = th.system_time
                    session.add(t)
        #p.cpu_times         = str(pinfo['cpu_times'])
        #user=0.09, system=0.0, children_user=0.0, children_system=0.0, iowait=0.0
        if pinfo['cpu_times'] != 'ACCESS_DENIED':
            c = CpuTime()
            c.pid               = pinfo['pid']
            c.user              = pinfo['cpu_times'][0]
            c.system            = pinfo['cpu_times'][1]
            c.children_user     = pinfo['cpu_times'][2]
            c.children_system   = pinfo['cpu_times'][3]
            c.iowait            = pinfo['cpu_times'][4]
            session.add(c)
        p.connections       = str(pinfo['connections'])
        p.ionice            = str(pinfo['ionice'])
        p.uids              = str(pinfo['uids'])
        p.gids              = str(pinfo['gids'])
        ## Memory_full_info
        #'rss', 'vms', 'shared', 'text', 'lib', 'data', 'dirty', 'uss', 'pss', 'swap'
        if pinfo['memory_full_info'] != 'ACCESS_DENIED':
            m = Memory()
            m.pid               = pinfo['pid']
            m.rss               = pinfo['memory_full_info'][0]
            m.vms               = pinfo['memory_full_info'][1]
            m.shared            = pinfo['memory_full_info'][2]
            m.text              = pinfo['memory_full_info'][3]
            m.lib               = pinfo['memory_full_info'][4]
            m.data              = pinfo['memory_full_info'][5]
            m.dirty             = pinfo['memory_full_info'][6]
            m.uss               = pinfo['memory_full_info'][7]
            m.pss               = pinfo['memory_full_info'][8]
            m.swap              = pinfo['memory_full_info'][9]
            session.add(m)
        session.add(p)
session.commit()

