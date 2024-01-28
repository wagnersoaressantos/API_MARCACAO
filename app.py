from flask import Flask

from modules.demanda.controller import demanda_controller
from modules.paciente.controller import paciente_controller
from modules.sus.controller import sus_controller
from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(demanda_controller)
app.register_blueprint(paciente_controller)
app.register_blueprint(sus_controller)
Connect().create_tables()
app.run(debug=True)