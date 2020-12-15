"""
    File: passwordG.py
    Abstract: Create a app the displays the proper password genereator that is need with
                the car alogrimth
    Date: 12/2/2020
    Author: Brendon Magana for CST 205

"""
# https://kivy.org/doc/stable/api-index.htmls
import os
import kivy
from kivy.config import Config
kivy.require("1.9.1") 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from colour import Color
from kivy.core.clipboard import Clipboard
from kivy.core import window
# from core import logger
import pyperclip
import random


red = [1,0,0,1]
blue = [0,0,1,1]
white = '#FFFFFF'

if_the_user_agree = False

generatedPassword = str()


class MainApp(App):

    #variables to keep track of the text fields for later additon
    # l_info = ObjectProperty(None)
    #passwordT = ObjectProperty(None)

    # 0 being off 1 being on as in true / false 
    # you can use 0 or 1 && True or False 
    Config.set('graphics', 'resizable', '0') 
  
    # fix the width of the window  
    Config.set('graphics', 'width', '1280') 
  
    # fix the height of the window  
    Config.set('graphics', 'height', '720') 

    
    
    

    def build(self):

        

        main_layout = BoxLayout(padding = 10, orientation="vertical")
        
        #----------------------- fucntions for events--------------------------------------

        

        def location_agrement(self):
            test_prompt = "Agreed: We will now take your \n current location! <%add location>"

            lGl = globals()

            

            # once the button is seleced then we have to change the variable to true
            lGl['if_the_user_agree'] = True

            iA = if_the_user_agree

            if iA == True:
                l_info.text = test_prompt
            else:
                l_info.text = "Please agree"


            

        def pressed(self):
            #this string will change to the class that my team leader will make using the algorthim.
            lgL = globals() 

            passswordGen = ""

            

            if t_input.text == "":
                passwordT.text = "Enter the complexity!"
            elif (int)(t_input.text) < 5:
                passwordT.text = "Please raise the complexity!"
            elif (int)(t_input.text) > 36:
                passwordT.text = "Please lower the complexity"
            else:

                complectiy_num = (int)(t_input.text)

                if(complectiy_num >=5 and complectiy_num <= 36):
                    #make the proper commands for the user
                    for x in range(complectiy_num):
                        passswordGen += (chr)(random.randint(1,101))
                
            

                lgL['generatedPassword']  = str(passswordGen)

                global if_the_user_agree

                iA = if_the_user_agree

                passwordText = passwordT.text

                if iA == True:
                    passwordT.text = generatedPassword
                elif iA == False:   
                    passwordT.text = "Please agree to the \n location terms"



            # if(complectiy_num >=5 and complectiy_num <= 36):
            #     #make the proper commands for the user
            #     for x in range(complectiy_num):
            #         passswordGen += (chr)(random.randint(1,101))
                
            

            # lgL['generatedPassword']  = str(passswordGen)

            # global if_the_user_agree

            # iA = if_the_user_agree

            # passwordText = passwordT.text

            # if iA == True:
            #     passwordT.text = generatedPassword
            # elif iA == False:   
            #         passwordT.text = "Please agree to the \n location terms"

        
        

        def copy_password(self):
            globals()
            try:
                Clipboard.copy(generatedPassword)
                
            except:
                print("Could not be copied to clipboard: " + generatedPassword)
                pass

            
        #---------------------------------- end------------------------------------

        #---------------------- header(name of the program) --------------------------

        v_layout = BoxLayout(size=(1,1),size_hint=(.5,.5),
                      pos_hint={'center_x': .5, 'center_y': 1})
        
        label = Label(text = 'TraffKey',
                      size=(25,25),
                      size_hint = (.5,1),
                      font_size = '30sp',
                      bold = True,
                      color = red
                      #border = (5,'solid', (1,1,1,1.))
                      #background_color = {1,0,0,1}
                      )

        #add the widget to the layout
        v_layout.add_widget(label)

        main_layout.add_widget(v_layout)
        
        #------------------------------ end ----------------------------------

        #-------------------------------- text field to prompt the use to aggree to the terms and add the comlpecity----------

        v_prompt_for_user = BoxLayout(
                                        padding=5,
                                        size=(50,50),
                                        
                                        pos_hint={'center_x': .4, 'center_y': 1}
                                        )

        prompt_for_user = Label(size=(55,25),
                                font_size = 20,
                                #size_hint = (.5,1),
                                text="""
                                In order to generate a password you will need to:
                                - Add the level of difficulty in the text box below, 
                                - Agree for us to use your location by selecting the
                                  button below
                                - Finally, Select the generate button below. 
                                """
                                )

        v_prompt_for_user.add_widget(prompt_for_user)

        main_layout.add_widget(v_prompt_for_user)


        #-------------------------------- end ------------------------------------------------------

        #-------------------------------------- complexity of the password------------------

        v2_layout = BoxLayout(padding=5,
                              size=(50,25),
                              size_hint=(.5,.3)
                              )

        t_input = TextInput(hint_text='complexity of the password: 5-36 charaters long')

        v2_layout.add_widget(t_input)

        main_layout.add_widget(v2_layout)

        #------------------------------- end --------------------------------------


        #-------------------------------- Button to agree location ------------------------------

        v3_layout = BoxLayout(padding=10,
                               size=(50,25),
                               size_hint=(.5,.3))

        btn_location = Button(text=" User Agree to sharing location",
        background_color=red,
        pos_hint={'center_x': .3,'center_y': .5},
        )

        # bind the btn_location to change prompts as the user secteclts propper information.

        btn_location.bind(on_press=location_agrement)

        #add the button to the layout
        v3_layout.add_widget(btn_location)

        main_layout.add_widget(v3_layout)

        #--------------------------------- end ----------------------------------

        #---------------------------------- click buttton to generate password--------------

        v4_layout = BoxLayout(padding = 10,
                               size = (50,25),
                               size_hint = (.5,.3)
                                )
        btn_generate = Button(text = "Click to generate new password",
                              background_color=red,
                              pos_hint = {'center_x': .3,'center_y': .5}
                            )
        #bind that makes the function change text

        
        btn_generate.bind(on_press=pressed)

        #add the button to a vertical layer to make the second button apper
        v4_layout.add_widget(btn_generate)

        #add to the main layout
        main_layout.add_widget(v4_layout)

        #---------------------------------- end ----------------------------------

        #------------------------------------ horizontal text box layout --------------------------

        main_h_layout = BoxLayout(orientation ='horizontal'
                                  #size=(25,25),
                                  #size_hint=(.5,.3)
                                  )

        #--------------------------------------- Prompt text box ------------------------------------

        h_layout = BoxLayout(
                        pos_hint = {'center_x': .5,'center_y': .5},
                         size=(10,10),
                         size_hint=(1.4,.5)
                        )

        #this label will change due to the users actions!
        l_info = Label(text="""Please agree to the location activation """ 
                       )


        h_layout.add_widget(l_info)

        main_h_layout.add_widget(h_layout)

        #--------------------------------------- end -------------------------------------------

        #----------------------------------------- password text field ---------------------------

        h2_layout = BoxLayout(
                               #size_hint=(.5,.3)
                               )

        passwordT = Label(text='The password will pop up',
                                size = (20,20)
                                )

        h2_layout.add_widget(passwordT)

        main_h_layout.add_widget(h2_layout)

        #--------------------------------- copy button ------------------------------------------

        h3_layout = BoxLayout(  pos_hint = {'center_x': .5,'center_y': .5},
                                size_hint =(.5, .25), 
                                pos =(20, 20)
                                #size_hint = (.5,.5)
                                
                              )

        copy_btn = Button(text="Copy")


        #makes the copy option become true
        copy_btn.bind(on_press=copy_password)

        h3_layout.add_widget(copy_btn)

        main_h_layout.add_widget(h3_layout)

        #---------------------------------- end ----------------------------------------------

        #------------------------------------------ end ---------------------------------

        # finally add the horizontal layout to the vertical layout to make the flow work

        main_layout.add_widget(main_h_layout)
        
        




        #---------------------------------- end ----------------------------------

        


        return main_layout

    

if __name__ == '__main__':
 app = MainApp()
 app.run()