


def get_page_raw(link, method="selenium"):
    if method == "selenium":
        return __get_page_selenium()
    elif method == "requests":
        return __get_page_requests()
    else:
        raise KeyError(f"Wrong method selected: {method}")
    

def __get_page_selenium():
    return None


def __get_page_requests():
    return None