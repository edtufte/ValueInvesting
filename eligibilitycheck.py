def eligibilitycheck(ticker,dfformatted):
    
    legiblestock = True
    reasonlist=[]

    # print (dfformatted)
    # EPS increases over the year (consistent)
    for growth in dfformatted.epsgrowth:
        if growth<0:
            legiblestock = False
            reasonlist.append('there was negative growth '+str(round(100*growth,4)) + '%')
            break
    # ROE > 0.15
    if dfformatted.roe.mean()<0.13:
            legiblestock = False
            reasonlist.append('roe mean is less than 13% at '+ str(round(100*dfformatted.roe.mean(),4)) + '%')
    # ROA > 0.07 (also consider debt to equity cause Assets = liabilities + equity)
    if dfformatted.roa.mean()<0.07:
            legiblestock = False
            reasonlist.append('roa mean is less than 0.07 ' + str(dfformatted.roa.mean()))
    # Long term debt < 5 * income
    if dfformatted.longtermdebt.tail(1).values[0]>5*dfformatted.netincome.tail(1).values[0]:
            legiblestock = False
            reasonlist.append('long term debt is 5 times the net income')
    # Interest Coverage Ratio > 3
    if dfformatted.interestcoverageratio.tail(1).values[0]<3:
            legiblestock = False
            reasonlist.append('Interest coverage ratio is less than 3 at ' + str(round(dfformatted.interestcoverageratio.tail(1).values[0],2)))
#     print ticker,legiblestock,reasonlist
    return reasonlist