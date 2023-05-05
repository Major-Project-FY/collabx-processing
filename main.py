# importing routes
from routes import routes

# module imports
from dotenv import load_dotenv
import os

load_dotenv()
port = os.getenv('PORT')

# serving app
if __name__ == "__main__":
    routes.app.run(port=port, debug=True)
