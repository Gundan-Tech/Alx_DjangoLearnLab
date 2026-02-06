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
