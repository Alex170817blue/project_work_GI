import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import (Column, ForeignKeyConstraint, Integer, MetaData,
                        PrimaryKeyConstraint, String, Table, UniqueConstraint,
                        create_engine)
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.engine import URL

load_dotenv()


def mysql_connection():
    url = URL.create(
        "mysql+pymysql",
        username=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        host=os.environ.get("MYSQL_HOST", "localhost"),
        port=int(os.environ.get("MYSQL_PORT", 3306)),
        database=os.environ["MYSQL_DATABASE"],
        query={"charset": "utf8mb4"},
    )
    return create_engine(url)


def column_type(series, col):
    if pd.api.types.is_integer_dtype(series):
        return Integer
    if pd.api.types.is_float_dtype(series):
        return DOUBLE
    return String(120) if col.endswith("_name") or col == "geo_group" else String(50)


def build_metadata(tables):
    metadata = MetaData()
    for t in tables:
        columns = [Column(c, column_type(t.df[c], c), nullable=(c not in t.pk))
                   for c in t.df.columns]

        constraints = [PrimaryKeyConstraint(*t.pk)]
        # una FK per ogni coppia: ForeignKeyConstraint([colonna_fatto], ["tabella.colonna"])
        constraints += [ForeignKeyConstraint([c], [ref]) for c, ref in t.fks.items()]
        # i fatti hanno id come PK: l'unicità sulla chiave naturale evita i duplicati
        if t.pk == ["id"]:
            constraints.append(UniqueConstraint(*t.fks.keys()))

        Table(t.name, metadata, *columns, *constraints, mysql_engine="InnoDB")
    return metadata


def load_mysql(engine, tables, recreate=True):
    metadata = build_metadata(tables)
    by_name = {t.name: t for t in tables}

    if recreate:
        metadata.drop_all(engine)
    metadata.create_all(engine)

    with engine.begin() as conn:
        for table in metadata.sorted_tables:
            df = by_name[table.name].df
            df.to_sql(table.name, conn, if_exists="append", index=False,
                      chunksize=5000, method="multi")
            print(f"{table.name}: {len(df)} righe")