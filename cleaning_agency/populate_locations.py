from bookings.models import GeneralLocation

locations = [
    "Amlwch", "Beaumaris", "Benllech", "Holyhead", "Llangefni", 
    "Menai Bridge", "Newborough", "Aberffraw", "Bodedern", "Bryngwran",
    "Brynsiencyn", "Cemaes Bay", "Gaerwen", "Gwalchmai", "Llanerchymedd",
    "Llanfairpwllgwyngyll", "Llangeinwen", "Llangoed", "Moelfre", "Pentraeth",
    "Rhosneigr","Bangor"  # Ensure all locations are included
]

for location_name in locations:
    GeneralLocation.objects.create(name=location_name)