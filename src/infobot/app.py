import requests,json
class bot:
	def ok(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url['ok']
		except:return json.loads('{"ok":"false"}')


	def token(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			s = self.url['ok']
			return token
		except:return json.loads('{"ok":"false"}')


	def first_name(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['first_name']	
		except:return json.loads('{"ok":"false"}')


	def id(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['id']	
		except:return json.loads('{"ok":"false"}')


	def is_bot(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['is_bot']	
		except:return json.loads('{"ok":"false"}')


	def username(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['username']	
		except:return json.loads('{"ok":"false"}')


	def can_join_groups(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['can_join_groups']	
		except:return json.loads('{"ok":"false"}')


	def can_read_all_group_messages(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['can_read_all_group_messages']	
		except:return json.loads('{"ok":"false"}')


	def supports_inline_queries(self,token):
		self.url =requests.get(f"https://api.telegram.org/bot{token}/getme").json()
		try:
			return self.url["result"]['supports_inline_queries']	
		except:return json.loads('{"ok":"false"}')

#MUamel Ameer