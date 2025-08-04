
from app import create_app

app = create_app()

if __name__ == "__main__": # Only run the next block if this file is being run directly, not imported.
    app.run(debug=True)