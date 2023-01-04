#! /var/mail/flask
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

# this wraps our app in an api and this initializes a restful api
app = Flask(__name__)
api = Api(app)

# make a new request parser object
## will automatically parse through requests that are being sent to make sure it fits the guidelines we choose
video_put_args = reqparse.RequestParser()
# 
video_put_args.add_argument("name", type=str, help="name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="views of the video is required", required = True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required = True)
videos = {}

def ab_if_vid_not(video_id):
    if video_id not in videos:
        abort(404, message = "Video id is not valid...")

def ab_if_vid_in(video_id):
    if video_id in videos:
        abort(409, message = "Video already in catalog...")
# make a resource in this api, 
# when a get request is sent via .add_resource information will be sent based on the video_id I have asked for
class Video(Resource):
    def get(self, video_id):
        ab_if_vid_not(video_id)
        return videos[video_id]

    def put(self, video_id):
        ab_if_vid_in(video_id)
        args = video_put_args.parse_args()
        videos[video_id]= args
        return videos[video_id], 201

    def delete(self, video_id):
        ab_if_vid_not(video_id)
        del videos[video_id]
        return '', 204


# now need to register this as a resource api.add_resource(Class, url) (can use a / to use a default url)
# essentially, it determines what the root of the resource will be
api.add_resource(Video, "/video/<int:video_id>")

# this starts both the server and the application
# debug=True says that we are in debug mode so we will see all of that output and any logging information, so if we have a bug it will tell us why
if __name__ == "__main__":
    app.run(debug=True)