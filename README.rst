.. code-block:: python

    import falcon
    from falcon_cors import CORS

    cors = CORS()

    api = falcon.API(middleware=[cors.middleware])


