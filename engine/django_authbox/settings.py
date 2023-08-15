_q='MAIN_DOMAIN'
_p='backgroundColors'
_o='borderColors'
_n='tableCellProperties'
_m='tableProperties'
_l='styles'
_k='heading3'
_j='heading2'
_i='heading1'
_h='paragraph'
_g='mediaEmbed'
_f='fontSize'
_e='italic'
_d='templates'
_c='DB_NAME'
_b='ALLOWED_HOSTS'
_a='SECRET_KEY'
_Z='DB_PASSWORD'
_Y='BACKEND'
_X='allauth'
_W='view'
_V='blockQuote'
_U='numberedList'
_T='bulletedList'
_S='heading'
_R='toolbar'
_Q='/dashboard/'
_P='code'
_O='ENGINE'
_N='environment'
_M='class'
_L='title'
_K='model'
_J='true'
_I='DIRS'
_H='id'
_G='label'
_F='color'
_E=False
_D='default'
_C='NAME'
_B=True
_A='|'
import os
from pathlib import Path
from encryption import OutboxEncryption
from django.utils.translation import gettext_lazy as _
BASE_DIR=Path(__file__).resolve().parent.parent
BASE_DIR_1=os.path.normpath(os.path.join(BASE_DIR,'..'))
BASE_DIR_2=os.path.normpath(os.path.join(BASE_DIR_1,'..'))
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.sites','django.contrib.humanize',_X,'allauth.account','allauth.socialaccount','allauth.socialaccount.providers.google','allauth.socialaccount.providers.facebook','allauth.socialaccount.providers.github','captcha','multiselectfield','parler','crispy_forms','crispy_bootstrap4','django_ckeditor_5','debug_toolbar','cachalot','menu','region','outbox_hitcount','hitcount','core','backend','frontend']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.locale.LocaleMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='django_authbox.urls'
TEMPLATES=[{_Y:'django.template.backends.django.DjangoTemplates',_I:[],'APP_DIRS':_B,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages','frontend.processor.context_outbox','backend.processor.context_outbox','backend.processor.get_main_domain','backend.processor.site_id','backend.processor.version']}}]
WSGI_APPLICATION='django_authbox.wsgi.application'
LIB=OutboxEncryption(os.path.join(BASE_DIR,_N))
file_name=LIB.scan_environment_variable()
file_name_color='\x1b[91m'+file_name+'\x1b[0m'
file_path=os.path.join(BASE_DIR,_N,file_name)
file_path_color=os.path.join(BASE_DIR,_N,file_name_color)
if not Path(file_path).is_file():raise Exception(f"[1m File Not found: [0m {file_path_color}")
PLAINT_KEY=[_Z,_a]
PLAINT_LIST=[_b]
KEY=LIB.dec_environ(PLAINT_KEY,PLAINT_LIST)
DB_ENGINE=KEY['DB_ENGINE']
if'sqlite3'in DB_ENGINE:
	db_name=KEY[_c]
	if db_name.find('/')<0 and db_name.find('\\')<0:DATABASES={_D:{_O:DB_ENGINE,_C:os.path.join(BASE_DIR,'db',db_name)}}
	else:DATABASES={_D:{_O:DB_ENGINE,_C:db_name}}
else:DATABASES={_D:{_O:DB_ENGINE,_C:KEY[_c],'USER':KEY['DB_USER'],'PASSWORD':KEY[_Z],'HOST':KEY['DB_HOST'],'PORT':KEY['DB_PORT']}}
AUTH_PASSWORD_VALIDATORS=[{_C:'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{_C:'django.contrib.auth.password_validation.MinimumLengthValidator'},{_C:'django.contrib.auth.password_validation.CommonPasswordValidator'},{_C:'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE=_H
TIME_ZONE='Asia/Makassar'
USE_I18N=_B
USE_L10N=_B
USE_TZ=_E
STATIC_URL='/static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
SITE_ID=1
CONTRIBUTE_PATH=os.path.join(BASE_DIR_2,'authbox-contribute','clothes')
TEMPLATES[0][_I].clear()
TEMPLATES[0][_I].append(os.path.join(CONTRIBUTE_PATH,_d))
TEMPLATES[0][_I].append(os.path.join(CONTRIBUTE_PATH,_d,_X))
STATIC_ROOT=os.path.join(CONTRIBUTE_PATH,'staticfiles')
STATICFILES_DIRS=[os.path.join(CONTRIBUTE_PATH,'static')]
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(CONTRIBUTE_PATH,'media')
DEBUG_TOOLBAR_PANELS=['cachalot.panels.CachalotPanel','debug_toolbar.panels.history.HistoryPanel','debug_toolbar.panels.versions.VersionsPanel','debug_toolbar.panels.timer.TimerPanel','debug_toolbar.panels.settings.SettingsPanel','debug_toolbar.panels.headers.HeadersPanel','debug_toolbar.panels.request.RequestPanel','debug_toolbar.panels.sql.SQLPanel','debug_toolbar.panels.staticfiles.StaticFilesPanel','debug_toolbar.panels.templates.TemplatesPanel','debug_toolbar.panels.cache.CachePanel','debug_toolbar.panels.signals.SignalsPanel','debug_toolbar.panels.redirects.RedirectsPanel','debug_toolbar.panels.profiling.ProfilingPanel']
MIDDLEWARE+=['debug_toolbar.middleware.DebugToolbarMiddleware','frontend.request_exposer.RequestExposerMiddleware']
DEBUG=KEY['DEBUG']
UNDER_CONSTRUCTION=KEY['UNDER_CONSTRUCTION']
SECRET_KEY=KEY[_a]
ALLOWED_HOSTS=KEY[_b]
HITCOUNT_KEEP_HIT_IN_DATABASE={'months':3}
HITCOUNT_KEEP_HIT_ACTIVE={'minutes':1}
LANGUAGES=(_H,_('Indonesia')),('en',_('English'))
LOCALE_PATHS=[os.path.join(BASE_DIR,'locale')]
PARLER_DEFAULT_LANGUAGE_CODE=_H
PARLER_LANGUAGES={1:({_P:_H},{_P:'en'}),_D:{'fallbacks':[_H],'hide_untranslated':_E}}
RECAPTCHA_PUBLIC_KEY='6Le_ixcmAAAAABbCXol2K5HaE0vY906KKFrFm0PX'
RECAPTCHA_PRIVATE_KEY='6Le_ixcmAAAAAFeqpjBlKQcgDkPxZjMmk--cuEZU'
IMPORT_EXPORT_USE_TRANSACTIONS=_B
LOGIN_REDIRECT_URL=_Q
LOGOUT_REDIRECT_URL=_Q
AUTH_USER_MODEL='core.User'
ACCOUNT_FORMS={'login':'core.forms.UserLoginForm','reset_password':'core.forms.UserResetPasswordForm','signup':'core.forms.UserSignupForm'}
AUTHENTICATION_BACKENDS=['allauth.account.auth_backends.AuthenticationBackend']
EMAIL_USE_SSL=_E
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='auto.email.activation@gmail.com'
EMAIL_HOST_PASSWORD='hpsodjhhkhaemoir'
EMAIL_PORT=587
EMAIL_USE_TLS=_B
DEFAULT_FROM_EMAIL='AUTHBOX.web.id'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS=_E
ACCOUNT_LOGIN_ON_PASSWORD_RESET=_B
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=_B
ACCOUNT_USERNAME_MIN_LENGTH=4
ACCOUNT_SESSION_REMEMBER=_B
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=_B
ACCOUNT_LOGIN_ATTEMPTS_LIMIT=5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=86400
ACCOUNT_LOGOUT_REDIRECT_URL=_Q
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_UNIQUE_EMAIL=_B
ACCOUNT_USER_MODEL_USERNAME_FIELD=None
ACCOUNT_USERNAME_REQUIRED=_E
ACCOUNT_LOGOUT_ON_GET=_B
SOCIALACCOUNT_LOGIN_ON_GET=_E
SENDGRID_API_KEY='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'
CACHES={_D:{_Y:'django.core.cache.backends.locmem.LocMemCache','LOCATION':'unique-snowflake'}}
CACHES_TIMEOUT=24*60*60
INTERNAL_IPS=['127.0.0.1','localhost','authbox.web.id']
customColorPalette=[{_F:'hsl(4, 90%, 58%)',_G:'Red'},{_F:'hsl(340, 82%, 52%)',_G:'Pink'},{_F:'hsl(291, 64%, 42%)',_G:'Purple'},{_F:'hsl(262, 52%, 47%)',_G:'Deep Purple'},{_F:'hsl(231, 48%, 48%)',_G:'Indigo'},{_F:'hsl(207, 90%, 54%)',_G:'Blue'}]
CKEDITOR_5_CONFIGS={_D:{_R:[_S,_A,'bold',_e,'link',_T,_U,_V,'imageUpload',_f]},'extends':{'blockToolbar':[_h,_i,_j,_k,_A,_T,_U,_A,_V],_g:{'previewsInData':_J},_R:[_S,_A,'outdent','indent',_A,'alignment',_A,'bold',_e,'underline','strikethrough',_A,'link',_A,_P,'subscript','superscript','highlight',_A,_T,_U,'todoList',_A,'codeBlock','sourceEditing','insertImage',_A,_V,_A,'fontFamily',_f,'fontColor','fontBackgroundColor',_g,'removeFormat','insertTable'],'image':{_R:['imageTextAlternative',_A,'imageStyle:alignLeft','imageStyle:alignRight','imageStyle:alignCenter','imageStyle:side',_A],_l:['full','side','alignLeft','alignRight','alignCenter']},'table':{'contentToolbar':['tableColumn','tableRow','mergeTableCells',_m,_n],_m:{_o:customColorPalette,_p:customColorPalette},_n:{_o:customColorPalette,_p:customColorPalette}},_S:{'options':[{_K:_h,_L:'Paragraph',_M:'ck-heading_paragraph'},{_K:_i,_W:'h1',_L:'Heading 1',_M:'ck-heading_heading1'},{_K:_j,_W:'h2',_L:'Heading 2',_M:'ck-heading_heading2'},{_K:_k,_W:'h3',_L:'Heading 3',_M:'ck-heading_heading3'}]}},'list':{'properties':{_l:_J,'startIndex':_J,'reversed':_J}}}
CRISPY_TEMPLATE_PACK='bootstrap4'
tmp=KEY.get(_q)
MAIN_DOMAIN=KEY[_q]if tmp else'127.0.0.1:8000'