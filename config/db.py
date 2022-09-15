from sqlalchemy import create_engine, MetaData

engine =create_engine('mysql+pymysql://root:@localhost/pi_1')

meta = MetaData()

conn = engine.connect()
