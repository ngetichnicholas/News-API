class News:
  '''
  News class to define news objects
  '''

  def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
    self.author =author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.puplishedAt = publishedAt
    self.content = content

class Source:
  def __init__(self,id,name):
    self.id = id
    self.name = name
      