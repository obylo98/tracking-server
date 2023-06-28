from flask import Flask, send_file, request
import datetime

app = Flask(__name__)

@app.route('/pixel')
def tracking_pixel():
    # Get tracking data
    device = request.user_agent.string
    open_time = datetime.datetime.now()
    location = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Log the tracking data (you can customize the storage method)
    log_tracking_data(device, open_time, location)

    # Return a 1x1 transparent pixel image
    return send_file('pixel.png', mimetype='image/png')

def log_tracking_data(device, open_time, location):
    # Write the tracking data to a log file or store it in a database
    with open('tracking_log.txt', 'a') as file:
        file.write(f"Device: {device}\n")
        file.write(f"Open Time: {open_time}\n")
        file.write(f"Location: {location}\n")
        file.write('\n')

if __name__ == '__main__':
    app.run()
