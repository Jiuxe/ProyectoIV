import hug
# from QueTocaBBDD import Horario

# horario=Horario()

@hug.get('/')
def index():
	"""Devuelve estado"""
	return { "status": "OK" }

@hug.get('/status')
def status():
	"""Devuelve estado"""
	return { "status": "OK" }

# @hug.get('/horario')
# def actividades_bd():
# 	info = horario.LeerHorario("D1")
# 	return { "Horario": info }

# @hug.get('/unhorario/{id}')
# def one ( id: int ):
# 	info = horario.LeerHorario(id)
# 	return { "Horario": info }
