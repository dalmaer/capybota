import os
import argparse
from datetime import datetime, timedelta


def copy_images_with_dates(input_dir, start_date):
    if not os.path.exists(input_dir):
        print("Input directory not found.")
        return

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid start date format. Use YYYY-MM-DD.")
        return

    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.jpg')):
                file_path = os.path.join(root, filename)
                new_date = start_date.strftime("%Y-%m-%d")
                new_filename = f"{new_date}-capybara.jpg"
                new_path = os.path.join(root, new_filename)

                while os.path.exists(new_path):
                    start_date += timedelta(days=1)
                    new_date = start_date.strftime("%Y-%m-%d")
                    new_filename = f"{new_date}-capybara.jpg"
                    new_path = os.path.join(root, new_filename)

                os.rename(file_path, new_path)
                print(f"Renamed {filename} to {new_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copy images with formatted dates.")
    parser.add_argument("--start-date", required=True,
                        help="Initial start date in YYYY-MM-DD format.")
    parser.add_argument("input_dir", help="Input directory containing images.")

    args = parser.parse_args()
    copy_images_with_dates(args.input_dir, args.start_date)
