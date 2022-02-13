from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
  def __init__(self,data):
    self.id = data['id']
    self.name = data['name']
    self.location = data['location']
    self.language = data['language']
    self.comments = data['comment']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def save(cls,data):
    query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comments)s);"
    return connectToMySQL('dojo_survey_schema').query_db(query,data)

  @classmethod
  def get_one(cls):
    query = "SELECT * FROM dojos ORDER BY CREATED_AT DESC LIMIT 1"
    result = connectToMySQL('dojo_survey_schema').query_db(query) # [{name: "blah"}]
    return cls(result[0])

  @staticmethod # the static method is not like a classmethod. classmethods perform the connection between routes as well.
  def validate_survey(survey):
    is_valid = True
    if len(survey['name']) < 3:
      flash('Name must be longer than 3 characters') # the flash method returns whatever we want to send to our user.
      is_valid = False
    if len(survey['location']) < 1:
      flash('Must choose a location')
      is_valid = False
    if len(survey['language']) < 1:
      flash('Must choose a language')
      is_valid = False
    if len(survey['comments']) < 10:
      flash('Must have a longer comment')
      is_valid = False
    return is_valid
