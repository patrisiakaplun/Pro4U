from django.urls import reverse
from reservation.models import TypeOfJob
from reservation.forms import TypeOfJobForm
import pytest


@pytest.fixture
def save_type_of_job(make_typeOfJob):
    typeOfJob = make_typeOfJob()
    typeOfJob.professional_id.save()
    typeOfJob.save()
    return typeOfJob


@pytest.mark.django_db
class TestTypeOfJob:
    def test_typeOfJob_list(self, client, professional):
        response = client.get(reverse('typeOfJob', kwargs={'professional': professional.pk}))
        assert response.status_code == 200
        assert 'reservation/typeOfJob_list.html' in response.templates[0].name

    def test_create_typeOfJob(self, client, professional, save_type_of_job):
        response = client.get(reverse('typeOfJob_create', kwargs={'professional': professional.pk}))
        assert response.status_code == 200
        assert 'reservation/typeOfJob_form.html' in response.templates[0].name

        data = {
            'typeOfJob_name': 'Woman haircut',
            'price': 200,
        }

        response = client.post(reverse('typeOfJob_create', kwargs={'professional': professional.pk}), data)
        assert response.status_code == 302
        assert TypeOfJob.objects.filter(professional_id=professional).count() == 2
        assert response.url == reverse('typeOfJob', kwargs={'professional': professional.pk})

    def test_typeOfJob_update(self, client, professional, save_type_of_job):
        url = reverse('typeOfJob_update', args=[save_type_of_job.pk])
        response = client.get(url)
        assert response.status_code == 200

        data = {
            'typeOfJob_name': 'Updated Type of Job',
            'price': 150,
        }

        response = client.post(url, data)
        assert response.status_code == 302
        save_type_of_job.refresh_from_db()
        assert save_type_of_job.typeOfJob_name == 'Updated Type of Job'
        assert save_type_of_job.price == 150
        assert TypeOfJob.objects.filter(professional_id=professional).count() == 1

    def test_typeOfJob_delete(self, client, professional, save_type_of_job):
        url = reverse('typeOfJob_delete', args=[save_type_of_job.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert TypeOfJob.objects.filter(professional_id=professional).count() == 0

    def test_form_validity(self):
        data = {
            'typeOfJob_name': 'Woman haircut',
            'price': 200,
        }

        form = TypeOfJobForm(data)
        assert form.is_valid()
