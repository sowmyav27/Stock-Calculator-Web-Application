#!/usr/bin/env python
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route('/index')
def init():
   return render_template('index.html')

@app.route('/results',methods=["POST"])

def stockProfitCalculator():
	tickerSymbol = request.form['ticker_Symbol']
	allotment = request.form['allotment']
	final_Share_Price = request.form['final_SharePrice']
	sell_Commission = request.form['sell_Commission']
	initial_Share_Prices = request.form['initial_SharePrice']
	buy_Commission = request.form['buy_Commission']
	capital_Gain_Tax_Rate = request.form['capital_Gain_TaxRate']
	
	#Calculations
	proceeds=float(allotment)*float(final_Share_Price)
	#share price
	total_Share_Prize=float(allotment)*float(initial_Share_Prices)
	#total commissions = sell Commission + Buy commission
	total_Commission=float(sell_Commission)+float(buy_Commission)
	#fixed cost of the symbol is share price+commission
	fixed_Cost = float(total_Share_Prize) + float(total_Commission)
	
	gain=float(proceeds)-fixed_Cost

	tax_On_Capital_Gain=float(capital_Gain_Tax_Rate)/100 * float(gain)
	#Cost = (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
	total_Cost_Symbol=float(tax_On_Capital_Gain)+total_Commission+total_Share_Prize
	
	net_Profit=proceeds-total_Cost_Symbol
	
	returns=(net_Profit/total_Cost_Symbol)*100
	#break even price is cost per unit
	break_Even_Price= float(fixed_Cost)/float(allotment)

	return render_template("results.html", proceeds="%.2f"%proceeds,totalCost="%.2f"%total_Cost_Symbol,finalSharePrice=final_Share_Price,sellCommission=sell_Commission,totalSharePrize=total_Share_Prize,initialSharePrice=initial_Share_Prices, buyCommission=buy_Commission,totalCommission=total_Commission,taxOnCapitalGain="%.2f"%tax_On_Capital_Gain, roi="%.2f"%returns, breakEven="%.2f"%break_Even_Price,netProfit="%.2f"%net_Profit)
	

if __name__ == '__main__':
   app.run()
