falcon-cors
========

About
------
This is a CORS algorithm and a falcon middleware for CORS

Usage
------
.. code-block:: python

    import falcon
    from falcon_cors import CORS

    cors = CORS(allow_origins_list=['test.com'])

    api = falcon.API(middleware=[cors.middleware])


