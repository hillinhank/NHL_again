#! /var/mail/flask
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# this wraps our app in an api and this initializes a restful api
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video (name = {name}, views = {views}, likes = {likes})"
        

# db.create_all() COMMENT OUT create_all so we dont override that data in our db

# make a new request parser object
## will automatically parse through requests that are being sent to make sure it fits the guidelines we choose
video_put_args = reqparse.RequestParser()
# 
video_put_args.add_argument("name", type=str, help="name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="views of the video is required", required = True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required = True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of the video is required")
video_update_args.add_argument("views", type=int, help="views of the video is required")
video_update_args.add_argument("likes", type=int, help="likes of the video is required")

resource_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}

# make a resource in this api, 
# when a get request is sent via .add_resource information will be sent based on the video_id I have asked for
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message= "no video found")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message = "Video is taken...")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        ab_if_vid_not(video_id)
        del videos[video_id]
        return '', 204


# now need to register this as a resource api.add_resource(Class, url) (can use a / to use a default url)
# essentially, it determines what the root of the resource will be
api.add_resource(Video, "/https://statsapi.web.nhl.com/api/v1/")

# this starts both the server and the application
# debug=True says that we are in debug mode so we will see all of that output and any logging information, so if we have a bug it will tell us why
if __name__ == "__main__":
    app.run(debug=True)