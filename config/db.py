from sqlalchemy import create_engine, MetaData

engine =create_engine('mysql://ba9afcb304b59e:27ca6703@us-cdbr-east-06.cleardb.net/heroku_339b76dfa1a5759?reconnect=true')

meta = MetaData()

conn = engine.connect()
