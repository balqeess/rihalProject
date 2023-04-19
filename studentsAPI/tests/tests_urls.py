from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from studentsAPI.views import students_delete, students_form, students_statistics

class TestURLS(SimpleTestCase):

    # Testing the 'students_insert' URL
    def test_urls_resolved(self):
        # to get the URL of the 'students_insert' view
        url = reverse('students_insert')
        # Asserting that the view function that the URL resolves to is students_form()
        self.assertEquals(resolve(url).func, students_form)

    def test_urls_resolved(self):
         # to get the URL of the 'students_delete' view
        url = reverse('students_delete')
        # Asserting that the view function that the URL resolves to is students_delete()
        self.assertEquals(resolve(url).func, students_delete)

    def test_urls_resolved(self):
         # to get the URL of the 'students_update' view
        url = reverse('students_update')
        # Asserting that the view function that the URL resolves to is students_form()
        self.assertEquals(resolve(url).func, students_form)
    
    def test_urls_resolved(self):
        # to get the URL of the 'students_statistics' view
        url = reverse('students_statistics')
        # Asserting that the view function that the URL resolves to is students_statistics())
        self.assertEquals(resolve(url).func, students_statistics)
    
    

    
