from db import session
from models import Subscriber, Newsletter, Engagement
from utils import log_event, export_subscribers_csv, import_subscribers_json, analyze_performance

def add_subscriber():
    name = input("Enter name: ")
    email = input("Enter email: ")
    subscriber = Subscriber(name=name, email=email)
    session.add(subscriber)
    session.commit()
    print(" Subscriber added!")


def remove_subscriber():
    email = input("Enter subscriber email to remove: ")
    sub = session.query(Subscriber).filter_by(email=email).first()
    if sub:
        sub.status = "unsubscribed"
        log_event("unsubscribe_log.txt", f"Unsubscribed: {sub.email}")
        session.commit()
        print(" Subscriber unsubscribed.")
    else:
        print(" Subscriber not found.")


def send_newsletter():
    title = input("Enter newsletter title: ")
    content = input("Enter content: ")

    newsletter = Newsletter(title=title, content=content)
    session.add(newsletter)
    session.commit()

    subscribers = session.query(Subscriber).filter_by(status="active").all()
    for sub in subscribers:
        engagement = Engagement(subscriber_id=sub.id, newsletter_id=newsletter.id)
        session.add(engagement)
    session.commit()

    print(f" Newsletter '{title}' sent to {len(subscribers)} subscribers.")


def record_engagement():
    email = input("Enter subscriber email: ")
    title = input("Enter newsletter title: ")

    sub = session.query(Subscriber).filter_by(email=email).first()
    nl = session.query(Newsletter).filter_by(title=title).first()

    if sub and nl:
        eng = session.query(Engagement).filter_by(subscriber_id=sub.id, newsletter_id=nl.id).first()
        if eng:
            opened = input("Opened? (y/n): ") == "y"
            clicked = input("Clicked? (y/n): ") == "y"
            eng.opened = opened
            eng.clicked = clicked
            session.commit()
            print("Engagement recorded.")
        else:
            print(" Engagement record not found.")
    else:
        print(" Subscriber or newsletter not found.")


def export_subscribers():
    subscribers = session.query(Subscriber).all()
    export_subscribers_csv(subscribers)


def import_subscribers():
    filename = input("Enter JSON filename: ")
    data = import_subscribers_json(filename)
    for item in data:
        subscriber = Subscriber(name=item["name"], email=item["email"])
        session.add(subscriber)
    session.commit()
    print(" Subscribers imported from JSON")


def analyze():
    engagements = session.query(Engagement).all()
    analyze_performance(engagements)
