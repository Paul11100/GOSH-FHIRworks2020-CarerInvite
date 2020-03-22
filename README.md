Start by activating virtual environment:
1. `source env/bin/activate`

To Run Demo:
1. Make sure FHIR record is running
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




