from django.contrib import admin
from .models import Registrator, Domain, Parse_History, Parser, Price, Parse_Error

admin.site.register(Registrator)
admin.site.register(Domain)
admin.site.register(Parse_History)
admin.site.register(Parser)
admin.site.register(Price)
admin.site.register(Parse_Error)
