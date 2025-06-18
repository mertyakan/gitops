from locust import HttpUser, task, between

class PetclinicUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home_page(self):
        self.client.get("/")

    @task
    def find_owners_page(self):
        self.client.get("/owners/find")

    @task
    def veterinarians_page(self):
        self.client.get("/vets.html")

    @task
    def error_page(self):
        self.client.get("/oups")

    @task
    def static_resources(self):
        self.client.get("/resources/images/pets.png")

