from django.db import models
from .profile import Profile
from django.db.models import Q


class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return f"Client id: {self.client_id} with profile id: {self.profile_id} born in: [{self.birthday}]"

    @staticmethod
    def create_new_client(username, password, first_name, last_name, email, phone_number, country, city, address,
                          birthday):
        profile = Profile.create_new_profile(username, password, first_name,
                                             last_name, email, phone_number,
                                             country, city, address)
        client = Client(profile_id=profile, birthday=birthday)
        client.save()

        return client

    @staticmethod
    def delete_client(client_id: int):
        profile_id_delete = Client.objects.filter(client_id=client_id).values_list('profile_id', flat=True)[0]

        Client.objects.filter(client_id=client_id).delete()
        Profile.delete_profile(profile_id_delete)

    @staticmethod
    def filter_by_client_id(client_id):

        return Client.objects.filter(client_id=client_id) if client_id else []

    @staticmethod
    def filter_client_by_city(city):
        profile_ids = Profile.filter_by_city(city).values('profile_id') if city else []

        return Client.objects.filter(Q(profile_id__in=profile_ids)) if city else []
