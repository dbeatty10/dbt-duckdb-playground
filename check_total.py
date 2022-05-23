import duckdb

PLAYGROUND = "playground.duckdb"

if __name__ == "__main__":
    conn = duckdb.connect(PLAYGROUND)
    conn.execute("select * from fct_paid_income")
    print(conn.fetchall())
