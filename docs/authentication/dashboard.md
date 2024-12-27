# Dashboard Tests

1. Test auth user: When a user login, user will be redirected to dashboard.
2. Test authenticated user: When a unauthenticated try to access the dashboard, directly using url, will be redirect to Login, with query_string `redirect_to` to Dashboard