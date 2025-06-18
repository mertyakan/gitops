from locust import HttpUser, task, between
import random
import string
from datetime import date
import re

class PetclinicUser(HttpUser):
    host = "https://petclinic.mertyakan.com"
    wait_time = between(1, 3)

    @task
    def full_owner_and_pet_flow(self):
        # 👤 Rastgele kullanıcı bilgileri
        first_name = ''.join(random.choices(string.ascii_letters, k=6))
        last_name = ''.join(random.choices(string.ascii_letters, k=6))
        address = f"{random.randint(1, 9999)} Locust Ave"
        city = random.choice(["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"])
        telephone = ''.join(random.choices("0123456789", k=10))

        # 📝 Kullanıcıyı ekle
        with self.client.post("/owners/new", data={
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "city": city,
            "telephone": telephone
        }, allow_redirects=False, catch_response=True) as response:

            if response.status_code == 302 and "Location" in response.headers:
                redirect_url = response.headers["Location"]
                match = re.search(r"/owners/(\d+)", redirect_url)
                if match:
                    owner_id = match.group(1)
                    print(f"✅ Owner created: {first_name} {last_name} (ID: {owner_id})")

                    # 🐶 Evcil hayvan bilgileri
                    pet_name = random.choice(["Loki", "Max", "Maya", "Bobby", "Pamuk"])
                    birth_date = date.today().strftime("%Y-%m-%d")
                    pet_type_id = str(random.choice([1, 2, 3]))  # Cat, Dog, Hamster gibi

                    self.client.get(f"/owners/{owner_id}/pets/new")
                    self.client.post(f"/owners/{owner_id}/pets/new", data={
                        "name": pet_name,
                        "birthDate": birth_date,
                        "type": pet_type_id
                    })
                    print(f"🐾 Pet added: {pet_name} for Owner ID {owner_id}")
                else:
                    print("❗ ID bulunamadı: redirect =", redirect_url)
            else:
                print(f"❌ Owner ekleme başarısız: {response.status_code}")

