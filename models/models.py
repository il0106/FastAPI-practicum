from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Float

metadata = MetaData()

correlations = Table(
    'correlations',
    metadata,
    Column("SECID", String, primary_key=True),
    Column("FXSECID", String, primary_key=True),
    Column("TRADEDATE", String),
    Column("COEFF_CORRELATION",Float),
    Column("COEFF_BETA",Float)
)





