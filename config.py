import web

db_host = 'localhost'
db_name = 'tiendasp'
db_user = 'taniaunid'
db_pw = 'hidalgo'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )