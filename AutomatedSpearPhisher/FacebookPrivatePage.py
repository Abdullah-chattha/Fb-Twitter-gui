from tkinter import Label, Button, Entry
from CommonFrame import CommonFrame
from config import pathToTorInstallation
from FacebookChatPhisher import *
# TODO: add posting and phishing text generation 
from FacebookPost import post
import phishingTextGenerator 
from time import sleep
from helpers import *

class FacebookPrivatePage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        
        #subheadings
        setSubHeading(self, 'Private Facebook')
        #Facebook selection path
        createLeftSubHeading(self, 'Please enter fields')
        createRightSubHeading(self, 'Previous Page: Facebook')

        #frame for buttons/entry fields
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        button_manager = ButtonManager(button_frame, self.changePages)

        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')

        #warning symbol if any field missing
        self.field_warning_label = createFieldWarning(button_frame, row=6, col=1)
        self.entry_manager = EntryManager(button_frame, start_row=1, label_col=0, entry_col=1)
        self.entry_manager.addLabelWithEntry('Email used for Facebook:', 'facebook_email_entry')
        self.entry_manager.addLabelWithEntry('Facebook username:', 'facebook_username_entry')
        self.entry_manager.addLabelWithEntry('Facebook Password:', 'facebook_password_entry')
        self.entry_manager.addLabelWithEntry('Number of friends:', 'facebook_numberOfFriends_entry')

        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.send_facebook_quad, row=5, col=1)

        #back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=6,col=0)

    #function to pass arguments to Ashraf's scripts
    def send_facebook_quad(self):
        entry_manager = self.entry_manager
        facebook_email_entry = entry_manager.getValueOfEntry('facebook_email_entry')
        facebook_username_entry = entry_manager.getValueOfEntry('facebook_username_entry')
        facebook_password_entry = entry_manager.getValueOfEntry('facebook_password_entry')
        facebook_numberOfFriends_entry = entry_manager.getValueOfEntry('facebook_numberOfFriends_entry')

        if facebook_email_entry =='' or facebook_username_entry ==''\
            or facebook_password_entry =='' or facebook_numberOfFriends_entry =='' :
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            # login to Facebook
            driver = loginToFacebook(pathToTorInstallation, facebook_email_entry , facebook_password_entry)
            sleep(8)
            # get list of friend's pages
            FULLHTMLPAGE = getFriendsListHTMLPage(driver, facebook_username_entry)
            # extract the URL to their page
            friendURLS = parseHTML(FULLHTMLPAGE, 'friendsurls', 1)
            # scrape and store their likes pages
            # TODO: figure out how to store files in output directory
            scrapeLikePages(driver, friendURLS, int(facebook_numberOfFriends_entry))
            # create phishing text based on created like pages
            # TODO: pass in output and input directory
            phishingTextGenerator.main()
            self.changePages('FacebookPage')
