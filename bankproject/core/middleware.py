# middleware.py
from django.utils import translation

class LanguagePreferenceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang_code = request.COOKIES.get('preferred_language', 'en')  # Default to English
        translation.activate(lang_code)
        request.LANGUAGE_CODE = lang_code

        response = self.get_response(request)
        response.set_cookie('preferred_language', lang_code)
        return response
