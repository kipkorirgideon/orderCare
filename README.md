# Order Management System

### How to prepare your machine?

- install `Python`, `Postgres`, `Redis`

- install [Pipenv](https://pipenv.pypa.io/en/latest/)

- create a new Postgres database (example: `order_care`) 

- copy `.template_env` into `.env`
- add your database credentials to `.env` file
- Activate the virtual environment by running `pipenv shell`
- run `pipenv install`

### How to run?

- run `python manage.py migrate`

- run `python manage.py runserver 8000`

### Create OAuth2 Client
- Go to `http://localhost:8000/admin/`
- Login with your superuser credentials
- Go to `Applications` and click `Add Application`
- Add `Name`, `Client Type` and `Authorization Grant Type`
- Grab `Client ID` and `Client Secret` and add them to `.env` file
- Add `http://localhost:8000/api/auth-login/` to `Allowed Callback URLs` in your OAuth2 Client

### How to test?
- To register a new user, send a `POST` request to `http://localhost:8000/ api/auth-register/` with `username`, `password` and `email` in the body
- To login, send a `POST` request to `http://localhost:8000/api/auth-login/` with `username` and `password` in the body
- Once Authenticated, by internal OAuth2 server, you will get an `access_token` and `refresh_token` in the response
- To access protected resources, make sure to add `Authorization` header with `Bearer <access_token>` in the request


### Available API Endpoints
- `{protocol}://{host_domain}/api/auth-register/` - `POST` - Register a new user
- `{protocol}://{host_domain}/api/auth-login/` - `POST` - Login a user
- `{protocol}://{host_domain}/api/orders/` - `GET` - List all orders
- `{protocol}://{host_domain}/api/orders/` - `POST` - Create a new order
- `{protocol}://{host_domain}/api/orders/<order_id>/` - `GET` - Get an order
- `{protocol}://{host_domain}/api/orders/<order_id>/` - `PUT` - Update an order
- `{protocol}://{host_domain}/api/orders/<order_id>/` - `DELETE` - Delete an order
- `{protocol}://{host_domain}/api/orders/customers/` - `GET` - List all customers
- `{protocol}://{host_domain}/api/orders/customers/` - `POST` - Create a new customer
- `{protocol}://{host_domain}/api/orders/customers/<customer_id>/` - `GET` - Get a customer
- `{protocol}://{host_domain}/api/orders/customers/<customer_id>/` - `PUT` - Update a customer
- `{protocol}://{host_domain}/api/orders/customers/<customer_id>/` - `DELETE` - Delete a customer
- `{protocol}://{host_domain}/api/orders/items/` - `GET` - List all items
- `{protocol}://{host_domain}/api/orders/items/` - `POST` - Create a new item
- `{protocol}://{host_domain}/api/orders/items/<item_id>/` - `GET` - Get an item
- `{protocol}://{host_domain}/api/orders/items/<item_id>/` - `PUT` - Update an item
- `{protocol}://{host_domain}/api/orders/items/<item_id>/` - `DELETE` - Delete an item

### Hosting on Heroku
- App is hosted on Heroku at `https://ordercare-3759a549b02f.herokuapp.com/`
- Enabled Continuous Deployment for any push to `main`

### Accessing Admin Panel
- Go to `https://ordercare-3759a549b02f.herokuapp.com/admin/`
- Use `admin` as username and `admin` as password to login

