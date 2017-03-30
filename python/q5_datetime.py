# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

>>> date1= datetime.strptime(date_start, '%m-%d-%Y')
>>> date2= datetime.strptime(date_stop, '%m-%d-%Y')
>>> days1 = (date2-date1).days
>>> print(days1)
937

####b)  
date_start = '12312013'  
date_stop = '05282015'  

>>> date1 = datetime.strptime(date_start, '%m%d%Y')
>>> date2 = datetime.strptime(date_stop, '%m%d%Y')
>>> days2 = (date2-date1).days
>>> print(days2)
513

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

>>> date1 = datetime.strptime(date_start, '%d-%b-%Y')
>>> date2 = datetime.strptime(date_stop, '%d-%b-%Y')
>>> days3 = (date2-date1).days
>>> print(days3)
7850
