from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from jnius import autoclass


Builder.load_string('''
<AudioTool>
	orientation: 'vertical'
	Label:
		id: display_label
		text: '00:00'
	BoxLayout:
		size_hint: 1, .2
		TextInput:
			id: user_input
			text: '5'
			disabled: duration_switch.active == False # TUT 3 IF SWITCH IF OFF TEXTINPUT IS DISABLED
			on_text: root.enforce_numeric()
		Switch:
			id: duration_switch
	BoxLayout:
		Button:
			id: start_button
			text: 'Start Recording'
			on_release: root.startRecording_clock()
		Button:
			id: stop_button
			text: 'Stop Recoding'
			on_release: root.stopRecording()
			disabled: True

	''')

class AudioApp(App):
	def build(self):
		return AudioTool()

class MyRecorder(self):
		 ''' Recorder object to access the Android audio recorder '''
		self.MediaRecorder = autoclass ( 'android.media.MediaRecorder' )  
		self.AudioSource = autoclass ( 'android.media.MediaRecorder $ AudioSource' )  
		self.OutputFormat = autoclasse ( 'android.media.MediaRecorder $ OutputFormat' )  
		self.AudioEncoder = autoclasse ( 'android.media.MediaRecorder $ AudioEncoder' )  
		 
		# Grave o microfone com um gravador 3GP
		self.mRecorder = self.MediaRecorder ( )  
		self.mRecorder . setAudioSource ( self.AudioSource . MIC )
		self.mRecorder . setOutputFormat ( self.OutputFormat . THREE_GPP )
		self.mRecorder . setOutputFile ( '/sdcard/testrecorder.3gp' )
		self.mRecorder . setAudioEncoder ( self.AudioEncoder . ARM_NB )
		self.mRecorder . preparar ( )

class AudioTool(BoxLayout):
	def __init__(self, **kwargs):
		super(AudioTool, self).__init__(**kwargs)

		self.start_button = self.ids['start_button']
		self.stop_button = self.ids['stop_button']
		self.display_label = self.ids['display_label']
		self.switch = self.ids['duration_switch'] # Tutotial 3
		self.user_input = self.ids['user_input']

		
	def enforce_numeric(self):
		if self.user_input.text.isdigit() == False:
			digit_list = [num for num in self.user_input.text if num.isdigit()]
			self.user_input.text = "".join(digit_list)

	def startRecording(self, dt):

		self.r = MyRecorder() # create the recorder object
		self.r.mRecorder.start() # start the recording
	
	def startRecording_clock(self):
		self.mins = 0 # Reset if the a função gets called more that once
		self.zero = 1 # Reset the minutes on our timer

		self.duration = int(self.user_input.text) # Set the duration as the user input text if switch is on
		Clock.schedule_interval(self.updateDisplay, 1)
		self.start_button.disabled = True # Prevents the a user from clicking start again which may crash the program
		self.stop_button.disabled = False
		self.switch.disabled = True # TUT Switch disable when start is pressed
		Clock.schedule_once(self.startRecording)

	def stopRecording(self):
		Clock.unschedule(self.updateDisplay)
		Clock.unschedule(self.startRecording)
		self.display_label.text = 'Fisished Recording!'
		self.start_button.disabled = False
		self.stop_button.disabled = True
		self.switch.disabled = False

	def updateDisplay(self, dt): # dt = delta time
		'''Called every second when start is pressed'''
		if self.switch.active == False: # if the switch if off
			if self.zero < 60 and len(str(self.zero)) == 1: ## '00:0'
				self.display_label.text = '0' + str(self.mins) + ':0' + str(self.zero)
				self.zero += 1

			elif self.zero < 60 and len(str(self.zero)) == 2: ## '00:'
				self.display_label.text = '0' + str(self.mins) + ':' + str(self.zero)
				self.zero += 1

			elif self.zero == 60:
				self.mins += 1 # add a minute
				self.display_label.text = '0' + str(self.mins) + ':00' # EG '01:00'
				self.zero = 1 # Reset zero to start again for a new minute
		
		elif self.switch.active == True:
			if self.duration == 0: # 0
				self.display_label.text = 'Recording Finished!'
				self.stopRecording()

			elif self.duration > 0 and len(str(self.duration)) == 1: # 0-9
				self.display_label.text = '00' + ':0' + str(self.duration)
				self.duration -= 1

			elif self.duration > 0 and self.duration < 60 and len(str(self.duration)) == 2: # 0-59
				self.display_label.text = '00' + ':' + str(self.duration)
				self.duration -= 1

			elif self.duration >= 60 and len(str(self.duration % 60)) == 1: # EG 01:07
				self.mins = self.duration / 60
				self.display_label.text = '0' + str(self.mins) + ':0' + str(self.duration % 60)
				self.duration -= 1
			elif self.duration >= 60 and len(str(self.duration % 60)) == 2: # EG 01:17
				self.mins = self.duration / 60
				self.display_label.text = '0' + str(self.mins) + ':' + str(self.duration % 60)
				self.duration -= 1

if __name__ == '__main__':
	AudioApp().run()

