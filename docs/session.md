# URL Shortener Session System

### User Dashboard

Welcome message on the logged in user dashboard is control using the Django session, while processing the request, the key "welcome" (default "False" signifying the welcome message is not displayed) in session is set to "True" (welcome message is displayed) for future use. When another request for Dashboard is processed, django does not load the welcome message in response.