from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)

class Humidity:
  def __init__(self, date, value):
    self.date = date
    self.value = value

class Rainfall:
    def __init__(self, date, value):
        self.date = date
        self.value = value

class Fertilizer:
    def __init__(self, date, type, kilo):
        self.date = date
        self.type = type
        self.kilo = kilo

class Human:
    def __init__(self,Idate, eid, did,gen, age, ex,plk):
        self.Idate= Idate
        self.eid=eid
        self.did=did
        self.gen=gen
        self.age=age
        self.ex=ex
        self.plk=plk

Humiditys = [Humidity('2018-06-10', 83), Humidity('2018-06-11', 97.3), Humidity('2018-06-12', 76), Humidity('2018-06-13', 73.56), Humidity('2018-06-14', 82),Humidity('2018-06-15', 67)
             ,Humidity('2018-06-16', 90),Humidity('2018-06-17', 78.3),Humidity('2018-06-18', 74)]


Rainfalls = [Rainfall('2018-06-10', 23.5 ), Rainfall('2018-06-11', 98.5), Rainfall('2018-06-12', 62.1), Rainfall('2018-06-13', 53), Rainfall('2018-06-14', 87.4),Rainfall('2018-06-15', 26.0)
             ,Rainfall('2018-06-16', 90.45),Rainfall('2018-06-17', 87.12),Rainfall('2018-06-18', 45.5)]

Fertilizers = [Fertilizer('2018-06-10', 'nitrogen' ,20 ), Fertilizer('2018-06-11', 'lankem_20' ,30 ), Fertilizer('2018-06-12', 'cic_f5' ,50 ), Fertilizer('2018-06-13', 'nitrogen' ,20 )]





dataset = [Human('2018-06-07','00001','Upper','Male','35',5,20),
           Human('2018-06-07', '00002', 'Upper','Male', '40', 15, 22),
           Human('2018-06-08', '00004', 'Moddle','Female','55', 5, 14),
           Human('2018-06-07', '00023', 'Upper', 'Female','35', 42, 20),
           Human('2018-06-09', '00056', 'East','Female', '46', 20, 25),
           Human('2018-06-07', '02345', 'Upper', 'Male','35', 5, 20),
           Human('2018-06-10','02522', 'Upper', 'Male', '36', 10, 50),
           Human('2018-06-07', '02745', 'Upper', 'Male', '35', 5, 20),
           Human('2018-06-12', '02523', 'Upper', 'Male', '36', 10, 50),
           Human('2018-06-07', '01545', 'Middle', 'Male','40', 5, 20),
           Human('2018-06-10','02522', 'West', 'Male', '86', 20, 50)]



@app.route('/')
def root():
    return render_template('signin.html')

@app.route('/handle_signin', methods=['POST'])
def handle_signin():
    return render_template('estate_select.html')

@app.route('/handle_signout')
def handle_signout():
    return render_template('signin.html')

@app.route('/handle_estate_select')
def handle_estate_select():
    return render_template('dashboard.html')

@app.route('/switch_estate')
def switch_estate():
    return render_template('estate_select.html')


@app.route('/handle_reports')
def handle_reports():
    return render_template('reports.html')

@app.route('/handle_humidity', methods=['GET', 'POST'])
def handle_humidity():
    if request.method == "POST":
        humi = Humidity(request.form.get('date'), request.form.get('value'))
        Humiditys.append(humi)
    return render_template('humidity.html', Humiditys = Humiditys)

@app.route('/handle_rainfall', methods=['GET', 'POST'])
def handle_rainfall():
    if request.method == "POST":
        rain = Rainfall(request.form.get('date'), request.form.get('value'))
        Rainfalls.append(rain)
    return render_template('rainfall.html', Rainfalls = Rainfalls)


@app.route('/handle_fertilizer', methods=['GET', 'POST'])
def handle_fertilizer():
    if request.method == "POST":
        ferti = Fertilizer(request.form.get('date'), request.form.get('type'), request.form.get('kilo'))
        Fertilizers.append(ferti)
    return render_template('fertilizer.html', Fertilizers=Fertilizers)


@app.route('/humidity_data')
def humidity_data():
    results = []
    labels = []
    for humi in Humiditys:
        results.append(humi.value)
        labels.append(humi.date)
    return jsonify({'results':results, 'labels':labels})

@app.route('/rainfall_data')
def rainfall_data():
    results = []
    labels = []
    for rain in Rainfalls:
        results.append(rain.value)
        labels.append(rain.date)
    return jsonify({'results':results, 'labels':labels})


@app.route('/handle_human')
def handle_human():
    return render_template('human_contribution.html', dataset=dataset)

if __name__ == '__main__':
    app.run()
