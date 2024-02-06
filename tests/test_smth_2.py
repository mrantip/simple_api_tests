import requests
from configuration import SERVICE_URL2
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL2)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)



# z = {'meta':
#          {'pagination':
#               {'total': 2966, 'pages': 297, 'page': 1, 'limit': 10,
#                'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1',
#                          'next': 'https://gorest.co.in/public/v1/users?page=2'}
#                }},
#      'data': [
#          {'id': 6140420, 'name': 'Mrs. Amish Dwivedi', 'email': 'dwivedi_amish_mrs@funk.test', 'gender': 'female',
#           'status': 'active'},
#          {'id': 6140419, 'name': 'Somnath Namboothiri', 'email': 'namboothiri_somnath@effertz.test', 'gender': 'female',
#           'status': 'inactive'},
#          {'id': 6140418, 'name': 'Rajinder Ganaka JD', 'email': 'jd_rajinder_ganaka@oreilly-ward.test',
#           'gender': 'male',
#           'status': 'inactive'},
#          {'id': 6140417, 'name': 'Prof. Trilokesh Devar', 'email': 'prof_trilokesh_devar@hilpert.test',
#           'gender': 'female',
#           'status': 'inactive'},
#          {'id': 6140416, 'name': 'Menka Talwar', 'email': 'talwar_menka@dietrich.test', 'gender': 'male',
#           'status': 'inactive'},
#          {'id': 6140415, 'name': 'Hiranmay Rana', 'email': 'hiranmay_rana@muller.example', 'gender': 'male',
#           'status': 'inactive'},
#          {'id': 6140413, 'name': 'Dhatri Khatri', 'email': 'khatri_dhatri@zulauf.example', 'gender': 'female',
#           'status': 'inactive'},
#          {'id': 6140414, 'name': 'Adhrit Pillai', 'email': 'adhrit_pillai@ortiz.test', 'gender': 'male',
#           'status': 'inactive'},
#          {'id': 6140412, 'name': 'Atreyee Mehrotra', 'email': 'atreyee_mehrotra@lebsack.example', 'gender': 'male',
#           'status': 'active'},
#          {'id': 6140411, 'name': 'Msgr. Kanti Dubashi', 'email': 'msgr_kanti_dubashi@lowe.test', 'gender': 'female',
#           'status': 'inactive'}]}
