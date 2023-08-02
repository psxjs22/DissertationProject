from django.contrib import admin

from basicapp.models import TreatmentGroup, ConsentForm, Participant, Demographics, Quiz, Question, Answers, Responses


admin.site.register(TreatmentGroup)
admin.site.register(ConsentForm)
admin.site.register(Participant)
admin.site.register(Demographics)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Responses)
