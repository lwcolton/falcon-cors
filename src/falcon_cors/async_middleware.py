from .middleware import CORSMiddleware


class AsyncCORSMiddleware(CORSMiddleware):
    async def process_resource_async(self, req, resp, resource, *args):
        if not getattr(resource, 'cors_enabled', self.default_enabled):
            return
        cors = getattr(resource, 'cors', self.cors)
        cors.process(req, resp, resource)
