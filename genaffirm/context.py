from django.conf import settings  # import the settings file


def stripe_test_mode(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {"STRIPE_TEST": settings.STRIPE_TEST}
