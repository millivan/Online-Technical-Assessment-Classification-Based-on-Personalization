from PIL import Image
import pickle
import streamlit as st


st.set_page_config(page_title="Prediction", page_icon="📈")
st.title("Online Technical Assessment Classification Based on Your Personalization")
gbc_pickle = open('./models/gbc2.sav', 'rb')
gbc = pickle.load(gbc_pickle)

st.markdown("""
            This form contains 7 sections
            - Demographics
            - Personal Preferences and Challenges
            - Preferred Learning Objects
            - Preferred Online Instructional Strategies
            - Preferred Online Instructional Strategies (Exclusively for Technical/ Coding Subjects)
            - Understanding of Learning Styles
            - Learning Style Test
            
            By completing the form and pressing the **Predict** button, you are able to identify which type(s) of online assessment is/are suitable for you to use in technical subjects like programming. 
            """)


st.header("Demographics")
gender = st.radio("Gender", ["Male", "Female"], index=None)
study_level = st.radio("Level of Study (If not in selection, choose the closest one)", ["Diploma", "Undergraduate", "Postgraduate"], index=None)
study_field = st.radio("Field of Study (If not in selection, choose the closest one)", ["Computer Science/ Information Technology", "Engineering (any)", "Medical Laboratory Technology"], index=None)
household_income = st.radio("Household Income", ["< RM 4,849", "RM 4,850 - RM 10,959", "> RM 10,960"], index=None)

st.header("Personal Preferences and Challenges")
pref_learning_mode = st.multiselect("Preferred Learning Mode", ["Face to Face", "Synchronous Online Learning (Real Time)", "Asynchronous Online Learning (On your own time)"])
pref_socmed = st.multiselect("Preferred Social Media Platform", ["WhatsApp", "Online Conference Platforms (e.g. Zoom)", "Blog Website (e.g. Reddit)", "Facebook", "TikTok", "YouTube", "Twitter", "Google Classroom", "Instagram", "Microsoft Teams"])
pref_comms = st.multiselect("Preferred Communication Platform", ["Telegram", "WhatsApp", "Microsoft Teams", "Google Classroom", "Call", "Email", "Online Conference Platforms (e.g. Zoom)", "University eLearning Chat Room"])
elearning_difficulties = st.multiselect("Difficulties in Online Learning", ["Accessibility", "Quality of Material", "Adaptability", "Health Issues", "Focus/ Commitment", "Time Management", "Cost", "Technical Issues", "Engagement", "Self-Motivation", "None"])

st.header("Preferred Learning Objects")
scale = ["Not at All", "Not Really", "Undecided", "Somewhat", "Very Much"]
slides = st.radio("Slide Presentation", scale, index=None)
books = st.radio("Book", scale, index=None)
notes = st.radio("Lecture Notes", scale, index=None)
edu_games = st.radio("Educational Games", scale, index=None)
video = st.radio("Video", scale, index=None)
audio_rec_lect = st.radio("Audio-recorded Lecture", scale, index=None)
animated_instruction = st.radio("Animated Instructions", scale, index=None)
real_obj_model = st.radio("Real Object Model", scale, index=None)
mind_map = st.radio("Mind Map", scale, index=None)
multimedia_content = st.radio("Multimedia Content", scale, index=None)
interactive_tool = st.radio("Interactive Tool", scale, index=None)
tech_supported_learning = st.radio("Technology-supported learning (including computer-based training systems)", scale, index=None)
intelligent_comp_instruction_systems = st.radio("Intelligent computer-aided instruction systems", scale, index=None)

