# SAML2_LIB

Modified django-saml2-auth to provide SSO functionality through SAML 2.0 in *HireXP*.

##### Flow -
> IDPs : Okta, OneLogin, ADFS, miniOrange, etc<br>
> User : Company employee who is IDP's admin.<br>
> Sub-User: An employee of User's company.
1. HireXP maintains models of IDPs it provides integration with.
2. User can configure and enable SSO from select IDPs only.

##### User's IDP is in the list-
1. User selects the IDP.
2. HireXP combines user's company's unique key, user's selected IDP's unique key from our DB and a salt(for security purposes), encodes it and generates a token to be used in **SSO URL** `https://api.hirexp.com/saml2/auth/<token>/` to uniquely and securely identify the company and the IDP.
3. User puts this URL into IDP's form while adding HireXP as Service Provider.
4. User gets `metadata.xml`'s `url` from IDP and uploads it's url into HireXP's Company's SSO Configuration Panel.
5. HireXP stores the `url` against the Company and IDP.

##### User's IDP is NOT in the list-
1. User contacts HireXP support and provides the details of the desired IDP.
2. HireXP support executive decides whether or not to allow SSO from the requested IDP.
3. If yes, then that IDP is registered into HireXP's IDPs List.
4. Now the user can follow the above procedure sinche the requested IDP is in the list.

##### User / Sub-User tries to login through SSO
1. User clicks on the HireXP app on the IDP's dashboard.
2. It sends `POST request` to **SSO URL** `https://api.hirexp.com/saml2/auth/<token>/`.
3. HireXP decodes the `token` and fetches the company and IDP object from DB.
4. In case either doesn't exists, `REDIRECT: LoginPage`, otherwise fetches the corresponding `metafile.xml` Plugs it into SAML config with other details like attribute mapping, create_user(boolean) etc. and the library does it's thing and logs the user in.
