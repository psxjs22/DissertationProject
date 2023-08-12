from django.contrib import admin

from basicapp.models import TreatmentGroup, ConsentForm, Participant, Demographic, Question, Response


admin.site.register(TreatmentGroup)
admin.site.register(ConsentForm)
admin.site.register(Participant)
admin.site.register(Demographic)
admin.site.register(Question)
admin.site.register(Response)
