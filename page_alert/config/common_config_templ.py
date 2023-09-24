class DBConfig:
    db_namepath = f"sqlite:////path/to/database.db"

class DBStandardFieldNames:
    alert_status_awaiting = "Initializing"

class FlaskConfig:
    secret_key = ""


class FormRestrictions:
    element_type = [
        "XPATH",
    ]
    accepted_intervals = [
        "Minutes",
        "Hours",
        "Days"
    ]