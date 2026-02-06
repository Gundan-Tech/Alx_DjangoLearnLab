\# LibraryProject

This is the initial Django project setup for the ALX Django learning lab.

# Permissions and Groups Setup

## Custom Permissions

The `Book` model in the `bookshelf` app includes the following custom permissions:

- `can_view`: Allows users to view the book list.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify existing book details.
- `can_delete`: Allows users to remove books from the library.

## Groups

1. **Viewers**: Assigned the `can_view` permission.
2. **Editors**: Assigned `can_view`, `can_create`, and `can_edit` permissions.
3. **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

# Security Implementations

1. **Browser Protections**: `X_FRAME_OPTIONS`, `SECURE_BROWSER_XSS_FILTER`, and `SECURE_CONTENT_TYPE_NOSNIFF` prevent Clickjacking, XSS, and MIME-sniffing.
2. **Cookie Security**: `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` ensure cookies are only transmitted over HTTPS.
3. **SQL Injection Prevention**: All views use the Django ORM and Forms for data handling, ensuring parameterized queries.
4. **CSRF Protection**: All POST forms utilize the `{% csrf_token %}` tag.
