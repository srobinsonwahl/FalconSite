from flask import Flask, render_template, request, redirect
from main import create_map, get_ip_coords

app = Flask(__name__)

@app.route('/')
def index():
    """
    Returns the home page using render template
    """

    return render_template('/index.html')

@app.route('/not_found')
def not_found():
    """
    Returns the not found page using render template
    """

    return render_template('/not_found.html')

@app.route('/result', methods=['POST'])
def result():
    """
    Takes in data from html form and passes it through to back end, checks if result is error code, if not, returns result page
    """

    data_from_form = request.form['QUERY']
    query = data_from_form
    result = create_map(get_ip_coords(data_from_form))

    if result == 999:
        return redirect('/not_found')
    
    else:
        return render_template('/result.html', query = query)

@app.route('/redirect', methods = ['GET'])
def redirect_home():
    """
    Returns to home page using render template
    """
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)