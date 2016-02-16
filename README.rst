falcon-cors
========

About
------
This is a CORS algorithm and a falcon middleware for CORS.

Interface Documentation:  https://falcon-cors.readthedocs.org/en/develop/falcon_cors.html

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




