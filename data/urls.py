from os import stat
from django.urls import path
from django.urls.conf import include

from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()

router.register('academicpower',views.Academic_power)
router.register('year',views.Year)
router.register('serviceManpower',views.Service_Manpower)
router.register('events',views.Event)
router.register('budgets',views.Budget)
router.register('academiceOutstand',views.Academice_Outstand)
router.register('serviceOutstand',views.Service_Outstand)
router.register('leavetime',views.leave_time)
router.register('studyleave',views.Study_leave)
router.register('pendings',views.Pending)
router.register('documents',views.Document)
router.register('approvals',views.Approval)
router.register('yearplan',views.Year_plan)
router.register('humanresource',views.Human_resource)
router.register('reports',views.Report)


urlpatterns = [
    path('',include(router.urls)),
]