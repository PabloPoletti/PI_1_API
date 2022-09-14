from sqlalchemy import create_engine, MetaData

engine =create_engine('mysql+pymysql://root:@127.0.0.1:3306/pi_1')

meta = MetaData()

conn = engine.connect()