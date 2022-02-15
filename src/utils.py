from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    return """
        <div style="text-align: left;">
        <strong>This is the API home</strong>. Specify a real endpoint path like:
        <ul style="text-align: left;">
            <li><a href='#'><u><i>/members</i></u> with <strong>GET</strong> method for get all members</a></li>
            <li><a href='#'><u><i>/members</i></u> with <strong>POST</strong> method and body data for add a new member</a></li>
            <li><a href='#'><u><i>/members/< int:member_id></i></u> with <strong>GET</strong> method for get a member</a></li>
            <li><a href='#'><u><i>/members/< int:member_id></i></u> with <strong>DELETE</strong> method for delete a member</a></li>
        </ul></div>
        """
