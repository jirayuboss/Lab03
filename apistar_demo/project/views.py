from apistar.backends import SQLAlchemy
from project.models import Poll, Choice
import json

student_id= {
    59011597: {'id': '59011597', 'firstname': 'Chatchanok', 'lastname': 'Wongsamang'},
    59011598: {'id': '59011598', 'firstname': 'Jiramate', 'lastname': 'Leingprom'},
    59011599: {'id': '59011599', 'firstname': 'Jirayu', 'lastname': 'Promsongwong'},
    59011600: {'id': '59011600', 'firstname': 'Kitpol', 'lastname': 'Tansakul'},
    59011601: {'id': '59011601', 'firstname': 'Nattamon', 'lastname': 'Sridam'},
    59011602: {'id': '59011602', 'firstname': 'Peeranat', 'lastname': 'Limpitaporn'},
    59011604: {'id': '59011604', 'firstname': 'Phison', 'lastname': 'Khankang'},
    59011605: {'id': '59011605', 'firstname': 'Thirawat', 'lastname': 'Rungrotchaiyaporn'},
}

json_stringlist = json.dumps(list(student_id.values()))

def create_poll(db: SQLAlchemy, question: str):
    session = db.session_class()
    poll = Poll(question=question)
    session.add(poll)
    session.commit()
    return {'question': question}
    
def create_choices(db: SQLAlchemy, poll_id: int, choice_text: str):
    session = db.session_class()
    poll = session.query(Poll).get(poll_id)
    choice = Choice(poll=poll.id, choice_text=choice_text, votes=0)
    session.add(choice)
    session.commit()
    return {'choice_text': choice_text}

def students():
    return json_stringlist

def all_student(student_num: int):
    return json.dumps(student_id[student_num])
