from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Assuming your HTML file is named index.html

@app.route('/run_streamlit')
def run_streamlit():
    # Path to your Streamlit app
    streamlit_script = os.path.join(os.getcwd(), 'project_01', 'streamlit_app.py')

    # Run the Streamlit app as a subprocess
    subprocess.Popen(['streamlit', 'run', streamlit_script])

    return redirect(url_for('index'))  # Redirect back to the home page after running the script

if __name__ == '__main__':
    app.run(debug=True)
