import streamlit as st
from st_paywall import add_auth

st.title("Welcome to Imaginarium Weaver")

if add_auth(required=True):

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
  
  
  option = st.selectbox(
      label= "choose a form of print",
      options= ("children's story (boardbook)", "card", "coloring page(s)"))
  
  ### Children's story option selected ###
  if option == "children's story (boardbook)":
          st.text("build a story for your loved one! once you're done, send it over to them as a physical copy or as a digital file!")
          def create_story_form():
              with st.form("story_form"):
                  # Genre options
                  genre = st.selectbox(
                      "Choose the Genre:",
                      options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "surprise me"]
                  )
  
                  # Setting options
                  setting = st.selectbox(
                      "Choose the Setting:",
                      options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "surprise me"]
                  )
  
                  # Supporting Characters options
                  supporting_characters = st.selectbox(
                      "Choose Supporting Character(s):",
                      options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "surprise me"],
                  )
  
                  # Plot Elements options
                  plot_elements = st.selectbox(
                      "Choose Plot Elements:",
                      options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "surprise me"]
                  )
  
                  # Theme options
                  theme = st.selectbox(
                      "Choose the Theme:",
                      options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "surprise me"]
                  )
  
                  # Object options
                  magical_objects = st.selectbox(
                      "Choose Magical Objects:",
                      options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "surprise me"]
                  )
  
                  # Tone/Mood options
                  tone = st.selectbox(
                      "Choose the Tone/Mood:",
                      options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "surprise me"]
                  )
          
                  # Submit button
                  submitted = st.form_submit_button("Create Story")
                  if submitted:               # Process the selections and generate the story (this part will interface with the AI model)
                      #def display_story_form(relation, name_of_reciptient, genre, setting, supporting_character, plot_elements, theme, magical_objects, tone):
                          st.write(f"I'd like you create a story about my {relation}, {name_of_reciptient}. The story's Genre will be: {genre}, with a setting as: {setting}. A supporting character will be: {supporting_characters}, with a plot element of: {plot_elements}. The theme of the story is: {theme}, a magical object, included somewhere in the story is a: {magical_objects}, adn the tone will be: {tone} ")
          create_story_form(
              
          )
     
  ### coloring pages selected ###
  if option == "coloring page(s)":
      st.text("build a page or pages of a coloring book including your loved one in it!")
  
  #how many coloring pages do they want?
  
  ### Card option selected ###
  if option == "card":
      st.text("build a card for anyone and send it right to them!")
  
      # SelectBox for selecting the main category
      category = st.radio( options=['Holidays', 'Special Occasions', 'Sentiments and Emotions','Specific Achievements','Seasonal','Invitations'], label= 'select a category' )
      if category =='Holidays':
          selected_option= st.selectbox(
                  label= 'Holiday options',
                  options=[
          "Christmas", "New Year's", "Easter", "Thanksgiving", "Valentine's Day",
          "Halloween", "Mother's Day", "Father's Day", "Independence Day",
          "St. Patrick's Day", "Hanukkah", "Diwali", "Chinese New Year", "Eid al-Fitr"
      ]
          )
      elif category =='Special Occasions':
          selected_option= st.selectbox(
                  label= 'Special Occasions',
                  options=[
          "Birthdays", "Anniversaries", "Weddings", "Engagements", "Graduations",
          "Retirements", "New jobs or promotions", "Housewarmings", "Baby showers",
          "Baptisms or Christenings", "Bar or Bat Mitzvahs", "Confirmations",
      ]
          )
  
      elif category =='Sentiments and Emotions':
          selected_option= st.selectbox(
                  label= 'Sentiments and Emotions',
                  options= [
          "Thank you", "Congratulations", "Sympathy or Condolences", "Get well soon",
          "Apologies", "Thinking of you", "Missing you", "Love and romance",
          "Friendship", "Encouragement", "Empathy", "Good luck", "Farewell or goodbye"
      ]
          )
      elif category =='Specific Achievements':
          selected_option= st.selectbox(
                  label= 'Specific Achievements',
                  options= [
          "Academic achievements", "Sporting achievements", "Personal milestones",
          "Professional milestones", "Recovery from illness", "Sobriety milestones"
      ]
          )
      elif category =='Seasonal':
          selected_option= st.selectbox(
              label='Seasonal',
              options= [
          "Spring", "Summer", "Autumn", "Winter greetings", "Daylight Saving Time reminders"
      ]
          )
      elif category == 'Invitations':
          selected_option= st.selectbox(
              label= 'Invitations',
              options= [
          "Parties", "Weddings", "Baby showers", "Bachelor/Bachelorette parties",
          "Business events", "Ceremonies", "Family reunions"
      ]
          )
          # Define a function to display the selected options
      def display_selections(category, selected_option):
          st.write(f"You have choosen the following: {selected_option} within the {category} category")
  
      # Button to confirm all selections
      if st.button("Lock in Answers"):
          display_selections(category, selected_option)
else: 
  st.write("a")
