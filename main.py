from flask import Flask, jsonify, request
import scrape
app = Flask(__name__)


@app.route('/smwhacks', methods=['GET'])
def get_smwhacks():
    moderated = request.args.get('moderated', True)
    pagination = request.args.get('pagination', 0)

    moderated = False if moderated == "0" else True
    if (pagination is not str) or (not pagination.isdigit()):
        pagination = 0
    else:
        pagination = int(pagination)
    return jsonify(scrape.scrape_smw_hacks(moderated, pagination))


if __name__ == "__main__":
    app.run(port=6000, debug=True)
