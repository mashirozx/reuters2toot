from mastodon import Mastodon
import filetype
from .get_config import GetConfig

config = GetConfig()

mastodon = Mastodon(
  access_token = config['MASTODON']['AccessToken'],
  api_base_url = config['MASTODON']['BaseUrl']
)

def media_post(file):
  kind = filetype.guess(file)
  # print('File extension: %s' % kind.extension)
  # print('File MIME type: %s' % kind.mime)
  return mastodon.media_post(file, kind.mime)

def TootPoster(data):
  """
  :data object: Return from media_downloader
  :return void
  """
  
  # print(data['plain'])
  try:
    mastodon.status_post(status=f"【{data['title']}】\n\n{data['plain']}", visibility=config['MASTODON']['TootVisibility'])
  except Exception:
    print(f'ERRO: failed[mastodon.status_post]')
    # for e in Exception:
    #   print(e)

if __name__ == '__main__':
  test_data = {'gif_count': 1, 'video_count': None, 'image_count': 3, 'plain': 'Tooting from python using `status_post` #mastodonpy !'}
  TootPoster(test_data)