
---

## 📄 `update.md`
```markdown
# Update Operation

```python
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
