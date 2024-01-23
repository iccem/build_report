import sqlite3
import pandas as pd


def _creat_db(conn):
    
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS adv_publications')

    c.execute('''
        CREATE TABLE IF NOT EXISTS adv_publications(
            ORDER_ID varchar(128),
            month integer,
            day integer,
            date datetime,
            client varchar(128),
            manager varchar(128),
            payer varchar(128),
            payment decimal,
            reason varchar(128),
            txt_size integer,
            title varchar(384),
            web_address varchar(128),
            vk_1_address varchar(128),
            vk_2_address varchar(128),
            tg_address varchar(128),
            tw_address varchar(128),
            note varchar(128),
            report
        )
    ''')


def load(file_path: str) -> None:
    """
    Loads data to db from xlsx.

    """
    db_path = 'scr/doc/online_adv.db'
    connected = False
    try:
        conn = sqlite3.connect(db_path)

        connected = True
    except sqlite3.Error as err:
        print(err)
    if connected:
        _creat_db(conn)

    df = pd.read_excel(file_path, engine='openpyxl')
    df.to_sql('adv_publications', conn, if_exists='replace', index=False, index_label=None)
    conn.commit()
 