st.header("Preferred Online Instructional Strategies")
live_lect = st.radio("Live Lecture", scale, index=None)
pre_rec_lect = st.radio("Pre-recorded Lecture", scale, index=None)
pre_rec_slide = st.radio("Pre-recorded Slide Lecture", scale, index=None)
demo = st.radio("Demonstration", scale, index=None)
simul = st.radio("Simulation", scale, index=None)
guided_learning = st.radio("Guided Learning (Hands on)", scale, index=None)
lab = st.radio("Digital Lab Experiments", scale, index=None)
grp_discuss = st.radio("Live Group Discussions", scale, index=None)
forum = st.radio("Forum", scale, index=None)
games = st.radio("Games", scale, index=None)
journaling = st.radio("Journaling", scale, index=None)
youtube = st.radio("YouTube Video", scale, index=None)
video_feedback = st.radio("Video-based Feedback", scale, index=None)
live_chat = st.radio("Live Chat", scale, index=None)
brainstorm = st.radio("Brainstorming", scale, index=None)
debate = st.radio("Online Debate", scale, index=None)
blog = st.radio("Blog Writing", scale, index=None)
pbl = st.radio("Problem Based Learning", scale, index=None)
internet = st.radio("Internet Research", scale, index=None)
guest_online_lect = st.radio("Invited Guest Online Lecture", scale, index=None)
virtual_field_trip = st.radio("Virtual Field Trip", scale, index=None)
exit_tickets = st.radio("Exit Tickets (End Class Feedback)", scale, index=None)
learning_reflection = st.radio("Learning Reflection", scale, index=None)
online_exercise = st.radio("Online Exercise/ Practice", scale, index=None)
procedural_demo = st.radio("Procedural Demonstration (Perform a given action)", scale, index=None)
concept_mapping = st.radio("Concept Mapping", scale, index=None)
doc_analysis = st.radio("Document Analysis", scale, index=None)
debug = st.radio("Debugging", scale, index=None)
review = st.radio("Review (Article, Play, Movie, Audio, Book, etc.)", scale, index=None)

st.subheader("Preferred Online Instructional Strategies (Exclusively for Technical/ Coding Subjects)")
tech_sub_pref = st.multiselect("Online Technical Instructional Strategies", ["YouTube Video", "Live Lecture", "Pre-recorded Lecture", "Others"])


st.header("Understanding of Learning Styles")
familiar_ls = st.radio("Are you familiar with the term learning style before this survey?", ["Yes", "No"], index=None)
aware_ls = st.radio("Are you aware what your learning style is?", ["Yes", "No"], index=None)
important_ls = st.radio("Do you think knowing your own learning style is important in improving your learning ability?", ["Yes", "No"], index=None)

