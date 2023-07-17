from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///price.sqlite")

CREATE_TABLE_QUERY = """
CREATE TABLE product
(
    id integer primary key,
    name varchar unique,
    description varchar,
    price float
);
"""
INSERT_VALUE_QUERY = """
INSERT INTO product(name, description, price)
VALUES ('test', 'Описание товара', 1200)
"""
with engine.connect() as conn:
    conn.execute(text(CREATE_TABLE_QUERY))

    conn.execute(text(INSERT_VALUE_QUERY))

    conn.commit()
    result = conn.execute(text("""SELECT * FROM PRODUCT;"""))
    print(result.fetchall())


