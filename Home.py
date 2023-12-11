import streamlit as st
from st_paywall import add_auth

st.title("Welcome to Imaginarium Weaver")

add_auth(required=True)

def checkout_form():
    with st.expander('',expanded=True):        
        st.markdown("Let's make a story")
        options = ['Storybook Elements','AI Builder','Summary/organize','Payment Information', 'download finished materials']        
        radio_cols = st.columns([.25,10])
        step = radio_cols[1].radio(label='',label_visibility='collapsed', options=options,horizontal=True,index=0)                
        if step == 'Storybook Elements':
            st.text("build a story for your loved one! once you're done, send it over to them as a physical copy or as a digital file!")
        def create_story_form():
                # Genre options
            genre = st.selectbox(
                st.write("Choose the Genre")
                options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", 
                             "Historical Adventure", "Mythological Tale", "Superhero Story", "Time Travel Adventure", "Dystopian World", 
                             "surprise me"]
                )
                # Setting options
                setting = st.selectbox(
                    "Choose the Setting:",
                    options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", 
                             "Ancient Ruins", "Haunted House", "Futuristic City", "Magical Kingdom", "Pirate Ship", 
                             "surprise me"]
                )
                # Supporting Characters options
                supporting_characters = st.selectbox(
                    "Choose Supporting Character(s):",
                    options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", 
                             "Brave Knight", "Mysterious Sorcerer", "Loyal Sidekick", "Royal Guard", "Clever Inventor", 
                             "surprise me"],
                )
                # Plot Elements options
                plot_elements = st.selectbox(
                    "Choose Plot Elements:",
                    options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", 
                             "A Forbidden Love", "A Mysterious Prophecy", "A Legendary Sword", "An Unlikely Hero", "A Forbidden Spell", 
                             "surprise me"]
                )
                # Theme options
                theme = st.selectbox(
                    "Choose the Theme:",
                    options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", 
                             "Overcoming Fear", "Love and Sacrifice", "The Power of Imagination", "Trust and Betrayal", "Growth and Transformation", 
                             "surprise me"]
                )
                # Object options
                magical_objects = st.selectbox(
                    "Choose Magical Objects:",
                    options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", 
                             "Time-Turning Hourglass", "Phoenix Feather", "Crystal Ball", "Shape-shifting Potion", "Teleportation Ring", 
                             "surprise me"]
                )
                # Tone/Mood options
                tone = st.selectbox(
                    "Choose the Tone/Mood:",
                    options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", 
                             "Suspenseful", "Whimsical", "Inspirational", "Spooky", "Nostalgic", 
                             "surprise me"]
                )
                # Submit button
                submitted = st.form_submit_button("Create Story")
                if submitted:               # Process the selections and generate the story (this part will interface with the AI model)
                    #def display_story_form(relation, name_of_reciptient, genre, setting, supporting_character, plot_elements, theme, magical_objects, tone):
                        st.write(f"I'd like you create a story about my {relation}, {name_of_reciptient}. The story's Genre will be: {genre}, with a setting as: {setting}. A supporting character will be: {supporting_characters}, with a plot element of: {plot_elements}. The theme of the story is: {theme}, a magical object, included somewhere in the story is a: {magical_objects}, and the tone will be: {tone} ")
        create_story_form(
            
        # )
        # st.markdown('##### Lets start with the basic details.')            
        # name_cols = st.columns(2)
        # name_cols[0].text_input('**Travler Name**', placeholder='First Name')
        # name_cols[1].text_input('Last Name',label_visibility='hidden', placeholder='Last Name')
        # st.text_input('**Traveler Email**',placeholder='📧 Your Email')
        # f_cols = st.columns(2)                  
        # f_cols[1].selectbox('**Traveler Origin**',options=['United States','Canada','Mexico'] )
        # f_cols[0].date_input('**Traveler Date of Birth**')
        #     if step == 'AI Builder':
        #     date_cols =st.columns(3)
        #     date_cols[0].date_input('Check In Date')
        #     date_cols[1].date_input('Check Out Date')
        #     date_cols[2].selectbox('Room Type',options=['Standard','Deluxe','Suite'])
        #     st.markdown('---')
        #     option_cols = st.columns(2)
        #     with option_cols[0]:                                                                
        #         image = Image.open('assets/desert.jpg')
        #         st.image(image, caption='Our Desert View',use_column_width=True)
        #         st.write('**Room, 1 King Bed**')                
        #         dim_cols = st.columns(2)
        #         dim_cols[0].write('📏 550 sq ft')
        #         dim_cols[0].write('🌵 Desert View')
        #         dim_cols[1].write('👥 Sleeps 2')
        #         dim_cols[1].write('🛏️ King Size')          
        #         policy_cols = st.columns(2)          
        #         policy = policy_cols[0].radio('**Cancellation Policy**',options=['Non-Refundable','Fully Refundable'],horizontal=False,key='option1')
        #         delta_color, delta_val = ('off',0) if policy == 'Non-Refundable' else ('normal',50)
        #         base_price = 450
        #         price = base_price if policy == 'Non-Refundable' else base_price + delta_val                                
        #         policy_cols[1].metric('**Nightly Price**',value=f'$ {price}',delta_color=delta_color,delta=f'$ {delta_val}')
        #         st.button('Select',type='primary',key='select_1')
        #     with option_cols[1]:                
        #         image = Image.open('assets/ocean.jpg')
        #         st.image(image, caption='Our Ocean View',use_column_width=True)
        #         st.write('**Room, 2 Full Beds**')                
        #         dim_cols = st.columns(2)
        #         dim_cols[0].write('📏 600 sq ft')
        #         dim_cols[0].write('🏖️ Ocean View')
        #         dim_cols[1].write('👥 Sleeps 4')
        #         dim_cols[1].write('🛏️ Full Size')                                    
        #         policy_cols = st.columns(2)                
        #         policy = policy_cols[0].radio('**Cancellation Policy**',options=['Non-Refundable','Fully Refundable'],horizontal=False,key='option2')
        #         delta_color, delta_val = ('off',0) if policy == 'Non-Refundable' else ('normal',50)
        #         base_price = 450
        #         price = base_price if policy == 'Non-Refundable' else base_price + delta_val                
        #         policy_cols[1].metric('**Nightly Price**',value=f'$ {price}',delta_color=delta_color,delta=f'$ {delta_val}')#,label_visibility='hidden'
        #         st.button('Select',type='primary',key='select_2')                                  

        if step == 'Summary/organize': 
            st.markdown('---')            
            st.write('**Traveler Information**')
            summ_cols = st.columns(2)           
            summ_cols[0].text_input('**Travler Full Name**', placeholder='First Name',disabled=True)            
            summ_cols[1].text_input('**Traveler Email**',placeholder='Your Email',disabled=True)       
            f_cols = st.columns(2)                  
            f_cols[1].text_input('**Traveler Origin**',disabled=True,placeholder='United States')
            f_cols[0].date_input('**Traveler Date of Birth**',disabled=True)                                         
            st.write('**Arrival & Departure Information**')
            date_cols =st.columns(2)
            date_cols[0].date_input('**Arrival Date**',disabled=True)
            date_cols[1].date_input('**Departure Date**',disabled=True)                        
            st.write('**Room Information**')
            room_cols = st.columns(2)
            room_cols[0].text_input('**Room Type**',disabled=True,placeholder='Standard')
            room_cols[1].text_input('**Beds**',disabled=True,placeholder='1 King')

        if step == 'Payment Information':
            st.text_input('**Credit Card Information**',placeholder='Card Number')
            exp_cols = st.columns(2)
            exp_cols[0].text_input('',placeholder='Expires',label_visibility='collapsed')
            exp_cols[1].text_input('',placeholder='CVV',label_visibility='collapsed')
            st.text_input('**Billing Address**',placeholder='Address 1')
            st.text_input('',placeholder='Address 2',label_visibility='collapsed')
            st.text_input('',placeholder='Postal Code',label_visibility='collapsed')
            footer_cols = st.columns([5,1])                 
            agreed = footer_cols[0].checkbox('I agree to terms and conditions')
            footer_cols[1].button('Submit',type='primary',key='submit_btn',disabled=not agreed)
        if step == 'download finished materials':
            st.write('set up')
        #only accesible if payment was submitted

##### wizard functions ####
def wizard_form_header():
    sf_header_cols = st.columns([1,1.75,1])
        
    with sf_header_cols[1]:            
        st.subheader('Load Data to Snowflake')
            
    # determines button color which should be red when user is on that given step
    wh_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
    ff_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
    lo_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
    sf_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

    step_cols = st.columns([.5,.85,.85,.85,.85,.5])    
    step_cols[1].button('Warehouses',on_click=set_form_step,args=['Jump',1],type=wh_type)
    step_cols[2].button('File Format',on_click=set_form_step,args=['Jump',2],type=ff_type)        
    step_cols[3].button('Load Options',on_click=set_form_step,args=['Jump',3],type=lo_type)      
    step_cols[4].button('Source Files',on_click=set_form_step,args=['Jump',4],type=sf_type)
        
st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write("congrats on your future winnings now get in there champ")
st.write(f'for your records and future logins, your email is: {st.session_state.email}')

st.title("Create custom printed material for a family member, a loved one, or anyone!")
# File uploader allows user to add their own image
uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])

