import threading


def run_scrape_compare_scripts(thread_limit=4):
    db_connect = DBConnect()

    thread_pool = []
    while True:
        if len(thread_pool) < thread_limit:
            thread = threading(target=None)
            thread_pool.append(thread)
            thread.start()
        for thread in thread_pool:
            if not thread.is_alive():
                thread_pool.remove(thread)

