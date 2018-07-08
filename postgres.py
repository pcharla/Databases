# database will not be a .db file stored in ur filesystem
# will be  a database embeddded in postgres installation
# requirement -- u need to have an existing database in ur postgresql database server
#it comes with a default database called postgres once installed, we pas database here into file
#or create ur own database thru pgadmin

import psycopg2
conn= psycopg2.connect( ') 
cur= conn.cursor() # cursor object, REFER to connection object and cursor method
cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price Real)')# you want to point to ur cursor object
conn.commit()# committ changes to db
conn.close() # close the connection


#def add_data(item, quantity, price):
  #conn= psycopg2.connect('lite.db')
  #cur= conn.cursor()
  #cur.execute('INSERT INTO store VALUES(?,?,?)',(item,quantity,price))
  #conn.commit()
  #conn.close()


#def view():
  #conn= psycopg2.connect('lite.db')
  #cur= conn.cursor()
  #cur.execute('SELECT * FROM store')
  #rows= cur.fetchall()
  #return rows

#def delete(item):
  #conn= psycopg2.connect('lite.db')
  #cur= conn.cursor()
  #cur.execute('DELETE FROM store WHERE item=?', (item,))
  #conn.commit()
  #conn.close()

#def update(quantity, price, item):
  #conn= psycopg2.connect('lite.db')
  #cur= conn.cursor()
  #cur.execute('UPDATE store SET quantity=?, price=? WHERE item= ?', (quantity, price, item)) 
  #conn.commit()
  #conn.close()
  


#delete('vinegar')

#create()
#add_data('water',2,3)
#add_data('vinegar',3,4)
#add_data('coke',4,5)
#add_data('beer',6,3)
#add_data('wine',8,9)
#update(11,22,'coke')

#print(view()) # rows variable is returned as a python list with data in it




  

  
