# Todo-Application 📝

Welcome to Todo-Application, a robust Django project designed for efficient task management.

## Features 🚀

- **Task Operations**: Seamlessly manage tasks through intuitive creation, updating, and deletion functionalities.
  
- **Authentication and Authorization**: Ensure task security with Django's powerful authentication and authorization system. Users can exclusively administer their tasks upon proper authorization.

## Getting Started 🛠️

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/adityaShar24/Django-todo.git

2. **Change the Directory**
   ```shell
    cd Todo-Application

3. **Install Dependencies:** 
    ```shell
    pip install -r requirements.txt
 

4. **Apply Migrations:** 
    ```shell
    python manage.py migrate


5. **Create Superuser:** 
    ```shell
    python manage.py createsuperuser    

6. **Run Development Server:** 
    ```shell
    python manage.py runserver    

## Usage 📌

- **Access the Application:**
  Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

- **Login:**
  Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and login with the superuser credentials.

- **Create Tasks:**
  Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and create a task.

- **Delete Task:**
  Visit [http://127.0.0.1:8000/delete_task](http://127.0.0.1:8000/delete_task) and delete a task.

- **Update Task:**
  Visit [http://127.0.0.1:8000/update_task/](http://127.0.0.1:8000/admin/) and update a task.

- **Note:**
  All steps informed here require login. These routes are protected with the `@login_required` decorator, and if not authenticated, you will be redirected to the login page ([http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)).


## Contributing 🤝

Feel free to contribute to enhance the functionality of Todo-Application. Follow the [contribution guidelines](CONTRIBUTING.md) for more details.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/adityaShar24/Django-todo/blob/main/LICENSE) file for details.

## Acknowledgments 🙏

Special thanks to the Django community and contributors for making this project possible.

Happy task managing! 😊






