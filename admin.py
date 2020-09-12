from django.contrib import admin

from home.models import Contact

from home.models import login 
from home.models import Register



# Register your models here.
admin.site.register(Contact)  
admin.site.register(login)  
admin.site.register(Register) 
 
