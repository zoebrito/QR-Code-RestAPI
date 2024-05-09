# QR Code RestAPI

This project provides a RESTful API for creating, retrieving, and deleting QR codes. It allows users to interact with the API using HTTP requests to perform various operations related to QR codes.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Create a virtual environment:

    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Make sure Docker is started on your system.

6. Run pytest locally to check that everything is working correctly.

7. Start the application using Docker Compose:

    ```
    docker-compose up --build
    ```

## Usage

Once the application is running, you can interact with the API using HTTP requests. The OpenAPI specification documentation is available at [http://localhost/docs](http://localhost/docs). Follow these steps to access the documentation and test the API:

1. Navigate to [http://localhost/docs](http://localhost/docs) in your web browser.
2. Click on the "Authorize" button.
3. Input the following credentials:
    - Username: admin
    - Password: secret
4. Once authenticated, you can test making, retrieving, and deleting QR codes directly from the OpenAPI spec page.

## Description

This project aims to simplify the process of generating QR codes by providing a convenient RESTful API. Users can easily create QR codes with custom data, retrieve QR codes based on specific criteria, and delete QR codes when they are no longer needed. By leveraging Docker for containerization, the application can be deployed seamlessly across different environments. Additionally, the OpenAPI specification documentation offers comprehensive details on the available endpoints and their respective functionalities, making it easier for developers to integrate the API into their applications.
