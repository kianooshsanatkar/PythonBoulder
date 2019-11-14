from sqlalchemy.ext.declarative import declarative_base


class db:
    Base = declarative_base()
    connection_str = "postgresql://IUEPA_Test:pass1234@localhost/IUEPA_DB"
    echo = True
