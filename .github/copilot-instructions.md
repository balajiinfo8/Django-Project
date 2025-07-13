# Copilot Instructions for FoodWebSite Django Projects

## Project Structure & Architecture
- This workspace contains multiple Django projects:
  - `ECOMMERCE_UI/` (main e-commerce app)
  - `mysite/` (food-related app)
  - `TODO-LIST/` (todo app)
- Each project follows standard Django conventions: `manage.py`, app directories, `settings.py`, `urls.py`, `models.py`, `views.py`, `templates/`, and `static/`.
- Media files (e.g., product images) are stored in `media/` directories within each project.
- Templates are organized per app (e.g., `food/templates/food/`, `ecommerce/templates/`).

## Key Workflows
- **Run development server:**
  - `python manage.py runserver` (from the relevant project directory)
- **Apply migrations:**
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- **Create superuser:**
  - `python manage.py createsuperuser`
- **Database:**
  - Uses SQLite by default (`db.sqlite3` in each project).

## Patterns & Conventions
- Views are function-based by default (see `food/views.py`, `ecommerce/views.py`).
- Template rendering uses context dictionaries (e.g., `context = {'item_list': item_list}` in views).
- Static and media files are referenced via Django's static/media settings; see `static/` and `media/` folders.
- URL routing is defined per app in `urls.py` and included in the project's main `urls.py`.
- Models are defined in each app's `models.py` and registered in `admin.py`.

## Integration Points
- No external APIs or third-party integrations are present by default.
- All dependencies are standard Django; install with `pip install django` if needed.

## Examples
- To add a new view, define a function in `views.py`, add a URL pattern in `urls.py`, and create a template in the app's `templates/` folder.
- Example view (from `food/views.py`):
  ```python
  def index(request):
      item_list = Item.objects.all()
      context = {'item_list': item_list}
      return render(request, 'food/index.html', context)
  ```

## References
- Key files: `manage.py`, `settings.py`, `urls.py`, `views.py`, `models.py`, `templates/`, `static/`, `media/`
- For project-specific logic, see each app's directory under the main project folder.

---
If any conventions or workflows are unclear, please provide feedback for clarification or expansion.
