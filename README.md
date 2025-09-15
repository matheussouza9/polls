# Polls Application

A full-stack polling application built with Django (backend) and Vue.js (frontend), containerized with Docker.

## Prerequisites

- Docker (with Docker Compose) or Podman (with Podman Compose)

## Getting Started

### 1. Start the Application

Start all services using Docker Compose:

```bash
docker-compose up -d
```

Or if you're using Podman:

```bash
podman-compose up -d
```

This will start the following services:
- Backend (Django) - http://localhost:8000
- Frontend (Vue.js) - http://localhost:8080
- Database (Postgres)
- Redis
- Celery
- Celery Beat (Periodic tasks manager)

### 3. Create a Superuser

To create an admin user, run:

```bash
docker exec backend python manage.py createsuperuser
```

Or with Podman:

```bash
podman exec -it polls_backend_1 python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 4. Access the Admin Interface

Once the application is running, you can access the admin interface at:
http://localhost:8000/admin/


### 5 Setup Periodic Tasks
1. To setup periodic tasks, go to http://localhost:8000/admin/django_celery_beat/periodictask/ page
2. Push the "Add Periodic Task +" button on top right corner
3. Give it a name and select one of the registered tasks available
4. Set the schedule to run as you like
5. Save
