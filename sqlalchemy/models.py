# models.py
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.sqltypes import DateTime

# Tworzymy bazę danych SQLite (plik local.db)
engine = create_engine("sqlite:///baza_alchemy.db", echo=True)

Base = declarative_base()


# Definiujemy tabelę User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surnname = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (f"<User(id={self.id}, name='{self.name}',surname={self.surnname}, email='{self.email}',"
                f"created_at='{self.created_at}')>")

class Spendings(Base):
    __tablename__ = 'spendings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'))  # Foreign key to User
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (f"<Spendings(id={self.id}, user_id={self.user_id}, amount={self.amount}, created_at='{self.created_at}')>")
# Tworzymy tabele w bazie
Base.metadata.create_all(engine)

# Tworzymy sesję do interakcji z bazą danych

def get_session():
    """Funkcja zwracająca sesję do bazy danych."""
    session = sessionmaker(bind=engine)
    return session()

def create_user(name, surname, email,date:datetime=datetime.now()):
    """Funkcja tworząca nowego użytkownika."""
    session = get_session()
    new_user = User(name=name, surnname=surname, email=email, created_at=date)
    session.add(new_user)
    session.commit()
    session.close()
    return new_user

def list_users():
    """Funkcja zwracająca listę wszystkich użytkowników."""
    session = get_session()
    users = session.query(User).all()
    session.close()
    return users

create_user("bartek","sielski","sielskibartosz95@gmial.com")
create_user("ola","prokopska","olaprokopska@gmial.com", datetime(2025,12,24,21,47))

def create_spending(user_id, amount, date:datetime=datetime.now()):
    """Funkcja tworząca nowe wydatki."""
    session = get_session()
    new_spending = Spendings(user_id=user_id, amount=amount, created_at=date)
    session.add(new_spending)
    session.commit()
    session.close()
    return new_spending

def list_spendings():
    """Funkcja zwracająca listę wszystkich wydatków."""
    session = get_session()
    spendings = session.query(Spendings).all()
    session.close()
    return spendings

def get_all_spendings_with_users():
    session = get_session()
    result = (
        session.query(Spendings)
        .join(User, Spendings.user_id == User.id)
        .all()
    )
    session.close()
    return result
create_spending(1,100)
create_spending(2,200)
print(get_all_spendings_with_users())