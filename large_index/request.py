#!/usr/bin/python3

import requests
from large_index.config import Config

class Request:
  def __init__(self,
    request: str = '',
  ):
    super().__init__()
    self.request = request

  def status_request(self):
    return self.request.status_code == 200

if __name__ == "__main__":
  class_request = Request()
  class_request.status_request()
