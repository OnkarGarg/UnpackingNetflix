
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["UPLOAD_FOLDER"] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired(),  FileAllowed(['csv'], "not allowed!")])
    submit = SubmitField("Upload File")


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        print(file)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))
        return "File Has Been Uploaded"
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
