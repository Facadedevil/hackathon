# AI call Summarizer

## Description
This project was developed in Python and is intended to be used in a hackathon event. It showcases various features and functionalities to solve specific challenges during the hackathon.

## Features
- **Virtual Environment Setup**:
    - The project uses a Python virtual environment to manage dependencies.
    - Commands to create and activate the virtual environment are provided.
- **Dependency Installation**:
    - Dependencies are installed using `pip`.
    - Specific dependencies include `ffmpeg` and others listed in `requirements.txt`.
- **Database Migrations**:
    - The project includes Django database migrations.
    - Commands to create and apply migrations are provided.
- **Server Setup**:
    - The project includes a Django server setup.
    - Instructions to create a media directory and run the server are provided.
- **API Endpoint for Audio Summary**:
    - An API endpoint is available for generating summaries from audio files.
    - Example command using `curl` is provided to post audio files to the endpoint.

## Installation
To set up and run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Facadedevil/hackathon.git
    ```
2. Navigate to the project directory:
    ```sh
    cd hackathon
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install ffmpeg
    pip install -r requirements.txt
    ```

## Usage
Provide instructions on how to use the project. Include examples and screenshots if necessary.

```sh
# Example command to run the project
python manage.py makemigrations
python manage.py migrate
mkdir media
python manage.py runserver
curl -X POST -F "audio=@path_to_audio_file" http://127.0.0.1:8000/api/generate-summary/
```

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/YourFeatureName
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/YourFeatureName
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

