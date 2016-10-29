from flask import Flask
from jinja2 import Environment, PackageLoader
from all_in_one import model

app = Flask(__name__)
env = Environment(autoescape=True, loader=PackageLoader('all_in_one', 'webapp/templates'))


def datetimeformat(value, format='%Y/%m/%d %H:%M:%S'):
    return value.strftime(format)

env.filters['datetimeformat'] = datetimeformat


@app.route('/', methods=['GET'])
def show_news():
    news = model.News.objects.order_by('-date')

    template = env.get_template('news.html')
    return template.render(news=news)


# This is for debugger
def port_check(hostname, port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((hostname, port))
    except socket.gaierror:
        sock.close()
        return False
    sock.close()
    return result == 0


if __name__ == '__main__':
    # This is for debugger
    debug_port = 5678
    if port_check('debug_host', debug_port):
        import pydevd
        pydevd.settrace('debug_host', port=debug_port, stdoutToServer=True, stderrToServer=True)

    app.run(host='0.0.0.0')
