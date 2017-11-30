# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "package"
app_title = "Package"
app_publisher = "taher"
app_description = "Package app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "taherkhalil52@gmail.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/package/css/package.css"
# app_include_js = "/assets/package/js/package.js"

# include js, css files in header of web template
# web_include_css = "/assets/package/css/package.css"
# web_include_js = "/assets/package/js/package.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "package.install.before_install"
# after_install = "package.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "package.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Sales Invoice" : {
		"validate": "package.package.doctype.packages.packages.package_buy"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"package.tasks.all"
# 	],
# 	"daily": [
# 		"package.tasks.daily"
# 	],
# 	"hourly": [
# 		"package.tasks.hourly"
# 	],
# 	"weekly": [
# 		"package.tasks.weekly"
# 	]
# 	"monthly": [
# 		"package.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "package.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "package.event.get_events"
# }

