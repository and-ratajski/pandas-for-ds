from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.db', echo=False)
db_types = {'POP': 'float64', 'AREA': 'float64', 'GDP': 'float64', 'IND_DAY': 'datetime64'}

# Write to a DB
db_df = pd.DataFrame(data=data).T.astype(dtype=db_types)
db_df.dtypes

db_df.to_sql('data.db', con=engine, index_label='ID', if_exsits='fail')

# Read from DB
db_df = pd.read_sql('data.db', con=engine, index_col='ID')
db_df.index.name = None  # axis[0] is named 'ID' after DB load
db_df.fillna(value=float('nan'), inplace=True)  # DB NULLs are casted into None by sqlalchemy
