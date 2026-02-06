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
