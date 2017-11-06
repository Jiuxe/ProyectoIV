# # -*- coding: utf-8 -*-
# import json
#
# class QueToca:
# 	"""Clase que gestiona las horas de clase"""
#
# 	def __init__(self):
# 		try:
# 			with open('./horario.json') as datos:
# 				self.horario = json.load(datos)
# 		except IOError as fallo:
# 			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)
#
#
# 	def CrearHorario(curso=None, grupo=None, asignatura=None, hora_inicio=None, hora_fin=None, fecha=None, aula=None, profesor=None):
# 		curso = 4
# 		if curso > 5 or curso < 0:
# 			raise IndexError("Error en el numero de curso.")
#
# 		datos = {
# 			"curso": curso,
# 			"grupo": "A",
# 			"asignatura": "Infraestructura Virtual",
# 			"hora_inicio": "9:30",
# 			"hora_fin": "10:30",
# 			"fecha": "05/10/2017",
# 			"aula": "1.2",
# 			"profesor": "JJ"
# 		}
# 		try:
# 			with open('./nuevo_horario.json', 'w') as nuevo:
# 				json.dump(datos, nuevo)
# 				return True
# 		except IOError as fallo:
# 			print("Error %d escribiendo nuevo_horario.json: %s", fallo.errno, fallo.strerror)
#
#
# 	def LeerHorario(curso=None, grupo=None):
# 		try:
# 			with open('./horario.json') as datos:
# 				horario_leido = json.load(datos)
# 		except IOError as fallo:
# 			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)
# 		return str(horario_leido)
#
#
# 	def ModificarHorario(nuevo_curso=None, nuevo_grupo=None, nueva_asignatura=None,
# 						 nueva_hora_inicio=None, nueva_hora_fin=None, nueva_fecha=None, nuevo_aula=None, nuevo_profesor=None):
# 		try:
# 			with open('./horario.json') as datos:
# 				horario_modificado = json.load(datos)
# 		except IOError as fallo:
# 			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)
#
# 		nuevo_curso = 3
# 		if nuevo_curso == None or nuevo_curso > 5 or nuevo_curso < 0:
# 			horario_modificado["curso"] = horario_modificado["curso"]
# 		else:
# 			horario_modificado["curso"] = nuevo_curso
#
# 		nuevo_grupo = "B"
# 		if nuevo_grupo != None:
# 			horario_modificado["grupo"] = nuevo_grupo
#
# 		nueva_asignatura = "DDSI"
# 		if nueva_asignatura != None:
# 			horario_modificado["asignatura"] = nueva_asignatura
#
# 		nueva_hora_inicio = None
# 		if nueva_hora_inicio != None:
# 			horario_modificado["hora_inicio"] = nueva_hora_inicio
#
# 		if nueva_hora_fin != None:
# 			horario_modificado["hora_fin"] = nueva_hora_fin
#
# 		if nueva_fecha != None:
# 			horario_modificado["fecha"] = nueva_fecha
#
# 		if nuevo_aula != None:
# 			horario_modificado["aula"] = nuevo_aula
#
# 		if nuevo_profesor != None:
# 			horario_modificado["profesor"] = nuevo_profesor
#
# 		try:
# 			with open('./horario.json', 'w') as modificado:
# 				json.dump(horario_modificado, modificado)
# 				return True
# 		except IOError as fallo:
# 			print("Error %d escribiendo horario.json: %s", fallo.errno, fallo.strerror)
#
#
# 	def BorrarHorario(curso=None, grupo=None, asignatura=None):
# 		try:
# 			with open('./horario.json') as datos:
# 				horario_a_borrar = json.load(datos)
# 		except IOError as fallo:
# 			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)
# 		# Implementado borrar
# 		horario_a_borrar["curso"] = "null"
# 		horario_a_borrar["grupo"] = "null"
# 		horario_a_borrar["asignatura"] = "null"
# 		horario_a_borrar["hora_inicio"] = "null"
# 		horario_a_borrar["hora_fin"] = "null"
# 		horario_a_borrar["fecha"] = "null"
# 		horario_a_borrar["aula"] = "null"
# 		horario_a_borrar["profesor"] = "null"
#
# 		try:
# 			with open('./horario.json', 'w') as borrado:
# 				json.dump(horario_a_borrar, borrado)
# 				return True
# 		except IOError as fallo:
# 			print("Error %d escribiendo horario.json: %s", fallo.errno, fallo.strerror)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import psycopg2
import os

API_TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(API_TOKEN)
database = os.environ["DATABASE"]
user = os.environ["USER"]
password = os.environ["PASSWD"]
host = os.environ["HOST"]
conn = psycopg2.connect(database=database, user=user, password=password, host=host)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola, de momento solo repito')

@bot.message_handler(commands=['horario'])
def send_activity(message):
	cid = message.chat.id
	cur = conn.cursor()
	cur.execute("SELECT * FROM horario")
	row = cur.fetchall()
	conn.close()
	cur.close()
	bot.send_message(cid, str(row))

@bot.message_handler(commands=['viñeda'])
def send_welcome(message):
    bot.reply_to(message, 'Dime illo dime')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
