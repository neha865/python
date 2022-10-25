#phonenumbers module
import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

n=int(input("how many Phone Numbers : "))
for i in range(n):
    print("\n")
    number = input("Enter Phone Number: ")
    number = ph.parse(number)
    country = geocoder.description_for_number(number, "en")
    sim_card_provider = carrier.name_for_number(number, "en")
    time_zone = timezone.time_zones_for_number(number)
    print("Country : ", country)
    print("Sim Card Provider : ", sim_card_provider)
    print("Time Zone : ", time_zone)

