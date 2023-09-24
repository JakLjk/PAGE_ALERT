class FormRestrictions:
    #-------------------------------------------
    element_type = [
        "XPATH",
        ]
    #-------------------------------------------
    accepted_intervals = {
        "Minutes":60,
        "Hours":3600,
        "Days":86400}
    #-------------------------------------------


class DBSStatusFieldsStdNames:
    #-------------------------------------------
    alert_status_initializing = "initializing"
    alert_status_active = "active"
    alert_status_delayed = "delayed"
    alert_status_stopped = "stopped"
    alert_status_difference = "difference"
    #-------------------------------------------
    user_webpage_not_yet_scraped = "notScraped"
    #-------------------------------------------