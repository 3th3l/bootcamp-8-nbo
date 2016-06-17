class NotesApplication(object):
	notes_list = []

	def __init__(self, author):
		self.author = author
		#notes_list = []

	def create(self, note_content):
		#self.note_content = note_content
		self.notes_list.append(note_content)

	def list(self):
		for note in self.notes_list:
			print "Note ID: ", self.notes_list.index(note) + 1
	    	print note
	    	print "By Author ", self.author
	    	print "--------------------------------------------"
    
	def get(self, note_id):
		if note_id >= 0 and note_id < len(self.notes_list):
			print "Note ID: ", str(note_id)
			print "Note Content: ", self.notes_list[note_id]
			print "Author: ", self.author
			print "--------------------------------------------"

	def search(self, note_id):
		self.search_text = search_text
		for search_text in self.note_content:
			print "Showing results for search ", self.search_text
			print "Note ID: ", self.notes_list.index(note) + 1
	    	print note
	    	print "By Author ", self.author
	    	print "--------------------------------------------

	def edit(self, note_id, new_content):

my_notes = NotesApplication("Ethel")

my_notes.create("This girl rocks!")
my_notes.create("TIA rocks!")
my_notes.create("This girl rocks even more!")

my_notes.list()
