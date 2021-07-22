# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

# write your loop here
for headline in headlines:
    #print(f'Current length of ticker is: {len(news_ticker)}')
    if len(news_ticker) + len(headline) < (140-1):
        news_ticker += f'{headline} '
        #print(f'Current length of ticker is: {len(news_ticker)}')
    else:
        for char in headline:
            if len(news_ticker) < (140):
                news_ticker += char
            else: 
                break

#for headline in headlines:
#    news_ticker += headline + " "
#    if len(news_ticker) >= 140:
#        news_ticker = news_ticker[:140]
#        break

print(news_ticker)