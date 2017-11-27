from pytest import skip
from flask import Flask, request, jsonify
#import multipart_url.py

class TestMultipartUrl(object):
	
	def test_can_call_an_address(self):
		#given 
		handler = Flask('multipart-url-receiver')		
		handler.run()
		@handler.route('/', methods=['GET'])
		def entry():
			return ""
		
		address = 'http://127.0.0.1:5000'
		#when
		#calling_url
		
			response=multipart_url.post_to_url(address)
		handler.stop()
		#then
		OK=200
		assert response.status == OK

