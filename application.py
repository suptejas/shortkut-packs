from flask import Flask, Response
import json

application = Flask(__name__)


@application.route('/api/v1/<name>')
def shortkut_pack(name: str):
    data = ''

    with open(fr'shortkuts/{name}.json') as f:
        data = f.read()

    data = json.loads(data)

    return Response(json.dumps(data), mimetype='text/json')


if __name__ == '__main__':
    application.run(debug=True)
