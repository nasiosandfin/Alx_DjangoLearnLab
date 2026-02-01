
---

## 📄 `CRUD_operations.md`
This file combines all four operations:

```markdown
# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output: <Book: 1984 by George Orwell (1949)>
