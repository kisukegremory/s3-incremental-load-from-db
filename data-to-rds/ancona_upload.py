import polars as pl
from sqlalchemy import create_engine

schema = {'id': pl.Categorical, 'code': pl.String, 'Date': pl.Datetime, 'NO2': pl.Float64, 'O3': pl.Float64, 'PM10': pl.Float64, 'Latitude': pl.Float64, 'Longitude': pl.Float64, 'station_name': pl.Categorical, 'Vegitation (High)': pl.Float64, 'Vegitation (Low)': pl.Float64}

ancona = pl.read_csv("data/ancona_data.csv", schema_overrides=schema, columns=['id','code','Date', 'PM10', 'Latitude', 'station_name', 'Vegitation (High)', 'Vegitation (Low)'])

engine = create_engine('postgresql://postgres:postgresspass@localhost:5432/postgres')

ancona.to_pandas(use_pyarrow_extension_array=True).to_sql('Ancona', engine, if_exists='replace', index=False)

