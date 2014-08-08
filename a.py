#coding=utf8

import time
import datetime
import math

print "====== Sun Angle ======"

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
	s = "%d°%d′%d″"%(hours, minutes, seconds)
	if flag:
		s = "-" + s
	return s

def get_radians(s):
	if s[0] == "-":
		flag = True
	else:
		flag = False
	s = s.replace("°", "|").replace("′", "|").replace("″", "|").replace("'", "|").replace('"', "|")
	s = s.split("|")
	hours = abs(int(s[0]))
	minutes = int(s[1])
	seconds = int(s[2])
	r = hours + minutes / 60.0 + seconds / 3600.0
	if flag:
		r = 0 - r
	return r


E = 125
N = 40
now = datetime.datetime.now()

E = get_radians("110°18′21″")
N = get_radians("25°19′41″")
now = time.strptime("2014-08-08 16:46:00", "%Y-%m-%d %H:%M:%S")
now = datetime.datetime.fromtimestamp(time.mktime(now))

print "===b"

print show_radians(E)
print show_radians(N)
print now.strftime("%Y-%m-%d %H:%M:%S")

now = now - datetime.timedelta(seconds=50)

n = int(now.strftime("%j"))


t_ping = now + datetime.timedelta(minutes=4*(E-120))
t_zhen = t_ping - datetime.timedelta(minutes=15)

t_bei = hours(now)
t_delta = hours(t_zhen)
t_wei = 12 * (E - 120) / 180.0

t = (t_bei + t_delta + t_wei) * 180 / 12.0 - 180


b = 23.45 * math.sin(2 * math.pi * (284 + n) / 365.0)

sin_a = math.sin(math.radians(N)) * math.sin(math.radians(b)) + math.cos(math.radians(N)) * math.cos(math.radians(b)) * math.cos(math.radians(t))

a = math.asin(sin_a)
a = a * 180.0 / math.pi
a = "%.3f°" % a 

print a


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

c = "%.3f°" % c 

print c
