from apistar import Include, Route
from project.views import  create_poll, create_choices, students, all_student

routes = [
        Route('/students', 'GET', students),
	Route('/create_poll', 'POST', create_poll),
	Route('/create_choices', 'POST', create_choices),
        Route('/students/{student_num}', 'GET', all_student),
]
