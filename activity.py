class Activity:

	def __init__(self, _id: str, status: str, title: str, progress: str):
		self.id = _id
		self.status: str = status
		self.title: str = title
		self.progress: str = progress

	def __str__(self) -> str:
		return f"{self.status} {self.progress} of {self.title}"

	def __eq__(self, other):
		return self.id == other.id