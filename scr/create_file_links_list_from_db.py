import sqlite3

def _create_STG_common_click_links_table(company, date_start, date_end):
    con = sqlite3.connect('scr/doc/online_adv.db')
    cursor = con.cursor()

    cursor.execute('DROP TABLE IF EXISTS STG_COMMON_CLICK_LINKS')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STG_COMMON_CLICK_LINKS as
        select * from (
        select
            ID
            , дата
            , клиент
            , сайт as link
            , 'сайт' as source
            from adv_publications
            where
            клиент = ? 
            and
            сайт is not null
        union
        select
            ID
            , дата
            , клиент
            , VK1 as link
            , 'VK 1' as source
            from adv_publications
            where
            клиент = ?
            and
            VK1 is not null
        union
        select
            ID
            , дата
            , клиент
            , VK2 as link
            , 'VK 2' as source
            from adv_publications
            where
            клиент = ? 
            and
            VK2 is not null
        union
        select
            ID
            , дата
            , клиент
            , TG as link
            , 'TG' as source
            from adv_publications
            where
            клиент = ? 
            and
            TG is not null)
        where дата >= datetime(?)
        and   дата <= ? 
    ''', [company, company, company, company, date_start, date_end])

    con.commit()
    con.close()

def _create_STG_tw_click_links_table(company, date_start, date_end):
    con = sqlite3.connect('scr/doc/online_adv.db')
    cursor = con.cursor()

    cursor.execute('DROP TABLE IF EXISTS STG_TW_CLICK_LINKS')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STG_TW_CLICK_LINKS as
        select * from (
        select
            ID
            , дата
            , клиент
            , TW as link
            , 'TW' as source
            from adv_publications
            where
            клиент = ? 
            and
            TW is not null)
        where дата >= datetime(?)
        and   дата <= ? 
    ''', [company, date_start, date_end])

    con.commit()
    con.close()

def _create_STG_report_links_table(company, date_start, date_end):
    con = sqlite3.connect('scr/doc/online_adv.db')
    cursor = con.cursor()

    cursor.execute('DROP TABLE IF EXISTS STG_REPORT_LINKS')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STG_REPORT_LINKS as
        select * from (
        select
            ID
            , дата
            , клиент
            , сайт as link
            , 'сайт' as source
            from adv_publications
            where
            клиент = ? 
            and
            сайт is not null
        union
        select
            ID
            , дата
            , клиент
            , VK1 as link
            , 'VK 1' as source
            from adv_publications
            where
            клиент = ?
            and
            VK1 is not null
        union
        select
            ID
            , дата
            , клиент
            , VK2 as link
            , 'VK 2' as source
            from adv_publications
            where
            клиент = ? 
            and
            VK2 is not null
        union
        select
            ID
            , дата
            , клиент
            , TG as link
            , 'TG' as source
            from adv_publications
            where
            клиент = ? 
            and
            TG is not null
        union
            select
            ID
            , дата
            , клиент
            , TW as link
            , 'TW' as source
            from adv_publications
            where
            клиент = ? 
            and
            TW is not null)
        where дата >= datetime(?)
        and   дата <= ? 
    ''', [company, company, company, company, company, date_start, date_end])

    con.commit()
    con.close()


    # cursor.execute('''
    #     select * from STG_REPORT_LINKS
    #     where дата >= datetime(?)
    #     and   дата <= ?
    #     ''', [date_start, date_end])

    # for row in cursor.fetchall():
    #     # print(row)
    #     report_links.append(row)
def create_STG_tables(company, date_start, date_end):
    _create_STG_common_click_links_table(company, date_start, date_end)
    _create_STG_tw_click_links_table(company, date_start, date_end)
    _create_STG_report_links_table(company, date_start, date_end)
'''
Переименовать колонки
Вынести sql-скрипт в отдельные файлы?
'''
    
