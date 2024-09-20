import cloudinary
import cloudinary.uploader

# Set up your Cloudinary configuration
cloudinary.config(
    cloud_name='drfznyqrt',
    api_key='828333267236618',
    api_secret='1J9Hxb8yJiF8T-YMQ1B14ATTzxY'
)

# Upload an image
response = cloudinary.uploader.upload('media/media/blog/TechTuts.png')
print(response)  # Check if the upload was successful
