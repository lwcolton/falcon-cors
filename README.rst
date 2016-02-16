falcon-cors
========

About
------
This is a CORS algorithm and a falcon middleware for CORS.

Interface Documentation:  https://falcon-cors.readthedocs.org/en/master/falcon_cors.html

pypi: https://pypi.python.org/pypi/falcon-cors

Install
-------

.. code-block:: shell

    pip install falcon-cors

Usage
------
.. code-block:: python

    import falcon
    from falcon_cors import CORS

    cors = CORS(allow_origins_list=['test.com'])

    api = falcon.API(middleware=[cors.middleware])


Override CORS for a specific resource
--------
.. code-block:: python

    import falcon
    from falcon_cors import CORS

    cors = CORS(allow_origins_list=['test.com'])

    api = falcon.API(middleware=[cors.middleware])

    public_cors = CORS(allow_all_origins=True)

    class MyPublicResource:
        cors = public_cors

        def post(self, req, resp):
            resp.body = "Everone can post to this resource"

    api.add_route("/public", MyPublicResource())

Turn CORS off for a specific resource
--------
.. code-block:: python

    class MyResource:
        cors_enabled = False


Tests and Contributing
-------
You can run tests using tox.  
If you want to contribute just submit a PR and please make sure you have created some tests for your feature.
I will review features and run the tests with tox before releasing them.
