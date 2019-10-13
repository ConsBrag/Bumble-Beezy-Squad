class Diplom():

  def __init__(self):
    self._topic = ''
    self.paragraphs = []

  @property
  def topic(self):
    return self._topic

  @topic.setter
  def topic(self, topic):
    self._topic = topic