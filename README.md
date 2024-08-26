# 📌 Django REST Framework

1. Clone this project into your preferred directory:

```sh
git clone git@github.com:git-camilabatista/django_tcc.git
```

2. Navigate to the `django_tcc` directory that was created:

```sh
cd django_tcc
```

4. Run the command to install all the necessary dependencies:

> [!IMPORTANT]
> To proceed with this step, it is necessary to have [Poetry](https://python-poetry.org/) already installed.

```sh
poetry install
```

4. Navigate to the `./django_tcc/setup/` directory:

```sh
cd django_tcc/setup/
```

5. Run the command to start the application:

```sh
make django
```

#### 🚩 With the application running, you can perform the Load Test and the CPU and Memory Test.

- To execute the Load Test, please visit: [Load Test with Locust](https://github.com/git-camilabatista/teste_carga_tcc)

- To execute the CPU and Memory Test, please visit: [CPU and Memory Test with Sysstat](https://github.com/git-camilabatista/monit_cpu_mem_tcc)