# Check if an image has been uploaded
if uploaded_img is not None:
    # To read image file buffer with PIL:
    from PIL import Image
    image = Image.open(uploaded_img)

    # Display the uploaded image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Please verify that this is the correct image. If not, please delete and upload a new image")
else:
    st.warning("Please upload an image.")

relation= st.text_input("relation to the reciptient")
if relation:
    st.success(relation)

name_of_reciptient= st.text_input("insert the name of the recipient here")
if name_of_reciptient:
    st.success(name_of_reciptient)
"---"

### end of picture and relation items ###


#option = st.selectbox(
    #label= "choose a form of print",
    #options= ("children's story (boardbook)", "card", "coloring page(s)"))

### Children's story option selected ###
#if option == "children's story (boardbook)":
        
   
# ### coloring pages selected ###
# if option == "coloring page(s)":
#     st.text("build a page or pages of a coloring book including your loved one in it!")

#how many coloring pages do they want?

### Card option selected ###
# if option == "card":
#     st.text("build a card for anyone and send it right to them!")

#     # SelectBox for selecting the main category
#     category = st.radio( options=['Holidays', 'Special Occasions', 'Sentiments and Emotions','Specific Achievements','Seasonal','Invitations'], label= 'select a category' )
#     if category =='Holidays':
#         selected_option= st.selectbox(
#                 label= 'Holiday options',
#                 options=[
#         "Christmas", "New Year's", "Easter", "Thanksgiving", "Valentine's Day",
#         "Halloween", "Mother's Day", "Father's Day", "Independence Day",
#         "St. Patrick's Day", "Hanukkah", "Diwali", "Chinese New Year", "Eid al-Fitr"
#     ]
#         )
#     elif category =='Special Occasions':
#         selected_option= st.selectbox(
#                 label= 'Special Occasions',
#                 options=[
#         "Birthdays", "Anniversaries", "Weddings", "Engagements", "Graduations",
#         "Retirements", "New jobs or promotions", "Housewarmings", "Baby showers",
#         "Baptisms or Christenings", "Bar or Bat Mitzvahs", "Confirmations",
#     ]
#         )

