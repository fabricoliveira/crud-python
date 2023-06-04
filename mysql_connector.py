# DROP DATABASE IF EXISTS dbyoutube;
# CREATE DATABASE IF NOT EXISTS dbyoutube;
# USE dbyoutube;

# CREATE TABLE IF NOT EXISTS sells (
#     sell_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     product_name varchar(255),
#     product_price int
# );


from mysql.connector import connect

# create connection
connection = connect(
    host='localhost',
    user='root',
    password='',
    database='dbyoutube'
)


# runs connection
cursor = connection.cursor()


# CRUD - CREATE
def create(product_name=None, product_price=None):
    query = f'INSERT INTO sells (product_name, product_price) VALUES ("{product_name}", {product_price})'
    cursor.execute(query)
    connection.commit()  # for create, update or delete operations
    print(f'cursor.lastrowid: {cursor.lastrowid}')


# CRUD - READ
def read(sell_id=None):
    query = 'SELECT * FROM sells '
    if sell_id:
        query += f' WHERE sell_id = {sell_id}'
    cursor.execute(query)
    result = cursor.fetchall()  # for read operations
    print(f'result: {result}')


# CRUD - UPDATE
def update(sell_id=None, product_price=None):
    query = f'UPDATE sells SET product_price = {product_price} WHERE sell_id = {sell_id}'
    cursor.execute(query)
    connection.commit()  # for create, update or delete operations


# CRUD - DELETE
def delete(sell_id=None):
    query = f'DELETE FROM sells WHERE sell_id = {sell_id}'
    cursor.execute(query)
    connection.commit()  # for create, update or delete operations


create('hedphone', 20)
read()
update(3, 10)
read()
delete(1)


# close connections
cursor.close()
connection.close()