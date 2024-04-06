from sqlalchemy import create_engine
from sqlalchemy import session
import data_classes

engine = create_engine('sqlite://smw_central.db', echo=True)
data_classes.Base.metadata.create_all(engine)

