from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
# the toolbar is only enabled in debug mode:
app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret'
toolbar = DebugToolbarExtension(app)


@app.route('/')
def show_templates():
   """Show templates"""
   
   return render_template('select-stories.html', stories=stories.values())

@app.route('/prompt')
def show_prompt():
   """Show prompt to input words"""
   story_id = request.args['story_id']
   story = stories[story_id]

   prompts = story.prompts
   return render_template('prompt.html', story_id=story_id,
                           title=story.title, prompts=prompts)

@app.route('/story')
def show_story():
   """Show story """
   story_id = request.args['story_id']
   story = stories[story_id]

   text = story.generate(request.args)
   return render_template('story.html', title=story.title, text=text)