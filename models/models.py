from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Float

metadata = MetaData()

correlations = Table(
    'correlations',
    metadata,
    Column("SECID", String, primary_key=True),
    Column("FXSECID", String, primary_key=True),
    Column("TRADEDATE", TIMESTAMP),
    Column("COEFF_CORRELATION", Float),
    Column("COEFF_BETA", Float)
)

quotes = Table(
    'quotes',
    metadata,
    Column("begin", TIMESTAMP),
    Column("open", Float),
    Column("close", Float),
    Column("high", Float),
    Column("low", Float),
    Column("value", Float),
    Column("volume", Integer)
)



