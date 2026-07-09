# Fakhar Naseer — Dynamic Django Portfolio

A dynamic personal portfolio website built with Django for the Web Technologies term project.
All content (Bio, Education, Skills, Experience, Projects) is stored in the database and
fetched dynamically through Django models, views, and templates — nothing is hardcoded in HTML.

## Project structure (one app per section, as required)

- `bio/` — Bio model (name, job title, photo, description, contact/social links) + the main `home` view
- `education/` — Education model (degree, institution, duration, score)
- `skills/` — Skill model and Software model (name + star rating)
- `experience/` — Experience model (work experience entries) and Project model (portfolio projects)

Templates live in `templates/` (project-level), static files (CSS) in `static/`,
and uploaded images (profile photo, project thumbnails) in `media/`.

## Setup — run locally

```bash
# 1. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Seed the database with the portfolio content + admin user
python manage.py seed_data

# 5. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` for the admin panel.

## Admin panel login

- **Username:** `admin`
- **Password:** `admin@`

Use the admin panel to edit Bio, add/remove Education entries, Skills, Software, Work Experience,
and Projects (including uploading project thumbnail images) without touching any code.

## Adding project thumbnails / more projects

Project entries were seeded from the CV (E-Shopping Website, Short Film, Creative Reels & VFX Edits,
Zombie Survival Game in Unity). The C++ university projects were intentionally left out for now —
add them later from the admin panel (`Experience → Projects → Add Project`) once you have the details,
along with thumbnail images and links if available.

## Theme

White + sky-blue, with a bokeh (blurred light circles) motif behind the hero — a nod to
photography/videography — and a film-sprocket strip top and bottom. Timecodes (00:00, 00:01 ...)
are used as the section navigation, fitting for a video editor's portfolio.

## Skills

The Skill model now has a `category` field (`creative` or `technical`) so the Skills section shows
Creative Skills (Videography, Photography, Video Editing, etc.), Technical Skills (Python, Django,
C++, C#, JavaScript, HTML & CSS), and Software separately. Adjust star ratings from the admin panel
any time.

## Social links

Bio now includes Instagram, Facebook, and GitHub — shown both in the hero and the contact footer.

## Notes on deployment

This is a full Django (backend + database) application. A plain **Netlify** deployment only serves
static files and cannot run a Django/Python backend by itself — it would need to be adapted
(e.g. via Netlify Functions with a serverless adapter, or run through a WSGI-capable host like
Render, Railway, or PythonAnywhere and pointed to at the required `<student_id>.netlify.app`
style domain via redirect). Deployment isn't covered in this delivery — ask separately when you're
ready and we'll figure out the right approach for your assignment's deployment requirement.
