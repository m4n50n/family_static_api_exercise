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
        <strong>This is the API home</strong>. You can run a new request (from <strong>Postman</strong>, for example) specifying a real endpoint path like:
        <ul style="text-align: left;">
            <li><u><i>/members/</i></u> with <strong>GET</strong> method for get all members</li>
            <li><u><i>/member/</i></u> with <strong>POST</strong> method and valid body data for add a new member</li>
            <li><u><i>/member/< int:member_id></i></u> with <strong>GET</strong> method for get a member</li>
            <li><u><i>/member/< int:member_id></i></u> with <strong>DELETE</strong> method for delete a member</li>
        </ul></div>
        """