st.header("Learning Style Test")
one = st.radio("When operating new equipment for the first time I prefer to", ["Read the instructions", "Listen to or ask for an explaination", 'Have a go and learn by "trial and error"'], index=None)
two = st.radio("When seeking travel directions I", ["Look at a map", "Ask for spoken directions", "Follow my nose or maybe use a compass"], index=None)
three = st.radio("When cooking a new dish I", ["Follow a recipe", "Call a friend for explanation", "Follow my instinct, tasting as I cook"], index=None)
four = st.radio("To teach someone something I", ["Write instructions", "Explain verbally", "Demonstrate and let them have a go"], index=None)
five = st.radio("I tend to say", ["I see what you mean", "I hear what you are saying", "I know how you feel"], index=None)
six = st.radio("I tend to say", ["Show me", "Tell me", "Let me try"], index=None)
seven = st.radio("I tend to say", ["Watch how I do it", "Listen to me explain", "You have a go"], index=None)
eight = st.radio("Complaining about faulty good I tend to", ["Write a letter", "Phone", "Go back to the store, or send the faulty item to the head office"], index=None)
nine = st.radio("I prefer these leisure activities", ["Museums or galleries", "Music or conversation", "Physical activities or making things"], index=None)
ten = st.radio("When shopping I tend to", ["Look and decide", "Discuss with shop staff", "Try on, handle or test"], index=None)
eleven = st.radio("Choosing a holiday, I", ["Read the brochures", "Listen to recommendations", "Imagine the experience"], index=None)
twelve = st.radio("Choosing a new car, I", ["Read the reviews", "Discuss with friends", "Test-drive what you fancy"], index=None)
thirteen = st.radio("Learning a new skill", ["I watch what the teacher is doing", "I talk through with the teacher exactly what I am supposed to do", "I like to give it a try and work it out as I go along by doing it"], index=None)
fourteen = st.radio("Choosing from a restaurant menu", ["I imagine what the food will look like", "I talk through the options in my head", "I imagine what the food will taste like"], index=None)
fifteen = st.radio("When listening to a band", ["I sing along to the lyrics (in my head or out loud)", "I listen to the lyrics and the beats", "I move in time with the music"], index=None)
sixteen = st.radio("When concentrating, I", ["Focus on the words or pictures in front of me", "Discuss the problem and possible solutions in my head", "Move around a lot, fiddle with pens and pencils and touch unrelated things"], index=None)
seventeen = st.radio("I remember things best by", ["Writing notes or keeping printed details", "Saying them aloud or repeating words and key points in my head", "Doing and practicing the activity or imagining it being done"], index=None)
eighteen = st.radio("My first memory is of", ["Looking at something", "Being spoken to", "Doing something"], index=None)
nineteen = st.radio("When anxious, I", ["Visualize the worst case scenarios", "Talk over in my head what worries me most", "Can't sit still, fiddle and move around constantly"], index=None)
twenty = st.radio("I feel especially connected to others because of", ["How they look", "What they say to me", "How they make me"], index=None)
twentyone = st.radio("When I revise for an exam, I", ["Write lots of revision notes", "I talk over my notes, to myself or to other people", "Imagine making the movement or creating the formula"], index=None)
twentytwo = st.radio("When explaining something to someone, I tend to", ["Show them what I mean", "Explain to them in different ways until they understand", "Encourage them to try and talk them through the idea as they try"], index=None)
twentythree = st.radio("My main interests are", ["Photography or watching films or people watching", "Listening to music or listening to the radio or talking to friends", "Physical/sports activities or fine wines, fine foods or dancing"], index=None)
twentyfour = st.radio("Most of my free time is spent", ["Watching television", "Talking to friends", "Doing physical activity or making things"], index=None)
twentyfive = st.radio("When I first contact a new person", ["I arrange a face to face meeting", "I talk to them on the telephone", "I try to get together to share an activity"], index=None)
twentysix = st.radio("I first notice how people", ["Look and dress", "Sound and speak", "Stand and move"], index=None)
twentyseven = st.radio("If I am very angry,", ["I keep replaying in my mind what it is that has upset me", "I shout lots and tell people how I feel", "I stomp about, slam doors and throw things"], index=None)
twentyeight = st.radio("I find it easiest to remember", ["Faces", "Names", "Things I have done"], index=None)
twentynine = st.radio("I think I can tell someone is lying because", ["They avoid looking at you", "Their voice changes", "The vibes I get from them"], index=None)
thirty = st.radio("When I'm meeting with an old friend", ['I say "it\'s great to see you!"', 'I say "it\'s great to hear your voice!"', "I give them a hug or a handshake"], index=None)

