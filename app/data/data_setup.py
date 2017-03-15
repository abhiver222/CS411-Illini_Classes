from flask import Flask, render_template, request, url_for, redirect
import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
from query import Query

'''
api_response is the raw data in XML format
api_json is JSON version of api_response
'''

'''
Get the list of all departments
Input: Lastest semester API URL
Ouput: List of all departments in JSON format with each
department code (e.g. CS), API URL to its courses, and its name.
'''
def get_all_departments():
	api_response = requests.get('http://courses.illinois.edu/cisapp/explorer/catalog/2017/spring.xml')
	api_json = bf.data(fromstring(api_response.text))
	departments_arr = api_json['{http://rest.cis.illinois.edu}term']['subjects']['subject']
	return departments_arr

'''
Get the list of all courses from a department
Input: Department API URL
Output: List of all courses in this department in JSON format
XML example: http://courses.illinois.edu/cisapp/explorer/catalog/2017/spring/AFRO.xml
'''
def get_all_courses(department_url):
	api_response = requests.get(department_url)
	api_json = bf.data(fromstring(api_response.text))
	courses_arr = api_json['{http://rest.cis.illinois.edu}subject']['courses']['course']
	return courses_arr

'''
Get a specific course
Input: Course API URL
Ouput: A course in JSON format that contains course number, course name, and course description
XML example: http://courses.illinois.edu/cisapp/explorer/catalog/2017/spring/AFRO/100.xml
'''
def get_a_course(course_url):
	api_response = requests.get(course_url)
	api_json = bf.data(fromstring(api_response.text))
	course = api_json['{http://rest.cis.illinois.edu}course']
	return course

'''
Insert all departments' name to the database
'''
def insert_departments(query):
	depts = get_all_departments()
	for dept in depts:
		print dept['$'] 	# For testing purposes
		query.insert_departments(dept['$'])

'''
Insert all courses' info to the database
'''
def insert_courses(query):
	depts = get_all_departments()
	# print depts
	for dept in depts:
		dept_id = dept['@id']			# e.g. CS
		dept_url = dept['@href']		# API URL for a particular dept.

		# print dept_id

		# Departments with little information will be passed
		if (dept_id == 'BIOL' or dept_id == 'ENT'
			or dept_id == 'PBIO' or dept_id == 'WGGP'):
			continue

		courses = get_all_courses(dept_url)
		for course in courses:
			course_url = course['@href']						# Get course API URL
			course = get_a_course(course_url)					# Get a course in JSON format

			course_id = course['@id']							# Get course id, e.g. CS 411
			course_name = course['label']['$']					# Get course name, e.g. Databases

			if 'description' not in course:						# Some of the courses don't have descriptions
				continue
			course_description = course['description']['$']

			# Insert the current course to the database
			crn = ""
			query.insert_courses(crn, course_description, course_id + " " + course_name, " ", 0, 0, 0, 0)

			# For testing purposes
			# print course_id
			# print course_name
			# print course_description

'''
Setup departments and courses info
'''
def main():
	query = Query()
	#insert_departments(query)     # Departments are already in the db, right?
	insert_courses(query)

if __name__ == "__main__":
    # execute only if run as a script
    main()
