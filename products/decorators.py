from contrib.auth.decorators import user_passes_test

def staff_required():
    return user_passes_test(lambda u: u.is_staff)