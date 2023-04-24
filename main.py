# importing routes
from routes import routes

# serving app
if __name__ == "__main__":
    routes.app.run(port=4000, debug=True)
