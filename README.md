![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!


------------- D E L E T E ------------

Commands:

`heroku_config`

# Install program in gitpod and codeanywhere

pip3 install 'django<4' gunicorn <br>
django-admin startproject boutique_ado . <br>
pip3 install dj_database_url psycopg2 <br>
pip3 install dj3-cloudinary-storage <br>
pip3 install django-allauth <br>
pip3 install django-crispy-forms <br>
pip3 install django-summernote <br>
pip3 install django-allauth <br>
pip install crispy-bootstrap5 <br>
pip3 install Pillow <br>

pip3 freeze > requirements.txt <br>

## Terminal code to remeber

python3 manage.py makemigrations --dry-run <br>
python3 manage.py showmigrations <br>
python3 manage.py migrate --plan <br>
python3 manage.py makemigrations <br>
python3 manage.py migrate <br>
python3 manage.py runserver <br>
pip install fontawesomefree <br>

# For env.py

import os <br>

os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL" <br>
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey" <br>
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"

-------------------------- NOTES -----------------------------
A Django model defines the fields and data behaviour's of the structured database.Therefore I would say that changing the field names alone of an existing walkthrough project model is not custom.What is custom is changing the field     types, options and relationships of an existing walkthrough project model. Also custom is creating a new model for the students project requirements where the field names, types options and relationships are appropriate for the user story. I hope that is clearer.

<https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+ECOMM_PAGPPF+2021_Q2/courseware/c38cb7ad50e9443dbd94f4cef3fed1ae/0b467723b3f54a5db85c975fdf67116d/>


git commit -m "Add products views and templates"

    {% block corecss %}
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato&display=swap">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Alegreya+Sans+SC:wght@800&family=Overpass:wght@300&family=Rajdhani:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"> -->
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    {% endblock %}


    {% block corejs %}
    <script src="https://kit.fontawesome.com/e9c73d7092.js" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <!-- <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

    <script src="https://kit.fontawesome.com/02d1f83f71.js" crossorigin="anonymous"></script> -->
    {% endblock %}
