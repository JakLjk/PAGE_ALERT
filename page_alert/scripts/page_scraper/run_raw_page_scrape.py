from time import sleep
import threading

from scraper_init import init_page_scrape




def run_raw_page_scrape(max__concurrent_threads = 4):
    thread_pool = []
    while True:
        if len(thread_pool) < max__concurrent_threads:
            thread = threading.Thread(target=init_page_scrape)
            thread_pool.append(thread)
            thread.start()

        for thread in thread_pool:
            if not thread.is_alive():
                thread_pool.remove(thread)



run_raw_page_scrape()
