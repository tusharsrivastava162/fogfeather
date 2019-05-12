SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    # Okta
    # 'METADATA_AUTO_CONF_URL': 'https://outlooksso.okta.com/app/exkie6pfvsrL6Q4rr356/sso/saml/metadata',

    # OneLogin
    'METADATA_AUTO_CONF_URL': 'https://app.onelogin.com/saml/metadata/31ccd229-4ed0-4d16-88b9-81e1cc76d69f',
    # 'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',

    # Optional settings below
    # 'DEFAULT_NEXT_URL': '/',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': True,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    # OneLogin
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'username',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
    },
    # Okta
    # 'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
    #     'email': 'email',
    #     'username': 'email',
    #     'first_name': 'firstName',
    #     'last_name': 'lastName',
    # },
    # 'TRIGGER': {
    #     'CREATE_USER': 'path.to.your.new.user.hook.method',
    #     'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    # },
    'ASSERTION_URL': 'http://52.66.250.136:8800', # Custom URL to validate incoming SAML requests against
    'ENTITY_ID': 'http://52.66.250.136:8800/saml2_auth/acs/', # Populates the Issuer element in authn request
    'USE_JWT': True, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'http://52.66.250.136', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

import json

json.dump(SAML2_AUTH, open('appinventiv.onelogin.json', 'w'), indent=4)
