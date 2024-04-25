# from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

# metadata = MetaData()

# operation = Table(
#     "operation",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("quantity", String),
#     Column("figi", String),
#     Column("instrument_type", String, nullable=True),
#     Column("date", TIMESTAMP),
#     Column("type", String),
# )

# class TransactionModel(Base):
#     __tablename__ = 'transactions_d-martynov-1_practicum'
#     __table_args__ = {"schema": "public", 'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
#     amount = Column(Float, nullable=False)
#     timestamp = Column(DateTime, nullable=False, default=func.now())
#     __table_args__ = (UniqueConstraint('user_id', 'amount', 'timestamp', name='unique_transaction'),)
#     user = relationship('UserModel', back_populates='transactions')


# class UserBalanceModel(Base):
#     __tablename__ = 'user_balances_d-martynov-1_practicum'
#     __table_args__ = {"schema": "public", 'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey(UserModel.id), unique=True, nullable=False)
#     balance = Column(Float, CheckConstraint('balance >= 0'), nullable=False, default=10.0)
#     user = relationship('UserModel', back_populates='balance')