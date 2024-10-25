from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'textbook', viewset=views.TextbookViewset, basename='textbook')
router.register(r'exercises', viewset=views.ExerciseViewset, basename='exercises')

urlpatterns = router.urls

