This repository is for the National AIDS Council Management Information System.

The application is written in mostly Python/Django with the Postgres database being used.
Visualizations are implemented using Apache Superset.
The stack includes:

- Django application
- Postgres Database
- Superset 
- Redis

The application can rapidly be deployed using Kubernetes with the included manifest files which are
available under the infrastructure/ directory.

Deploy with "kubectl apply -f infrastructure/overlays/prod"
