from app.database.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Text, VARCHAR

class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    author: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, default='')
    rating: Mapped[int] = mapped_column(Integer, nullable=False)



