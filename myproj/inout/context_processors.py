from django.db.models.signals import post_save
from django.dispatch import receiver
from inout.models import user_ticket,save_random_number
from django.conf import settings
def add_variable_to_context(request):
        random_data=save_random_number.objects.all()


        return {'data143': random_data}
    ##return context
##    return context
