import os
from django.conf import settings

DEFAULT_CONFIG = {
   'plugins': "fullscreen,paste,autoresize",
   'theme': "advanced",
   'theme_advanced_buttons1' : "bold,italic,strikethrough,bullist,numlist,justifyleft,justifycenter,justifyright,justifyfull,"\
                               "separator,undo,redo,separator,link,unlink,image"\
                               ",separator,cleanup,code,removeformat,charmap,"\
                               "fullscreen,paste",
   'theme_advanced_buttons2' : "",
   'theme_advanced_buttons3' : "",
   'theme_advanced_resizing' : 'true',
   'file_browser_callback': 'mce_filebrowser',
   'plugins' : "advimage",
}

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL',os.path.join(settings.STATIC_URL, 'tiny_mce/tiny_mce.js'))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT',os.path.join(settings.STATIC_ROOT, 'tiny_mce'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL','%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL)
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
