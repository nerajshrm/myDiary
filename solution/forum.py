#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from forumdb_solved import get_posts, add_post

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>dear, Diary!</title>
    <style>
    .container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
  }

      h1, form { text-align: center; 
                  background : white;
                    }
      h1{
        color: Gray;
      }
      p{
        color: Orange;
      }

      p, ,h3 {
          font-family: Arial, Helvetica, sans-serif;
          text-align : center;
      }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>My Diary</h1>
    <form action="#">

    <label for="fname">haunting past</label>
    <input type="text" id="fname" name="firstname" placeholder="date...">

    </form>

    <h3><em>Today is a great day, </br>
    wanna share your experience to future you
    </em> </h3>
    </br>
    <p><h2> <strong>dear, diary...</strong></h2></p>
    <form method=post class="container">
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''
# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (date, text) for text, date in get_posts())
  html = HTML_WRAP % posts
  return html


@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  message = request.form['content']
  add_post(message)
  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
