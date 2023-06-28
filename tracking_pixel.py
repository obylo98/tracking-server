from flask import Flask, send_file, request, render_template
import datetime

app = Flask(__name__)

log_data = []

@app.route('/pixel')
def tracking_pixel():
    device = request.user_agent.string
    open_time = datetime.datetime.now()
    location = request.headers.get('X-Forwarded-For', request.remote_addr)

    log_entry = {
        'device': device,
        'open_time': open_time,
        'location': location
    }

    log_data.append(log_entry)

    return send_file('pixel.png', mimetype='image/png')

@app.route('/log')
def view_log():
    return render_template('log.html', log_entries=log_data)

if __name__ == '__main__':
    app.run()