# MakerApp

App used to serve up functionality to Raspberry Pi Units:
/saveLog (POST endpoint for log data)
/timeInterval (GET)
/getAntMoveDelay (GET)
/setAntMoveDelay/<delay> (SET)
/targetNumber (GET)
/changeTime/<timeThreeDigitsTwoDecimals> (SET)
/changeTargetNumber/<num> (SET)
/stockSymbols (GET)
/setStockSymbols/<newStocks> (SET)

serves up static web pages for use with Automation Testing:
/test/--test_file_name-- (GET) example- this URL serves up test_1.html from the server:: .../test/test_1 
