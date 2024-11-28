import requests
from bs4 import BeautifulSoup
import time

def get_free_udemy_courses(retries=3, delay=5):
    url = "https://www.real.discount/filter/?category=All&store=Udemy&price=0&rating=0&sort=Newest"
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            break
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise RuntimeError(f"Failed to retrieve data after {retries} attempts. Error: {e}")

    if response.status_code != 200:
        raise RuntimeError(f"Failed to load the website. HTTP Code: {response.status_code}.")

    soup = BeautifulSoup(response.content, 'html.parser')
    courses = []

    for course in soup.find_all('div', class_='col-md-4'):
        title = course.find('h3').text.strip()
        link = course.find('a', class_='card-footer-item')['href']
        courses.append({'title': title, 'link': link})

    return courses

if __name__ == "__main__":
    try:
        free_courses = get_free_udemy_courses()
        for course in free_courses:
            print(f"Course: {course['title']}\nLink: {course['link']}\n")
    except RuntimeError as e:
        print(e)