import os
from flask import send_from_directory
from app import create_app


app = create_app()


@app.route('/images/<path:filename>')
def serve_image(filename):
    """Сервировка изображений из папки images."""
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))
    return send_from_directory(images_dir, filename)


if __name__ == '__main__':
    app.run(debug=True)
