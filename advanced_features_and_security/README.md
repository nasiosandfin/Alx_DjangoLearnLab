# LibraryProject

This is my first Django project.  
It was created as part of the Introduction to Django task in Alx_DjangoLearnLab.


# Permissions and Groups Setup

- Custom permissions defined in `Book` model: can_view, can_create, can_edit, can_delete.
- Groups created via Django Admin:
  - **Viewers** → can_view
  - **Editors** → can_view, can_create, can_edit
  - **Admins** → all permissions
- Views protected with `@permission_required`.
- Test users assigned to groups to verify access control.
