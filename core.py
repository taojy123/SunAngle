#coding=utf8

import time
import datetime
import math

#print "====== Sun Angle ======"

def hours(t):
    return t.hour + t.minute / 60.0 + t.second / 3600.0

def show_radians(r):
    if r < 0:
        flag = True
    else:
        flag = False
    r = abs(r)
    seconds = r * 3600
    hours = int(seconds / 3600)
    minutes = int(seconds % 3600 / 60)
    seconds = int(seconds % 60)
    s = u"%d°%d′%d″"%(hours, minutes, seconds)
    if flag:
        s = "-" + s
    return s

def get_radians(s):
    if s[0] == "-":
        flag = True
    else:
        flag = False
    s = s.replace(u"°", u"|").replace(u"′", u"|").replace(u"″", u"|").replace(u"'", u"|").replace(u'"', u"|")
    s = s.split(u"|")
    if len(s) > 2:
        hours = abs(int(s[0]))
        minutes = int(s[1])
        seconds = int(s[2])
    else:
        hours = abs(float(s[0]))
        minutes = 0
        seconds = 0
    r = hours + minutes / 60.0 + seconds / 3600.0
    if flag:
        r = 0 - r
    return r

def show_time(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")


def get_sun(E, N, now=None):

    E = get_radians(E)
    N = get_radians(N)
    if not now:
        now = datetime.datetime.now()

    #print E
    #print N
    #print show_time(now)

    #now = now - datetime.timedelta(seconds=50)

    n = int(now.strftime("%j"))

    t_ping = now + datetime.timedelta(minutes=4*(E-120))
    #print show_time(t_ping)

    t_zhen = t_ping - datetime.timedelta(minutes=15)
    #print show_time(t_zhen)

    t_bei = hours(now)
    t_delta = hours(t_zhen)
    t_wei = 12 * (E - 120) / 180.0
    #print t_bei, t_delta, t_wei

    t = (t_bei + t_delta + t_wei) * 180 / 12.0 - 180
    #print t

    b = 23.45 * math.sin(2 * math.pi * (284 + n) / 365.0)
    #print b

    sin_a = math.sin(math.radians(N)) * math.sin(math.radians(b)) + math.cos(math.radians(N)) * math.cos(math.radians(b)) * math.cos(math.radians(t))
    #sin_a = math.sin(N) * math.sin(b) + math.cos(N) * math.cos(b) * math.cos(t)
    #print sin_a

    a = math.asin(sin_a)
    a = a * 180.0 / math.pi
    a = u"%.3f°" % a 

    tan_m = math.tan(math.radians(b)) / math.cos(math.radians(t))
    m = math.atan(tan_m)
    m = m * 180.0 / math.pi

    tan_c = 0 - math.tan(math.radians(b)) * math.cos(math.radians(m)) * 1.0 / math.sin(math.radians(m-N)) 
    c = math.atan(tan_c)
    c = c * 180.0 / math.pi


    if m < N:
        c = c + 180
    else:
        if t > 0:
            c = c + 360

    c = u"%.3f°" % c 


    return (a, c)



if __name__ == "__main__":

    E = u"110°18′21″"
    N = u"25°19′41″"
    now = time.strptime("2014-08-08 16:46:00", "%Y-%m-%d %H:%M:%S")
    now = time.strptime("2014-08-11 10:50:00", "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.fromtimestamp(time.mktime(now))

    a, c = get_sun(E, N, now)

    print "================"
    print a, c