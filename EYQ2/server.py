import os, workwithxl
from flask import Flask, render_template, request, redirect, url_for

ALLOWED_EXTENSIONS = {'xls', 'xlsx'} # Data types of required files
UPLOAD_FOLDER = 'uploads' # Folder on the server for receiving files
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Checking the data types of uploaded files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('index.html')

# Uploading files from our computer to the server
@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        file = request.files.getlist('file[]')
        for f in file:
            if f and allowed_file(f.filename):
                filename = f.filename
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_list = os.listdir(UPLOAD_FOLDER)
        wwxl = workwithxl.WorkwithXL()
        wwxl.download_XL_in_DB(file_list)
        for filename in file_list:
            # After uploading to the database, we clear the folder on the
            # server
            os.remove(UPLOAD_FOLDER + "/" + filename)
    return render_template('index.html')

@app.route('/browse', methods=["POST", "GET"])
def browse():
    wwxl = workwithxl.WorkwithXL()
    downloaded_files = wwxl.list_of_downloaded_files()
    # Html-script for viewing uploaded files
    html = """
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8" />
  <title>Загруженные файлы</title>
 </head>
 <body>
 
 <form action="/download" method="POST">
 <ul>"""
    partStart = """<li>
  <p><input type="submit" name="report" value="
  """
    partEnd = """">
</li>
     """
    for file in downloaded_files:
        html += partStart + file + partEnd
    html += """</ul>
</form>
		
 <form action="/start">
			<p><input type="submit" value="Назад">
		</form>
 </body>
</html>"""
    return html

# Decoding the names of classes from the report and lines with the total
# balance of these classes. Creating a table
def row_table(row):
    wwxl = workwithxl.WorkwithXL()
    key = int(row[0])
    if key >= 0 and key <= 9:
        if key == 0:
            row[0] = "БАЛАНС"
        else:
            row[0] = "ПО КЛАССУ"

    html_row = "<tr><td>"
    for cell in row:
        html_row += cell + "</td><td>"
    html_row = html_row[:-4]
    html_row += "</tr>"
    
    if key >= 1 and key <= 8:
        html_row += """
        <tr><td colspan="7" align="center">""" + wwxl.classes.get(str(key + 1)) + "</td></tr>"
           
    return html_row

# Loading data from the server to a table
@app.route('/download', methods=["POST", "GET"])
def download():
    report = ""
    if request.method == 'POST':
        if request.form['report'] != "Загруженных файлов нет":
            report = request.form['report']
            report = report[55:]
            wwxl = workwithxl.WorkwithXL()
            file = wwxl.download_the_report(report)
            report = request.form['report']
    html = """
    <!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8">
  <title>
  """ + report + """
  </title>
 </head>
 <body>
  <table border="1">
   <caption>""" + report + """
   </caption>
   <tr>
   <th>Б/сч</th>
    <th>ВХОДЯЩЕЕ САЛЬДО Актив</th>
    <th>ВХОДЯЩЕЕ САЛЬДО Пассив</th>
    <th>ОБОРОТЫ	Дебет</th>
    <th>ОБОРОТЫ	Кредит</th>
    <th>ИСХОДЯЩЕЕ САЛЬДО Актив</th>
    <th>ИСХОДЯЩЕЕ САЛЬДО Пассив</th>
   </tr>"""
    html += """
   <tr><td colspan="7" align="center">""" + wwxl.classes.get('1') + "</td></tr>"
    for row in file:
        html += row_table(row)
    html += """</table>
  
   <form action="/browse">
			<p><input type="submit" value="Назад">
		</form>
    
 </body>
</html>"""
    return html

if __name__ == '__main__':
  app.run(debug=False)