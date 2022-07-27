# https://github.com/Imgur/imgurpython/tree/master/examples
'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'
	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

# Pull authentication from the auth example (see auth.py)
from auth import authenticate
from datetime import datetime

# You can also enter an album ID here
# https://ithelp.ithome.com.tw/articles/10241006
album = 'pVOzoNI'
image_path = 'test.jpg'

def upload_img(client, img_path, album, name='test-name', title='test-title'):
	# Here's the metadata for the upload. All of these are optional, including this config dict itself.
	config = {
		'album': album,
		'name':  name,
		'title': title,
		'description': f'test-{datetime.now()}'
	}
	print("Uploading image... ")
	image = client.upload_from_path(img_path, config=config, anon=False)
	print("Done")

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
    # 整個 image 的資訊為 JSON檔案，可以 print() 輸出確認
	image = upload_img(client, image_path, album)
	print("Image was posted! Go check your images you sexy beast!")
	print("You can find it here: {0}".format(image['link']))