import webapp2
import cgi

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
          "month": escape_html(month),
          "day": escape_html(day),
          "year": escape_html(year)})

    def get(self):
    	# default type is http file
        # self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (year and day and month):
            self.write_form("It's not valid input, friend",
              user_month,user_day,user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Thanks!")

application = webapp2.WSGIApplication([('/', MainPage),
  ('/thanks', ThanksHandler)],
	debug=True)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    month = month.lower().capitalize()
    if month in months:
        return month
    else:
        return None

def valid_day(day):
    if day and day.isdigit():
        alt = int(day)
        if alt > 0 and alt < 32:
            return alt

def valid_year(year):
    if year and year.isdigit():
        a = int(year)
        if a<2020 and a > 1900:
            return a

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