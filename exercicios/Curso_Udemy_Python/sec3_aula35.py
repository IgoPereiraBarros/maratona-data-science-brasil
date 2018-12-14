
class AudioFile:

	def __init__(self, filename):

		if not filename.endswith(self.ext):
			raise Exception('Formato inválido!')

		self.filename = filename


class MP3File(AudioFile):

	ext = 'mp3'

	def play(self):
		print('Tocando arquivo mp3')


class WavFile(AudioFile):

	ext = 'wav'

	def play(self):
		print('Tocando arquivo wav')
		

class OggFile(AudioFile):

	ext = 'ogg'

	def play(self):
		print('Tocando arquivo ogg')

mp3 = MP3File('algo.mp3')
mp3.play()

wav = WavFile('algo.wav')
wav.play()

ogg = OggFile('algo.mp3')
ogg.play()