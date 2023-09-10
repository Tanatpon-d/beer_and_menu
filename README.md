# Python Developer Test

A brief description of your project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Django Setup](#django-setup)
  - [Docker Compose Setup](#docker-compose-setup)
- [Accessing the API](#accessing-the-api) & [Swagger Documentation](#swagger-documentation)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version 3.9.13)
- Docker
- Docker Compose

## Getting Started

# Docker Compose Setup

1. Build and start the Docker containers:

   ```bash
   docker-compose up -d


### Django Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Django and other project dependencies:

   ```bash
   pip install -r requirements.txt
   
4. Apply database migrations:

   ```bash
   python manage.py migrate
   
5. Start the Django development server:

   ```bash
   python manage.py runserver
   
## Accessing the API &  Swagger Documentation

You can access the API at the following endpoint:

- **API Endpoint**: [http://localhost:5000/api](http://localhost:5000/api)

Please ensure that the Docker Compose containers are running before attempting to access the API.


Swagger documentation is available to explore and interact with the API endpoints. Here's how to access it:

1. Open a web browser.

2. Visit the Swagger documentation URL:

   - **Swagger URL**: [http://localhost:5000/api](http://localhost:5000/api)

3. You will be greeted with the interactive Swagger UI, allowing you to browse, inspect, and test the API endpoints effortlessly.

Feel free to explore and interact with the API using the Swagger documentation for a better understanding of the available endpoints and their functionality.


