from selenium import webdriver
import time
import sqlite3
import os
import time
import errno
# from doc import paths


def _get_selenium(rows, path_for_screens, time_sleep):
    print('Количество записей: ', len(rows))
    print(*rows, sep="\n")
    for x, y in rows.items():
        path_for_screen = y
        file_name = path_for_screens + x

        driver = webdriver.Chrome()
        driver.set_window_size(490, 850)

        # Move the window to position x/y
        driver.set_window_position(200, 5)
        time.sleep(3)
        try:
            driver.get(path_for_screen)
            time.sleep(time_sleep)

            driver.save_screenshot(file_name)
            time.sleep(5)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
            time.sleep(5)
            print("OK")


def _get_common_links(common_click_links):
    '''Получает список общих ссылок из таблицы 
    и генерирует названия файлов.
    Возвращает список пар: имя файла и ссылка'''
    con = sqlite3.connect('scr/doc/online_adv.db')
    cursor = con.cursor()
    cursor.execute('''
        select * from STG_COMMON_CLICK_LINKS
        ''')

    for row in cursor.fetchall():
        common_click_links.append(row)
    return common_click_links



def _make_common_screen():
    common_click_links = []
    temp = {}
    common_click_links =_get_common_links(common_click_links)

    for row in common_click_links:
        date = str(row[1]).replace("T00:00:00", "")
        splitted_date = date.split('-')
        clear_date = str(splitted_date[2] + '-' + splitted_date[1] + '-' + splitted_date[0])
        filename = str(row[0]) + '   ' + clear_date + '   ' + row[2] + '   ' + row[4] + '.png'
        path = row[3].replace("vk.com", "m.vk.com")
        temp[filename] = path
    # print('*')
    return temp


def make_screen(path_for_screens):
    try:
        if not os.path.exists(path_for_screens):
            os.makedirs(path_for_screens)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    
    rows_common_screen = _make_common_screen()
    _get_selenium(rows_common_screen, path_for_screens, 5)
    
    