from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Float

metadata = MetaData()

correlations = Table(
    'correlations',
    metadata,
    Column("SECID", String, primary_key=True),
    Column("FXSECID", String, primary_key=True),
    Column("TRADEDATE", TIMESTAMP),
    Column("COEFF_CORRELATION", Float, nullable=False),
    Column("COEFF_BETA", Float, nullable=False)
)

quotes = Table(
    'quotes',
    metadata,
    Column("SECID", String, nullable=False),
    Column("begin", TIMESTAMP, nullable=False),
    Column("end", TIMESTAMP, nullable=False),
    Column("open", Float, nullable=False),
    Column("close", Float, nullable=False),
    Column("high", Float, nullable=False),
    Column("low", Float, nullable=False),
    Column("value", Float),
    Column("volume", Integer)
)



