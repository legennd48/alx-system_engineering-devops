#!/usr/bin/python3
import getDash
from getDash import get_dash

dashboard_ids = get_dash()
for dashboard_id, dashboard_title in dashboard_ids.items():
    print(f"Dashboard ID: {dashboard_id}, Title: {dashboard_title}")
