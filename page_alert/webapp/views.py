from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from . import db
from .models import UserProcess
from .tools.url_parser import prettify_url
from page_alert.metadata.common_metadata import DBSStatusFieldsStdNames, FormRestrictions


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('pages', methods=['GET', 'POST'])
@login_required
def pages_list():
    if request.method == 'POST':
        # Load the form
        alert_name = request.form.get("alert-name")
        alert_link = request.form.get("page-link")
        alert_search_elem = request.form.get("search-element")
        alert_search_elem_type = request.form.get("element-type")
        alert_interval_value = request.form.get("interval-value")
        alert_interval_period_type = request.form.get("interval-type")
        
        # Convert interval to seconds
        # interval = alert_interval_value * FormRestrictions.accepted_intervals[alert_interval_period_type]

        # Adding alert information to db
        new_user_process = UserProcess(
            user_id = current_user.id,
            alert_name = alert_name,
            alert_status = DBSStatusFieldsStdNames.alert_status_initializing,
            element_comparison_identifier = alert_search_elem,
            element_comparison_type = alert_search_elem_type,
            refresh_interval_period_type = alert_interval_period_type,
            refresh_interval_value = alert_interval_value,
            webpage_link=alert_link)
        
        db.session.add(new_user_process)
        db.session.commit()
        flash(f"Alert {alert_name} added.")

    return render_template('pages_list.html', 
                           user=current_user,
                           dbStatusFields=DBSStatusFieldsStdNames,
                           formRestrictions=FormRestrictions)


@views.route('/alert_details/<alert_id>', methods=["GET", "POST"])
def alert_details(alert_id):
    alert = UserProcess.query.get(alert_id)
    if alert:
        if alert.user_id == current_user.id:
            if request.method == 'POST':
                alert.alert_name = request.form.get("alertName")
                alert.webpage_link = request.form.get("pageLink")
                alert.element_comparison_identifier = request.form.get("searchElement")
                alert.element_comparison_type = request.form.get("elementType")
                alert.refresh_interval_value = request.form.get("intervalValue")
                alert.refresh_interval_period_type = request.form.get("intervalType")

                db.session.commit()
            
            return render_template('alert_page.html',
                                    user=current_user, 
                                    alert=alert,
                                    formRestrictions=FormRestrictions)
        else:
            # TODO render information that access to this resource is restricted
            flash("Access to this resource is restricted", category='error')
            return redirect(url_for("views.pages_list"))
    else:
        # TODO render information that access to this resource is restricted
        flash("Access to this resource is restricted", category='error')
        return redirect(url_for("views.pages_list"))

    # print(alert_id)
    # return render_template('alert_page.html', user=current_user)