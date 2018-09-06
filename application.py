from flask import Flask,request,render_template
import random

application = Flask(__name__)

internalTime = "1.00"
internalTargetNumber = "31"
internalStockSymbols = "C"
internalAntDelay = 999


@application.route('/test/<htmlPage>')
def openPage(htmlPage):
   return render_template('%s.html' % htmlPage)

@application.route('/')
def hello_world():
   print("Standard out: Hello World!!!")
   return 'Hello World'

@application.route('/saveLog', methods=['GET','POST'])
def save_log():
	d = request.form
	print(dir(d))
	print(type(d))
	print(d.items()[0][1])
	return "Saved!"

@application.route('/timeInterval')
def time_interval():
	return internalTime

@application.route('/getAntMoveDelay')
def ant_move_delay():
	global internalAntDelay
	if internalAntDelay == 999:	
		ant_delay = random.randrange(100)
	else: 
		ant_delay = internalAntDelay
	return str(ant_delay)

@application.route('/setAntMoveDelay/<delay>')
def set_ant_move_delay(delay):
	global internalAntDelay
	internalAntDelay=int(delay)
	return "OK. Set ant speed to: %s." % internalAntDelay


@application.route('/targetNumber')
def target_number():
	return internalTargetNumber

@application.route('/changeTime/<timeThreeDigitsTwoDecimals>')
def change_time(timeThreeDigitsTwoDecimals):
	global internalTime
	internalTime = "%s.%s" % (timeThreeDigitsTwoDecimals[0],timeThreeDigitsTwoDecimals[1:3])
	return "set to %s" % internalTime 

@application.route('/changeTargetNumber/<num>')
def change_target_number(num):
	global internalTargetNumber
	internalTargetNumber = num
	return "set to %s" % num

@application.route('/stockSymbols')
def get_stock_symbols():
	#global internalStockSymbols
	return internalStockSymbols

@application.route('/setStockSymbols/<newStocks>')
def set_stock_symbols(newStocks):
	global internalStockSymbols
	internalStockSymbols=newStocks
	return "OK.  Set to: %s" % internalStockSymbols

@application.route('/recordAntTravels')
def save_ant_movements():
	print "Saved!!!"

if __name__ == '__main__':
   application.run()
