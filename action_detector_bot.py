import os	
import time
import subprocess

def read_character(char_input):
	print("User pressed",char_input)
	return char_input

def get_application(application):
	print("User opened",application)
	return application

def write_info():
	file=open("log_file.txt",'w')
	file.write("all the logs should be here")
	file.close()
	

