from django.urls import path
from django.urls.conf import include

from . import views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register('academicpower',views.Academic_power)
router.register('year',views.Year)
router.register('ServiceManpower',views.Service_Manpower)
router.register('Events',views.Event)
router.register('Budgets',views.Budget)
router.register('AcademiceOutstand',views.Academice_Outstand)
router.register('ServiceOutstand',views.Service_Outstand)
router.register('leavetime',views.leave_time)
router.register('Studyleave',views.Study_leave)
router.register('Pendings',views.Pending)
router.register('Documents',views.Document)
router.register('Approvals',views.Approval)
router.register('Yearplan',views.Year_plan)
router.register('Humanresource',views.Human_resource)
router.register('Reports',views.Report)


urlpatterns = [
    path('',include(router.urls)),
]