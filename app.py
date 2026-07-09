from flask import Flask, render_template
from models.prediction import predict_congestion
from models.optimization import optimize_signal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    congestion = predict_congestion()
    optimization = optimize_signal(congestion)

    return render_template(
        'dashboard.html',
        congestion=congestion,
        optimization=optimization
    )

if __name__ == '__main__':
    app.run(debug=True)
