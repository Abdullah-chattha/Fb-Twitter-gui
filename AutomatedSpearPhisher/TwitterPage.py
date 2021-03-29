from tkinter import Label, Button, Frame, Entry
from tweetGenerator import createCorpusForUser
from tweetGenerator import generateTweet
from CommonFrame import CommonFrame
from helpers import *

#-------------------------------------------Twitter page----------------------------------------------
class TwitterPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)           

        #subheadings
        setSubHeading(self, 'Twitter')
        #twitter selection path
        createLeftSubHeading(self, 'Please enter fields')
        createRightSubHeading(self, 'Previous Page: Main menu')

        #frame for buttons
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        #twitter symbol
        createPictureInFrame(button_frame, 'images/twitter.png')
        self.addButtons(button_frame)
        self.field_warning_label = createFieldWarning(button_frame, row=2, col=1)

        #entry fields
        self.entry_manager = EntryManager(button_frame, start_row=0, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)

    #function to pass to Ashraf's scripts
    def send_twitter_handle (self):
        entry_manager = self.entry_manager
        twitter_handle = entry_manager.getValueOfEntry('twitter_handle')
        if twitter_handle =='':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            #call tweet generator
            createCorpusForUser (twitter_handle)
            generateTweet (twitter_handle, 'example.com')

            #print(twitter_handle)
            self.changePages('MenuPage')

    def addButtons(self, button_frame):
        button_manager = ButtonManager(button_frame, self.changePages)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.send_twitter_handle, row=1, col=1)
        #back button
        button_manager.createChangePageButton(page_name='MenuPage', text='Back', row=2,col=0)

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Twitter handle of account:', 'twitter_handle')