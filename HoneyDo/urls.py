from django.urls import path
from HoneyDo import views
urlpatterns = [
    path('', views.task_list),
    path('api/tasks/', views.task_list),
    path('api/mytasks/', views.my_task_list),
    path('api/tasks/<int:pk>', views.getTask),
    path('api/lists/', views.list_list),
    path('api/lists/<int:pk>', views.getList),
    path('api/groups/', views.group_list),
    path('api/groups/<int:pk>', views.getGroup),
    path('api/profiles/', views.profile_list),
    path('api/profiles/<int:pk>', views.getProfile),
    path('api/reminders/', views.reminder_list),
    path('api/reminders/<int:pk>', views.getReminder),
    path('api/categories/', views.category_list),
    path('api/categories/<int:pk>', views.getCategory),
]