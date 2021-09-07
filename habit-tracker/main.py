import requests

from datetime import date, datetime

pixela_endpoint = "https://pixe.la/v1/users"

# USERNAME = '' <------------ insert a name and erase this note
# CSRF_TOKEN = '' <------------ make a password/key and erase this note

today_no_format = date.today()

# --------------------------TODAY'S DATE (CODE)---------------------------
TODAYS_DATE = today_no_format.strftime("%Y%m%d")
# -----------------------------------------------------------------------

# ---------------- MANUALLY ENTER A DATE  HERE --------------------------
DATE_OF_CHOICE = datetime(year=2021, month=8, day=28)

# -------------------- DON'T CHANGE THIS FORMAT -------------------------
DATE_OF_CHOICE_FORMATTED = DATE_OF_CHOICE.strftime("%Y%m%d")
# -----------------------------------------------------------------------
# print statement will reassure that it is in the correct format
# print(TODAYS_DATE)
# -----------------------------------------------------------------------

# -------------------------- THIS CREATES YOUR ACCOUNT ------------------

user_params = {
    "token": CSRF_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": CSRF_TOKEN
}
# -----------------------------------------------------------------------

# Comment out after successfully making an account --> you don't want your program
# to "attempt" to make an account every time you run this program.

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# HOW TO CREATE A PERSONAL GRAPH, PROVIDE ALL FIELDS AND API KEY AS A "HEADERS"

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "training1",
#     "name": "Martial Arts Graph",
#     "unit": "Minutes",
#     "type": "float",
#     "color": "kuro"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# graph_id = "" <----------- enter a the graph id and erase this note

# create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

# ----------------- CHANGE DATE PARAM TO CORRECT VARIABLE OF CHOICE----------

# ------------------- THIS CREATE A PIXEL FOR ROSTER-------------------------

pixel_config = {
    # THIS WILL AFFECT YOUR ROSTER VISUALS.
    "date": DATE_OF_CHOICE_FORMATTED,
    "quantity": "60.0"
}

# response = requests.post(url=create_pixel_endpoint, json=pixel_config, headers=headers)
#
# print(response.text)

# ------------------------------- UPDATES A PIXEL ---------------------------

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{TODAYS_DATE}"
edit_pixel_info = "70.5"

updates = {
    "quantity": edit_pixel_info
}
response = requests.put(url=update_endpoint, json=updates, headers=headers)
print(response.text)
