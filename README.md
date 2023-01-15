# Coding Jobs 💼
This project was inspired by [Tutorial Series on Youtube](https://youtube.com/playlist?list=PLpyspNLjzwBkV1Lo2CSKLFtzG3PUNTG8q).

- [Coding Jobs 💼](#coding-jobs-)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Running](#running)
- [Trouble Shootings](#trouble-shootings)
- [Contributing](#contributing)
- [License](#license)

# Setup
## Prerequisites
- some knowledge in `Python >= 3.11` and `pip`

> This project is constructed by combining [Vue3](https://vuejs.org/), [Bulma](https://bulma.io/) and [Django](https://www.djangoproject.com/). 

## Running
> Since this project does not use setup script, we must have to do it manually.

1. change one of the released branch and clone the git repository
  ```bash
    git clone https://github.com/kylesinlynn/coding-jobs-django-vue.git
  ```

2. create a virtual environment for python using `venv`
  ```bash
    python -m venv venv
  ```

3. install the required python packages
  ```bash
    pip install -r requirements.txt
  ```

4. run the `Django` test server and the server will be listening at [127.0.0.1:8000](http://127.0.0.1:8000/) by `default`
  ```bash
    python manage.py runserver
  ```

# Trouble Shootings
Create an issue upon your error that is associated with this project.

# Contributing
Feel free to fork and create pull requests. Your contribution will be appreciated.

# License
This project is licensed under [BSD License](LICENSE).