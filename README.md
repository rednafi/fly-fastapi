<div align="center">

<h1>Fly FastAPI</h1>
<strong>>> <i>Deploying a simple FastAPI app to Fly.io</i> <<</strong>

&nbsp;

</div>

[Fly.io](https://fly.io/) is a neat way to quickly deploy your application. I wanted to
take it for a spin and deploy a small Python app for starters. By default, it supports
deploying apps built with frameworks like Express, Nuxt, Django, Rails, etc. However, I
wanted to see if I can make it work with a small app built with FastAPI.

Turns out, if you can Dockerize your app, you can deploy it with Fly.io regardless of
the stack. Also, the deployment is completely automatic here; it's done by GitHub Action
and the deployment only kicks in if the corresponding commit has a tag that starts
with `v*`.

## Checkout the deployed app

* To access the deployed OpenAPI docs provided by FastAPI, go to
[https://fly-fastapi.fly.dev/docs](https://fly-fastapi.fly.dev/docs).
* Use the doc to make requests to the `GET /greetings` API endpoint. This endpoint
leverages HTTP basic auth. The username is `ubuntu` and password is `debian`.
* Or, you can use cURL to test the endpoint:

    ```bash
    curl -X GET https://fly-fastapi.fly.dev/greetings -u ubuntu:debian
    ```

    This will return:

    ```json
    {
      "ok": true,
      "message": "Hello from Fly!"
    }
    ```
If you can't access the app, that probably means, I tore down the container to save
money; you can still test it out locally.

## Run the app locally

Make sure you have the lastest version of [Docker](https://www.docker.com/) and `docker-compose` (v2) installed.

* Clone the repo.
* Head over to the root directory.
* Run:
    ```bash
    docker compose up
    ```
* Go to [http://localhost:5000/docs](http://localhost:5000/docs) in your browser.


## Run the unit tests

* Create and activate a virtual environment.
* Install the dependencies, run:

    ```bash
    pip install -r requirements.txt -r requirements-dev.txt
    ```
* Run the tests:

    ```bash
    pytest -s -v
    ```

    This will return:
    ```
    tests/test_main.py::test_auth_error PASSED
    tests/test_main.py::test_ok PASSED

    ============================ 2 passed in 0.16s =============================
    ```

## Todo

* Add cloudflare caching and DDOS protection.
* ~~Deploy via GitHub action. Currently, this is deployed via `flyctl`.~~

## Resources

* [Deploy a Python application via Fly](https://fly.io/docs/getting-started/python/)
* [Automate the deployment with GitHub Action](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/)


<div align="center">
<i> ✨ 🍰 ✨ </i>
</div>
