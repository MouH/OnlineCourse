import webapp2
import cgi

form="""
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form % {"text": text})


    def get(self):
    	# default type is http file
        # self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        self.write_form(rot13(user_text))


application = webapp2.WSGIApplication([('/', MainPage)],
	debug=True)

def escape_html(s):
    # need to import cgi
    # replace_dict = {'>': '&gt;', '<': '&lt;', '"': '&quot;', '&': '&amp;' }
    # return_html = ""
    # for i in range(0, len(s)):
    #     if s[i] in replace_dict:
    #         return_html = return_html + replace_dict.get(s[i])
    #     else:
    #         return_html = return_html + s[i]
    # return return_html
    return cgi.escape(s, quote = True)

def rot13(s):
    lower_chars = ''.join(chr(c) for c in range (97,123)) #ASCII a-z
    upper_chars = ''.join(chr(c) for c in range (65,91)) #ASCII A-Z
    lower_encode = lower_chars[13:] + lower_chars[:13] #shift 13 bytes
    upper_encode = upper_chars[13:] + upper_chars[:13] #shift 13 bytes
    output = "" #outputstring
    for c in s:
        if c in lower_chars:
                output = output + lower_encode[lower_chars.find(c)]
        elif c in upper_chars:
            output = output + upper_encode[upper_chars.find(c)]
        else:
            output = output + c
    return output
