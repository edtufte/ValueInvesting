def eligibilitycheck(ticker,dfformatted):
    
    elegiblestock = True
    reasonlist=[]

    # print (dfformatted)
    # EPS increases over the year (consistent)
    if dfformatted.epsgrowth.min() < 0:
        elegiblestock = False
        reasonlist.append('there was negative EPS growth '+str(round(100*dfformatted.epsgrowth.min(),4)) + '%')
    
    # ROE > 0.15
    if dfformatted.roe.mean()<0.13:
            elegiblestock = False
            reasonlist.append('Return on Equity (ROE) mean is less than 13% at '+ str(round(100*dfformatted.roe.mean(),2)) + '%')
    # ROA > 0.07 (also consider debt to equity cause Assets = liabilities + equity)
    if dfformatted.roa.mean()<0.07:
            elegiblestock = False
            reasonlist.append('Return on Assets (ROA) mean is less than 0.07 ' + str(dfformatted.roa.mean()))
    # Long term debt < 5 * income
    if dfformatted.longtermdebt.tail(1).values[0]>5*dfformatted.netincome.tail(1).values[0]:
            elegiblestock = False
            reasonlist.append('PY long term debt is more than 5 times the net income at '
                + str(dfformatted.netincome.tail(1).values[0]))
    # Interest Coverage Ratio > 3
    if dfformatted.interestcoverageratio.tail(1).values[0]<3:
            elegiblestock = False
            reasonlist.append('PY Interest coverage ratio is less than 3 at '
                + str(round(dfformatted.interestcoverageratio.tail(1).values[0],2)))
#     print ticker,elegiblestock,reasonlist

    return reasonlist