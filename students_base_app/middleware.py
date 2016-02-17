import re
from time import time
from django.db import connection


class StatMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Get db queries before view work
        db_queries = len(connection.queries)

        # Get view func work time
        start_view = time()
        response = view_func(request, *view_args, **view_kwargs)
        total_time = time() - start_view

        if hasattr(response, 'render'):
            response.render()

        # Get db queries after view func finish works
        db_queries = len(connection.queries) - db_queries

        if 'text/html' in response.get('content-type', ''):
            stat_info = '<!--\n Page generation time: {:.2F}s \n Queries count: {} \n--></body></html>'.format(
                total_time,
                db_queries)

            response.content = re.sub(r'[\s.]+(</body>)[\s.]+', stat_info, response.content)

        return response
