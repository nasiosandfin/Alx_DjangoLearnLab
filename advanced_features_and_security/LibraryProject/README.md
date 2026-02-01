# Permissions and Groups Setup

## Custom Permissions
- Defined in `bookshelf/models.py` for the `Book` model:
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

## Groups
- **Viewers** → assigned `can_view`
- **Editors** → assigned `can_view`, `can_create`, `can_edit`
- **Admins** → assigned all permissions

## Views
- Protected with `@permission_required` decorators:
  - `book_list` → requires `can_view`
  - `book_create` → requires `can_create`
  - `book_edit` → requires `can_edit`
  - `book_delete` → requires `can_delete`

## Testing
- Create test users in Django Admin.
- Assign them to groups.
- Verify that access is restricted/enabled based on permissions.

