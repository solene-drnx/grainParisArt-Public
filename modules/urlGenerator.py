import time 
from datetime import datetime, timedelta
import datetime

def decalageDate(baseURL, decalage):
    future_date = datetime.datetime.today() + datetime.timedelta(days=decalage)
    
    formatted_date = future_date.strftime("%Y-%m-%d")
    
    url = baseURL + formatted_date
    
    print(url)
    return (url)

