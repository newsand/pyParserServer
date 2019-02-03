from app import app
#import routes
from app.routes import *

#IMPORM MODELS

from app.models import texts
if __name__ == '__main__':
        app.run(port=8080, debug=True)