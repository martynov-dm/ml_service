# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, func, UniqueConstraint, CheckConstraint
# from sqlalchemy.orm import relationship
# from src.app.db import Base, engine


# class TaskModel(Base):
#     __tablename__ = 'tasks_d-martynov-1_practicum'
#     __table_args__ = {"schema": "public", 'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
#     model_name = Column(String(255), nullable=False)
#     input_data = Column(String(1024), nullable=False)
#     status = Column(String(50), nullable=False)
#     result = Column(String(1024), nullable=True)
#     created_at = Column(DateTime, nullable=False, default=func.now())
#     updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
#     user = relationship('UserModel', back_populates='tasks')



# Base.metadata.create_all(bind=engine)