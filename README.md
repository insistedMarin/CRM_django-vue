# CRM System

The CRM system is a comprehensive customer relationship management system designed to manage customers, sales opportunities, tasks, and generate reports. The system is developed using Vue.js for the frontend, Django for the backend, PostgreSQL as the database, and Jenkins for CI/CD automation.

## Technology Stack

- Frontend: Vue.js
- Backend: Django
- Database: PostgreSQL
- CI/CD: Jenkins

## Project Structure

The project consists of two main components: the frontend and the backend.

### Frontend

The frontend is a Vue.js application responsible for providing the user interface and interactions. To run the frontend, make sure to follow these steps:

1. Install Node.js and npm.
2. Navigate to the `crm_frontend` directory.
3. Run `npm install` to install all frontend dependencies.
4. Execute `npm run serve` to start the frontend development server.

### Backend

The backend is developed using the Django framework and handles business logic, database interactions, and API endpoints. To run the backend, follow these steps:

1. Navigate to the `crm_backend` directory.
2. Install Python and a virtual environment if not already installed.
3. Create and activate a virtual environment.
4. Run `pip install -r requirements.txt` to install backend dependencies.
5. Run `python manage.py migrate` to apply database migrations.
6. Execute `python manage.py runserver` to start the backend server.

## Database

The project uses PostgreSQL as the database management system. In the CI/CD pipeline, we use Jenkins to automate database deployment. The following tasks are configured in Jenkins:

1. Start the PostgreSQL container.
2. Wait for the PostgreSQL container to start and be ready to accept connections.

## CI/CD

We use Jenkins for continuous integration and continuous delivery. The pipeline configuration can be found in the `Jenkinsfile` and includes the following stages:

1. Start the PostgreSQL container.
2. Test the backend.
3. Build a Docker image for the Django application.
4. Run the Docker container for the Django application.
5. Apply database migrations.

To enhance our CI/CD process, we have added a Docker run command to launch the Jenkins container with additional configurations. This command is as follows:

```shell
docker run --rm -u root -p 8081:8080 -v jenkins-data:/var/jenkins_home -v //var/run/docker.sock:/var/run/docker.sock myjenkins:2.41
```
> **Note:** Here, `myjenkins:2.41` is an updated version of Jenkins based on `jenkinsci/blueocean`.

Please note that this is a sample pipeline configuration and can be further customized based on project requirements. Additionally, ensure that Jenkins security is configured, and sensitive information is stored as Jenkins credentials.

---

This README provides an overview of the project, the technology stack, installation guide, an overview of the CI/CD pipeline, and how to contribute. You can further expand and customize it based on the actual project's needs.

