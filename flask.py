app = Flask(__name__)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.route('/')
def home():
    return 'Dit is een test'

if __name__ == '__main__':
    ip_address = get_ip()
    print(f"Flask is running on {ip_address}:5000")
    app.run(host=ip_address, port=5000) 
