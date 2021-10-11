from urllib import request as url_request
from urllib import error as url_error

def decode_words(url):

    story_words = []
    try:
        story= url_request.urlopen(url)
        for line in story:
            story_words.append(line.decode('utf-8'))
    except (url_error) as error:
        print(error)
        return None
    finally:
        story.close()
    return story_words