if st.button("Predict"):
  gen = {"Female": 0, "Male": 1}.get(gender)
  level = {"Diploma": 0, "Undergraduate": 1, "Postgraduate": 2}.get(study_level)
  field = {"Computer Science/ Information Technology": 0, "Engineering (any)": 1, "Medical Laboratory Technology": 2}.get(study_field)
  income = {"< RM 4,849": 0, "RM 4,850 - RM 10,959": 1, "> RM 10,960": 2}.get(household_income)


  f2f = 0
  sync_learn = 0
  async_learn = 0
  for i in range(len(pref_learning_mode)):
    if pref_learning_mode[i] == "Face to Face":
      f2f = 1
    if pref_learning_mode[i] == "Synchronous Online Learning (Real Time)":
      sync_learn = 1
    if pref_learning_mode[i] == "Asynchronous Online Learning (On your own time)":
      async_learn = 1
      
  wa = 0
  zoom = 0
  blog_website = 0
  fb = 0
  tiktok = 0
  yt_socmed = 0
  twitter = 0
  gc = 0
  ig = 0
  teams = 0
  for i in range(len(pref_socmed)):
    if pref_socmed[i] == "WhatsApp":
      wa = 1
    if pref_socmed[i] == "Online Conference Platforms (e.g. Zoom)":
      zoom = 1
    if pref_socmed[i] == "Blog Website (e.g. Reddit)":
      blog_website = 1
    if pref_socmed[i] == "Facebook":
      fb = 1
    if pref_socmed[i] == "TikTok":
      tiktok = 1
    if pref_socmed[i] == "YouTube":
      yt_socmed = 1
    if pref_socmed[i] == "Twitter":
      twitter = 1
    if pref_socmed[i] == "Google Classroom":
      gc = 1
    if pref_socmed[i] == "Instagram":
      ig = 1
    if pref_socmed[i] == "Microsoft Teams":
      teams = 1
      
  tele = 0
  wa_comms = 0
  teams_comms = 0
  gc_comms = 0
  call = 0
  email = 0
  zoom_comms = 0
  eclass = 0
  for i in range(len(pref_comms)):
    if pref_comms[i] == "Telegram":
      tele = 1
    if pref_comms[i] == "WhatsApp":
      wa_comms = 1
    if pref_comms[i] == "Microsoft Teams":
      teams_comms = 1
    if pref_comms[i] == "Google Classroom":
      gc_comms = 1
    if pref_comms[i] == "Call":
      call = 1
    if pref_comms[i] == "Email":
      email = 1
    if pref_comms[i] == "Online Conference Platforms (e.g. Zoom)":
      zoom_comms = 1
    if pref_comms[i] == "University eLearning Chat Room":
      eclass = 1
    
  acc = 0
  quality = 0
  adapt = 0
  health = 0
  focus = 0
  time = 0
  cost = 0
  tech = 0
  engage = 0
  motivation = 0
  for i in range(len(elearning_difficulties)):
    if elearning_difficulties[i]  == "None":
      acc = 0
      quality = 0
      adapt = 0
      health = 0
      focus = 0
      time = 0
      cost = 0
      tech = 0
      engage = 0
      motivation = 0
      break
    if elearning_difficulties[i] == "Accessibility":
      acc = 1
    if elearning_difficulties[i] == "Quality of Material":
      quality = 1
    if elearning_difficulties[i] == "Adaptability":
      adapt = 1
    if elearning_difficulties[i] == "Health Issues":
      health = 1
    if elearning_difficulties[i] == "Focus/ Commitment":
      focus = 1
    if elearning_difficulties[i] == "Time Management":
      time = 1
    if elearning_difficulties[i] == "Cost":
      cost = 1
    if elearning_difficulties[i] == "Technical Issues":
      tech = 1
    if elearning_difficulties[i] == "Engagement":
      engage = 1
    if elearning_difficulties[i] == "Self-Motivation":
      motivation = 1
      
      

  scales = {"Not at All": 0, "Not Really": 1, "Undecided": 2, "Somewhat": 3, "Very Much": 4}
  sl = scales.get(slides)
  boo = scales.get(books)
  note = scales.get(notes)
  edu = scales.get(edu_games)
  vid = scales.get(video)
  aud = scales.get(audio_rec_lect)
  anim = scales.get(animated_instruction)
  real = scales.get(real_obj_model)
  mind = scales.get(mind_map)
  mult = scales.get(multimedia_content)
  inter = scales.get(interactive_tool)
  tech = scales.get(tech_supported_learning)
  intel = scales.get(intelligent_comp_instruction_systems)
  live = scales.get(live_lect)
  prl = scales.get(pre_rec_lect)
  prs = scales.get(pre_rec_slide)
  dem = scales.get(demo)
  sim = scales.get(simul)
  gl = scales.get(guided_learning)
  la = scales.get(lab)
  gd = scales.get(grp_discuss)
  foru = scales.get(forum)
  gam = scales.get(games)
  jou = scales.get(journaling)
  yt = scales.get(youtube)
  vf = scales.get(video_feedback)
  lc = scales.get(live_chat)
  brain = scales.get(brainstorm)
  deb = scales.get(debate)
  blo = scales.get(blog)
  pb = scales.get(pbl)
  inte = scales.get(internet)
  gol = scales.get(guest_online_lect)
  vft = scales.get(virtual_field_trip)
  et = scales.get(exit_tickets)
  lr = scales.get(learning_reflection)
  oe = scales.get(online_exercise)
  pd = scales.get(procedural_demo)
  cm = scales.get(concept_mapping)
  da = scales.get(doc_analysis)
  debu = scales.get(debug)
  rev = scales.get(review)


  yt_techpref = 0
  live_techpref = 0
  recorded_techpref = 0
  others_techpref = 0
  for i in range(len(tech_sub_pref)):
    if tech_sub_pref[i] == "YouTube Video":
      yt_techpref = 1
    if tech_sub_pref[i] == "Live Lecture":
      live_techpref = 1
    if tech_sub_pref[i] == "Pre-recorded Lecture":
      recorded_techpref = 1
    if tech_sub_pref[i] == "Others":
      others_techpref = 1


  yes_no = {"Yes": 1, "No": 0}
  fl = yes_no.get(familiar_ls)
  al = yes_no.get(aware_ls)
  il = yes_no.get(important_ls)

  ls1 = {"Read the instructions": 2, "Listen to or ask for an explaination": 1, 'Have a go and learn by "trial and error"': 0}.get(one)
  ls2 = {"Look at a map": 2, "Ask for spoken directions": 0, "Follow my nose or maybe use a compass": 1}.get(two)
  ls3 = {"Follow a recipe": 1, "Call a friend for explanation": 0, "Follow my instinct, tasting as I cook": 2}.get(three)
  ls4 = {"Write instructions": 2, "Explain verbally": 1, "Demonstrate and let them have a go": 0}.get(four)
  ls5 = {"I see what you mean": 2, "I hear what you are saying": 0, "I know how you feel": 1}.get(five)
  ls6 = {"Show me": 1, "Tell me": 2, "Let me try": 0}.get(six)
  ls7 = {"Watch how I do it": 1, "Listen to me explain": 0, "You have a go": 2}.get(seven)
  ls8 = {"Write a letter": 2, "Phone": 1, "Go back to the store, or send the faulty item to the head office": 0}.get(eight)
  ls9 = {"Museums or galleries": 0, "Music or conversation": 1, "Physical activities or making things": 2}.get(nine)
  ls10 = {"Look and decide": 1, "Discuss with shop staff": 0, "Try on, handle or test": 2}.get(ten)
  ls11 = {"Read the brochures": 2, "Listen to recommendations": 1, "Imagine the experience": 0}.get(eleven)
  ls12 = {"Read the reviews": 1, "Discuss with friends": 0, "Test-drive what you fancy": 2}.get(twelve)
  ls13 = {"I watch what the teacher is doing": 2, "I talk through with the teacher exactly what I am supposed to do": 1, "I like to give it a try and work it out as I go along by doing it": 0}.get(thirteen)
  ls14 = {"I imagine what the food will look like": 1, "I talk through the options in my head": 2, "I imagine what the food will taste like": 0}.get(fourteen)
  ls15 = {"I sing along to the lyrics (in my head or out loud)": 2, "I listen to the lyrics and the beats": 0, "I move in time with the music": 1}.get(fifteen)
  ls16 = {"Focus on the words or pictures in front of me": 1, "Discuss the problem and possible solutions in my head": 0, "Move around a lot, fiddle with pens and pencils and touch unrelated things": 2}.get(sixteen)
  ls17 = {"Writing notes or keeping printed details": 2, "Saying them aloud or repeating words and key points in my head": 1, "Doing and practicing the activity or imagining it being done": 0}.get(seventeen)
  ls18 = {"Looking at something": 2, "Being spoken to": 0, "Doing something": 1}.get(eighteen)
  ls19 = {"Visualize the worst case scenarios": 2, "Talk over in my head what worries me most": 1, "Can't sit still, fiddle and move around constantly": 0}.get(nineteen)
  ls20 = {"How they look": 0, "What they say to me": 2, "How they make me": 1}.get(twenty)
  ls21 = {"Write lots of revision notes": 2, "I talk over my notes, to myself or to other people": 0, "Imagine making the movement or creating the formula": 1}.get(twentyone)
  ls22 = {"Show them what I mean": 2, "Explain to them in different ways until they understand": 1, "Encourage them to try and talk them through the idea as they try": 0}.get(twentytwo)
  ls23 = {"Photography or watching films or people watching": 1, "Listening to music or listening to the radio or talking to friends": 0, "Physical/sports activities or fine wines, fine foods or dancing": 2}.get(twentythree)
  ls24 = {"Watching television": 2, "Talking to friends": 1, "Doing physical activity or making things": 0}.get(twentyfour)
  ls25 = {"I arrange a face to face meeting": 0, "I talk to them on the telephone": 1, "I try to get together to share an activity": 2}.get(twentyfive)
  ls26 = {"Look and dress": 0, "Sound and speak": 1, "Stand and move": 2}.get(twentysix)
  ls27 = {"I keep replaying in my mind what it is that has upset me": 0, "I shout lots and tell people how I feel": 1, "I stomp about, slam doors and throw things": 2}.get(twentyseven)
  ls28 = {"Faces": 0, "Names": 1, "Things I have done": 2}.get(twentyeight)
  ls29 = {"They avoid looking at you": 2, "Their voice changes": 1, "The vibes I get from them": 0}.get(twentynine)
  ls30 = {'I say "it\'s great to see you!"': 2, 'I say "it\'s great to hear your voice!"': 1, "I give them a hug or a handshake": 0}.get(thirty)


  def detDominantVAK(responses):
    visual_keywords = ["Read the instructions", 
                    "Look at a map", 
                    "Follow a recipe", 
                    "Write Instructions",
                    "I see what you mean",
                    "Show me",
                    "Watch how I do it",
                    "Write a letter",
                    "Museums or galleries",
                    "Look and decide",
                    "Read the brochures",
                    "Read the reviews",
                    "I watch what the teacher is doing",
                    "I imagine what the food will look like",
                    "I sing along to the lyrics (in my head or out loud)",
                    "Focus on the words or pictures in front of me",
                    "Writing notes or keeping printed details",
                    "Looking at something",
                    "Visualize the worst case scenarios",
                    "How they look",
                    "Write lots of revision notes",
                    "Show them what I mean",
                    "Photography or watching films or people watching",
                    "Watching television",
                    "I arrange a face to face meeting",
                    "Look and dress",
                    "I keep replaying in my mind what it is that has upset me",
                    "Faces",
                    "They avoid looking at you",
                    "I say \"it's great to see you!\"",
                    ]
    auditory_keywords = ["Listen to or ask for an explaination", 
                        "Ask for spoken directions", 
                        "Call a friend for explaination",
                        "Explain verbally",
                        "I hear what you are saying",
                        "Tell me",
                        "Listen to me explain",
                        "Phone",
                        "Music or conversation",
                        "Discuss with shop staff",
                        "Listen to recommendations",
                        "Discuss with friends",
                        "I talk through with the teacher exactly what I am supposed to do",
                        "I talk through the options in my head",
                        "I listen to the lyrics and the beats",
                        "Discuss the problem and possible solutions in my head",
                        "Saying them aloud or repeating words and key points in my head",
                        "Being spoken to",
                        "Talk over in my head what worries me most",
                        "What they say to me",
                        "I talk over my notes, to myself or to other people",
                        "Explain to them in different ways until they understand",
                        "Listening to music or listening to the radio or talking to friends",
                        "Talking to friends",
                        "I talk to them on the telephone",
                        "Sound and speak",
                        "I shout lots and tell people how I feel",
                        "Names",
                        "Their voice changes",
                        "I say \"it's great to hear your voice!\""
                        ]
    kinesthetic_keywords = ["Have a go and learn by \"trial and error\"", 
                          "Follow my nose or maybe use a compass", 
                          "Follow my instinct, tasting as I cook",
                          "Demonstrate and let them have a go",
                          "I know how you feel",
                          "Let me try",
                          "You have a go",
                          "Go back to the store, or send the faulty item to the head office",
                          "Physical activities or making things",
                          "Try on, handle or test",
                          "Imagine the experience",
                          "Test-drive what you fancy",
                          "I like to give it a try and work it out as I go along by doing it",
                          "I imagine what  the food will taste like", #double spacing here
                          "I move in time with the music",
                          "Move around a lot, fiddle with pens and pencils and touch unrelated things",
                          "Doing and practicing the activity or imagining it being done",
                          "Doing something",
                          "Can't sit still, fiddle and move around constantly",
                          "How they make me",
                          "Imagine making the movement or creating the formula",
                          "Encourage them to try and talk them through the idea as they try",
                          "Physical/sports activities or fine wines, fine foods or dancing",
                          "Doing physical activity or making things",
                          "I try to get together to share an activity",
                          "Stand and move",
                          "I stomp about, slam doors and throw things",
                          "Things I have done",
                          "The vibes I get from them",
                          "I give them a hug or a handshake"
                        ]

    visual_count = 0
    auditory_count = 0
    kinesthetic_count = 0

    for response in responses:
      response = response.lower()
      for keyword in visual_keywords:
        if keyword.lower() in response:
          visual_count += 1
      for keyword in auditory_keywords:
        if keyword.lower() in response:
          auditory_count += 1
      for keyword in kinesthetic_keywords:
        if keyword.lower() in response:
          kinesthetic_count += 1

    dominant_VAK = 0
    if (visual_count > auditory_count and visual_count > kinesthetic_count):
      dominant_VAK = 2
    elif kinesthetic_count > auditory_count:
      dominant_VAK = 1
    else:
      dominant_VAK = 0
    
    return dominant_VAK

  responses = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty]
  dominant_VAK = detDominantVAK(responses)

  demographics = [gen, level, field, income]
  learning_objects = [sl, boo, note, edu, vid, aud, anim, real, mind, mult, inter, tech, intel]
  learning_styles = [ls1, ls2, ls3, ls4, ls5, ls6, ls7, ls8, ls9, ls10, ls11, ls12, ls13, ls14, ls15, ls16, ls17, ls18, ls19, ls20, ls21, ls22, ls23, ls24, ls25, ls26, ls27, ls28, ls29, ls30, dominant_VAK]
  instructional = [live, prl, prs, dem, sim, gl, la, gd, foru, gam, jou, yt, vf, lc, brain, deb, blo, pb, inte, gol, vft, et, lr, oe, pd, cm, da, debu, rev]
  socmed = [fb, gc, wa, teams, ig, yt_socmed, zoom, blog_website, twitter, tiktok]
  comms = [call, gc_comms, teams_comms, wa_comms, eclass, zoom_comms, tele, email]
  diff = [time, tech, quality, acc, adapt, focus, motivation, cost, health, engage]
  tech_pref = [yt_techpref, live_techpref, recorded_techpref, others_techpref]
  understanding = [fl, al, il]
  learn_mode = [sync_learn, f2f, async_learn]
  user_input = []
  user_input.extend(demographics)
  user_input.extend(learning_objects)
  user_input.extend(instructional)
  user_input.extend(understanding)
  user_input.extend(learning_styles)
  user_input.extend(learn_mode)
  user_input.extend(socmed)
  user_input.extend(comms)
  user_input.extend(diff)
  user_input.extend(tech_pref)
  
  # st.write(user_input)
  
  new_prediction = gbc.predict([user_input])
  output = ["Written Assignment", "Case Study", "Real Time Online Exam", "Individual Project/ Assignment", "Group Project/ Assignment", "Online Quiz/ Test - MCQ", "Online Quiz/ Test - Essay", "Online Quiz/ Test - Open Book", "Peer Review Assessment Live Presentation", "Recorded Presentation", "Portfolio"]
  
  # st.write(new_prediction)    
  results = new_prediction[0]
  # results = [0]
  
  st.subheader("Results:")
  if 1 not in results:
    st.write("Unfortunately, we cannot predict a suitable online technical assessment for you :(")
  
  
  else:
    st.markdown("#### These are your results")
    results_index = [i for i in range(len(output)) if results[i] == 1]
    results_name = [output[i] for i in range(len(results_index))]
    # results_name = output
    # st.write(results_name)
    if "Written Assignment" in results_name:
      st.write("Written Assignment")
      wa_pic = Image.open("./pic/wa_pic.jpg")
      st.image(wa_pic, width=500)
      st.markdown('##')
      
    if "Case Study" in results_name:
      st.write("Case Study")
      cs_pic = Image.open("./pic/cs_pic.jpg")
      st.image(cs_pic, width=500)
      st.markdown('##')
      
    if "Real Time Online Exam" in results_name:
      st.write("Real Time Online Exam")
      rtoe_pic = Image.open("./pic/rtoe_pic.jpg")
      st.image(rtoe_pic, width=500)
      st.markdown('##')
      
    if "Individual Project/ Assignment" in results_name:
      st.write("Individual Project/ Assignment")
      ind_pic = Image.open("./pic/ind_pic.jpg")
      st.image(ind_pic, width=500)
      st.markdown('##')
      
    if "Group Project/ Assignment" in results_name:
      st.write("Group Project/ Assignment")
      grp_pic = Image.open("./pic/grp_pic.jpg")
      st.image(grp_pic, width=500)
      st.markdown('##')
      
    if "Online Quiz/ Test - MCQ" in results_name:
      st.write("Online Quiz/ Test - MCQ")
      mcq_pic = Image.open("./pic/mcq_pic.jpg")
      st.image(mcq_pic, width=500)
      st.markdown('##')
      
    if "Online Quiz/ Test - Essay" in results_name:
      st.write("Online Quiz/ Test - Essay")
      essay_pic = Image.open("./pic/essay_pic.jpg")
      st.image(essay_pic, width=500)
      st.markdown('##')
      
    if "Online Quiz/ Test - Open Book" in results_name:
      st.write("Online Quiz/ Test - Open Book")
      openbook_pic = Image.open("./pic/openbook_pic.jpg")
      st.image(openbook_pic, width=500)
      st.markdown('##')
      
    if "Peer Review Assessment Live Presentation" in results_name:
      st.write("Peer Review Assessment Live Presentation")
      live_pic = Image.open("./pic/live_pic.jpg")
      st.image(live_pic, width=500)
      st.markdown('##')
      
    if "Recorded Presentation" in results_name:
      st.write("Recorded Presentation")
      rec_pic = Image.open("./pic/rec_pic.jpg")
      st.image(rec_pic, width=500)
      st.markdown('##')
      
    if "Portfolio" in results_name:
      st.write("Portfolio")
      portfolio_pic = Image.open("./pic/portfolio.png")
      st.image(portfolio_pic, width=500)
      st.markdown('##')
      