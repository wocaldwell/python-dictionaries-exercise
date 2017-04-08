stockDict = { 'GM': 'General Motors',
  'CAT':'Caterpillar',
  'EK':"Eastman Kodak",
  'GE': 'General Electric' }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
  ( 'CAT', 100, '1-apr-1999', 24 ),
  ( 'GE', 200, '1-jul-1998', 56 ) ]

purchase_summary = {}

for purchase in purchases:
    ticker_symbol = purchase[0]
    number_of_shares = purchase[1]
    share_price = purchase[3]
    full_price = number_of_shares * share_price
    company_name = stockDict[ticker_symbol]
    print('I purchased {0} stock for ${1}.'.format(company_name, full_price))
    if ticker_symbol in purchase_summary:
        purchase_summary[ticker_symbol] += number_of_shares
    else:
        purchase_summary[ticker_symbol] = number_of_shares
for company in purchase_summary:
    print('I have a total of {0} shares in {1}.'.format(purchase_summary[company], company))


