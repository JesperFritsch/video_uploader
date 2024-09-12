
# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
from cloudinary import CloudinaryImage
from cloudinary.uploader import upload, upload_large, explicit
import cloudinary.api
from cloudinary.api import resource
from pprint import pprint

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

# Upload an image
# ==============================
# response = upload(r"B:\bilder\Coca_Cola_Classic_1920x1080.jpg")

# print(response)


#Upload a video
# response = upload(
#     r"B:\pythonStuff\snake_sim\snake_sim\render\videos\1_snakes_32x32_BDG00W_7675.mp4",
#     resource_type="video",
#     folder="snake_videos",
#     eager=[
#         {'width': 1080, 'height': 1350, 'crop': 'pad', 'background': 'blurred', 'quality': 'auto'},  # Adds padding to maintain a square format
#     ],
#     eager_async=True,
#     format="mp4",
#     video_codec="h264",
#     audio_codec="aac",
# )

# response = explicit(
#     'snake_videos/uyjgmfi0uwvcyijwhvkq',  # Use the public_id from the upload response
#     resource_type="video",
#     type="upload",  # Specifies the resource type as an uploaded video
#     eager=[
#         {'width': 1080, 'height': 1080, 'crop': 'pad', 'background': 'gray', 'quality': 'auto'}
#     ],
#     eager_async=True  # Ensure the transformation is done asynchronously
# )

response = cloudinary.api.resource(
    "snake_videos/uyjgmfi0uwvcyijwhvkq",  # Replace with the actual public_id of the uploaded video
    resource_type="video"
)

pprint(response)