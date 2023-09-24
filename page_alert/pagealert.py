
import sys
from os import path
# sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from .webapp import create_app


def initialize_webapp_and_backed():
    app = create_app()
    app.run(host="0.0.0.0", port=2139, debug=True)

    # TODO add backed init scripts
