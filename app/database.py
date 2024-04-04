from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config


engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
