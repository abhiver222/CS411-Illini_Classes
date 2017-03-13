from flask import Flask, render_template, request, url_for, redirect
import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps

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
For testing locally
'''
def main():
    # Print all departments
    depts = get_all_departments()
    for dept in depts:
        print dept['$']

if __name__ == "__main__":
    # execute only if run as a script
    main()