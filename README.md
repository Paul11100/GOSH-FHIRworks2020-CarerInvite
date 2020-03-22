#Project Description:
This is a project I made for UCL FHIR Hack, related to my Systems Engineering module project CarerCare, which is an app that intends to help Carers stay connected with their friends, and stay physically active. 

This API is intended for use of a Carer support organization, filtering by age range, using their records to quickly generate personalized messages, and the relevant contact number. 

Start by activating virtual environment:
1. `source env/bin/activate`

To Run Demo:
1. Make sure FHIR record is running, instructions here: https://github.com/goshdrive/FHIRworks_2020
2. Run this API with: `python server.py`
3. Run the demo with: `python demo.py`
4. Modify demo.py parameter values as you like

API Parameters Explained:
- limit: How many patients you want to return (Integer)
- lower: The lower age bound (Integer)
- upper: The upper age bound (Integer)
- name: The sender name (String)
- ref: The sender reference (String)
- url: The link to the carer app (String)

Running Pip Commands: 
- `python -m pip <commands>`