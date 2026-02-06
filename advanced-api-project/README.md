## Book API Endpoints

| Endpoint                      | Method    | Action            | Permission      |
| :---------------------------- | :-------- | :---------------- | :-------------- |
| `/api/books/`                 | GET       | List all books    | AllowAny        |
| `/api/books/<int:pk>/`        | GET       | View book details | AllowAny        |
| `/api/books/create/`          | POST      | Create a new book | IsAuthenticated |
| `/api/books/update/<int:pk>/` | PUT/PATCH | Edit a book       | IsAuthenticated |
| `/api/books/delete/<int:pk>/` | DELETE    | Delete a book     | IsAuthenticated |

**Custom Logic:**
The `BookSerializer` ensures that the `publication_year` cannot be in the future.
Authentication is required for all write operations (Create, Update, Delete).

## Testing Strategy

The API is tested using Django REST Framework's `APITestCase`.

### Coverage Includes:

1. **CRUD Operations**: Verification of Create, Read, Update, and Delete actions.
2. **Permissions**: Ensuring `IsAuthenticatedOrReadOnly` restricts write access to logged-in users.
3. **Data Integrity**: Checking that valid data is saved correctly and invalid data (e.g., future dates) is rejected via Serializer validation.
4. **Query Parameters**: Testing that `filters`, `search`, and `ordering` produce correct subsets of data.

### Running Tests:

To execute the suite, run:
`python manage.py test api`