#     elif category =='Sentiments and Emotions':
#         selected_option= st.selectbox(
#                 label= 'Sentiments and Emotions',
#                 options= [
#         "Thank you", "Congratulations", "Sympathy or Condolences", "Get well soon",
#         "Apologies", "Thinking of you", "Missing you", "Love and romance",
#         "Friendship", "Encouragement", "Empathy", "Good luck", "Farewell or goodbye"
#     ]
#         )
#     elif category =='Specific Achievements':
#         selected_option= st.selectbox(
#                 label= 'Specific Achievements',
#                 options= [
#         "Academic achievements", "Sporting achievements", "Personal milestones",
#         "Professional milestones", "Recovery from illness", "Sobriety milestones"
#     ]
#         )
#     elif category =='Seasonal':
#         selected_option= st.selectbox(
#             label='Seasonal',
#             options= [
#         "Spring", "Summer", "Autumn", "Winter greetings", "Daylight Saving Time reminders"
#     ]
#         )
#     elif category == 'Invitations':
#         selected_option= st.selectbox(
#             label= 'Invitations',
#             options= [
#         "Parties", "Weddings", "Baby showers", "Bachelor/Bachelorette parties",
#         "Business events", "Ceremonies", "Family reunions"
#     ]
#         )
#         # Define a function to display the selected options
#     def display_selections(category, selected_option):
#         st.write(f"You have choosen the following: {selected_option} within the {category} category")

#     # Button to confirm all selections
#     if st.button("Lock in Answers"):
#         display_selections(category, selected_option)
