from flask import Flask, render_template, redirect, url_for
from .forms import Ad_Event, RegisterAttendee


# Integrantes
# Juan Esteban Bedoya Vasquez
# Jhotin Posada Cano


events = [
    {
        "id": 1,
        "title": "Conferencia de Python",
        "slug": "python_conference",
        "description": "A python conference",
        "date": "2025-09-15",
        "time": "14:00",
        "location": "Principal Auditorium",
        "category": "Technology",
        "max_attendees": 50,
        "attendess": [
            {"name": "juan perez", "email": "juan@example.com"},
            {"name": "juan perez", "email": "juan@example.com"},
        ],
        "featured": True,
    }
]

categories = ["Technology", "Academic", "Cultural", "Sports", "Social"]
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html", events=events)


@app.route("/event/<slug>/")
def event_detail(slug):
    for event in events:
        if event["slug"] == slug:
            return render_template("event_detail.html", event=event)
    return "Event Not Found", 404


# @app.route("admin/event")
# def admin():
#     pass


@app.route("/event/category/<category>/")
def event_filter_by_cartegory(category: str):
    if category not in categories:
        return "Category Not Found", 404
    filtered_events = list(
        filter(lambda event: True if event["category"] == category else False, events)
    )
    return render_template("index.html", events=filtered_events)


@app.route("/event/<int:id>/register/", methods=["GET", "POST"])
def register_for_event(id):
    form = RegisterAttendee()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        print(name, email)
        return redirect(url_for("index"))

    return render_template("register_attende_form.html", form=form)
