import argparse
import datetime
import os
import requests

from atproto import Client

# python3 ./main.py --image ../images/2023-07-11-capybara.jpg --text "I'm the crime boss."


def main():
    email = os.getenv('BLUESKY_BOT_EMAIL')
    password = os.getenv('BLUESKY_BOT_PASSWORD')

    if email is None or password is None:
        print('Error: Please set BLUESKY_BOT_EMAIL and BLUESKY_BOT_PASSWORD environment variables.')
        return

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', help='Path or URL to the image')
    parser.add_argument(
        '--text', help='Text of the image and the ALT attribute')

    args = parser.parse_args()

    # Check if the image path is provided
    if args.image:
        image_path = args.image
    else:
        # Generate default filename
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        default_filename = f'{current_date}-capybara.jpg'
        image_path = os.path.join(os.getcwd(), default_filename)

    client = Client()
    profile = client.login(email, password)
    print('Welcome,', profile.displayName)

    # Get that capy image data
    capybara_image_data = get_capybara_image(image_path)
    # print(f'Image data: {capybara_image_data}')

    text = args.text if args.text else 'Don\'t worry, be Cappy!'

    client.send_image(
        text=text, image=capybara_image_data, image_alt=text
    )


def get_capybara_image(image_path):
    if image_path.startswith('http://') or image_path.startswith('https://'):
        # Image path is a URL
        response = requests.get(image_path)
        image_data = response.content
    else:
        # Image path is a file path
        with open(image_path, 'rb') as f:
            image_data = f.read()

    return image_data


if __name__ == '__main__':
    main()
