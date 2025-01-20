import streamlit as st

# Placeholder function to submit data to an API
def submit_to_api(data):
    # Replace with actual API call logic, e.g., requests.post(url, json=data)
    st.write("Submitting the following data to the API:")
    st.json(data)

# Title
st.title("Prakriti Questionnaire")

# Input fields for patient name and ID
st.write("### Patient Details")
patient_name = st.text_input("Name:", key="patient_name")
patient_id = st.text_input("Patient ID:", key="patient_id")

# Instructions
st.write("""
Answer each question by selecting the options that match your characteristics.  
You can select multiple options if they apply. The table below categorizes each trait into Vata, Pitta, and Kapha doshas.
""")

# All questions from the PDF
questions = [
    # MENTAL DOSHA
    {"question": "Performs Activities", "options": ["Very Rapidly", "With Moderate Speed", "Slowly"]},
    {"question": "Moods", "options": ["Change Quickly", "Change Quickly and Intense", "Non-changing and Steady"]},
    {"question": "Memory", "options": ["Good – Short Term", "Medium", "Good – Long Term"]},
    {"question": "Appetite", "options": ["Variable, Can Skip Meals Sometimes", "Strong Consistent Appetite", "Usually Mild, Can Skip Meals Without Discomfort"]},
    {"question": "Taste Preferences", "options": ["Sweet, Sour and Salty", "Sweet, Bitter and Astringent", "Pungent, Bitter and Astringent"]},
    {"question": "Frequency of Bowel Movements", "options": ["Irregularly", "Two or More Times Per Day", "Regularly"]},
    {"question": "Consistency of Faeces", "options": ["Hard, Dry Stool", "Loose Stool, Soft Stool", "Well Formed"]},
    {"question": "Perspiration", "options": ["Moderate", "Profuse with Body Odour", "Slight"]},
    {"question": "Sexual Desire", "options": ["Small", "Small to Moderate", "Abundant"]},
    {"question": "Amount of Sleep", "options": ["Usually 5-6 Hours", "Usually 6-8 Hours", "Usually 8 Hours or More"]},
    {"question": "Quality of Sleep", "options": ["Light, Easily Interrupted", "Deep and Uninterrupted", "Deep and Heavy"]},
    {"question": "Type of Dreams", "options": ["Fear, Flying, Running, Jumping, Climbing Trees and Mountains", "Anger, Violence, Struggle, War, Fire, Lightning, The Sun, Gold and Light", "Water, Lakes, Rivers, Oceans, Clouds, Swans, Flowers, and Romance"]},
    {"question": "Response to Challenge", "options": ["Uncertain, Indecisive, Worried", "Angered, Impatient, Irritable", "Clear, Stable, Patient"]},
    {"question": "Speech", "options": ["Fast, Omitting Words and Digressing", "Fast, Clear and Precise", "Slow, Clear and Sweet"]},
    {"question": "Gait", "options": ["Fast with Light Step", "Medium Speed with Precise, Determined Step", "Slow, Steady and Fluid"]},
    # BODY TYPE
    {"question": "Shape of Face", "options": ["Thin and Bony", "Oval, Angular", "Round, Full"]},
    {"question": "Complexion", "options": ["Dark, Brownish or Black", "Fair, Reddish", "Light, Clear and Whitish"]},
    {"question": "Involuntary Body Movements", "options": ["Twitching, Jerking and Fine Tremors", "Body is Usually Still", "Body is Usually Still"]},
    {"question": "Body Weight", "options": ["Light, Five to Ten Pounds Below Normal", "Normal, Medium Weight", "Heavy, Five or More Pounds Above Normal"]},
    {"question": "Build", "options": ["Lean, Thin, Tall or Short", "Medium Build, Medium Height", "Thick, Large, Fleshy or Plump"]},
    {"question": "Texture or Quality of Skin", "options": ["Dry, Coarse, Rough, Cracked or Scaling", "Soft, Delicate and Sensitive with Freckles, Moles", "Soft, Smooth and Oily"]},
    {"question": "Body Temperature", "options": ["Low, Cold Extremities", "High, Always Feels Warm", "Low, Body Feels Cool"]},
    {"question": "Stamina", "options": ["Short", "Moderate", "Strong"]},
    {"question": "Shape and Quality of Eyes and Lashes", "options": ["Small, Bulging and Deep-Set with Thin, Scanty Eye Lashes", "Sharp and Penetrating with Brown, Blonde or Copper Lashes", "Large, Attractive and Full with Long, Thick Lashes"]},
    {"question": "Veins", "options": ["Prominent or Branching, Close to the Surface", "Neither Hidden nor Prominent", "Deep and Hidden"]},
]

# Initialize counters
vata_count = 0
pitta_count = 0
kapha_count = 0

# Data to collect
responses = []

# Display the questionnaire
for i, q in enumerate(questions):
    st.write(f"**Q{i+1}. {q['question']}**")
    
    # Display checkboxes for options
    col1, col2, col3 = st.columns(3)
    with col1:
        vata_selected = st.checkbox(q["options"][0], key=f"vata_q{i}")
    with col2:
        pitta_selected = st.checkbox(q["options"][1], key=f"pitta_q{i}")
    with col3:
        kapha_selected = st.checkbox(q["options"][2], key=f"kapha_q{i}")
    
    # Increment counters based on selections
    if vata_selected:
        vata_count += 1
    if pitta_selected:
        pitta_count += 1
    if kapha_selected:
        kapha_count += 1

    # Collect response data
    responses.append({
        "question": q["question"],
        "vata": vata_selected,
        "pitta": pitta_selected,
        "kapha": kapha_selected
    })
    
    st.write("---")

# Submit button
if st.button("Submit"):
    # Prepare data to send
    data = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "responses": responses,
        "totals": {
            "vata": vata_count,
            "pitta": pitta_count,
            "kapha": kapha_count
        }
    }
    
    # Call the API placeholder function
    submit_to_api(data)
