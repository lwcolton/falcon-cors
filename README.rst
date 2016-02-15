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


