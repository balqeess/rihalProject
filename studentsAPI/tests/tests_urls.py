from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from studentsAPI.views import students_delete, students_form, students_statistics

class TestURLS(SimpleTestCase):

    def test_urls_resolved(self):
        url = reverse('students_insert')
        self.assertEquals(resolve(url).func, students_form)

    def test_urls_resolved(self):
        url = reverse('students_delete')
        self.assertEquals(resolve(url).func, students_delete)

    def test_urls_resolved(self):
        url = reverse('students_update')
        self.assertEquals(resolve(url).func, students_form)
    
    def test_urls_resolved(self):
        url = reverse('students_statistics')
        self.assertEquals(resolve(url).func, students_statistics)
    
    

    
