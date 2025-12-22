class Activity:

	def __init__(self, _id: str, status: str, title: str, progress: str, site_url: str):
		self.id = _id
		self.status: str = status
		self.title: str = title
		self.progress: str = progress
		self.site_url = site_url

	def __str__(self) -> str:
		return f"{self.status} {self.progress} of {self.title}"

	def __eq__(self, other):
		return (
			self.id == other.id
			and self.status == other.status
			and self.title == other.title
			and self.progress == other.progress
			and self.site_url == other.site_url
		) 