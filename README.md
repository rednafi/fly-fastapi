<div align="center">

<h1>Fly FastAPI</h1>
<strong>>> <i>Deploying a simple FastAPI app to Fly.io</i> <<</strong>

&nbsp;

</div>

## Test the deployed app



## Test locally

Make sure you have the lastest version of [Docker](https://www.docker.com/) and `docker-compose` (v2) installed.

* Clone the repo.
* Head over to the root directory.
* Run:
    ```
    docker compose up
    ```
* Go to [http://localhost:5000/docs](http://localhost:5000/docs).


## Run the unit tests

* Create and activate a virtual environment.
* Install the dependencies, run:

    ```
    pip install -r requirements.txt -r requirements-dev.txt
    ```
* Run the tests:

    ```
    pytest -s -v
    ```

    This will return:

    ```
    tests/test_main.py::test_auth_error PASSED
    tests/test_main.py::test_ok PASSED

    ============================ 2 passed in 0.16s =============================
    ```



<div align="center">
<i> ✨ 🍰 ✨ </i>
</div>
