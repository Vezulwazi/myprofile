Researcher Profile Page
This Streamlit application allows users to view and manage a researcher's profile, including their research field, publications, and trends related to those publications. The app also provides functionality to filter publications by keyword and visualize publication trends based on year.

Features
Researcher Overview: Displays the researcher's name, field of research, and institution.
Publications Upload: Allows users to upload a CSV file containing the researcher's publications.
Publication Filtering: Users can filter publications by a keyword to find relevant articles.
Publication Trends Visualization: Visualizes publication trends over time by displaying a bar chart of publication counts by year.
Contact Information: Displays the researcher's email for contact.
Prerequisites
Python 3.7+
Streamlit
Pandas
Installation
Clone the repository or download the script.

Install the required libraries:

bash
Copy
pip install streamlit pandas
How to Use
Start the Streamlit app by running the following command in your terminal:
bash
Copy
streamlit run app.py
The application will open in your web browser.

Upload a CSV file containing your publications. The CSV should have the following columns:

Title: The title of the publication.
Year: The year of publication.
Additional columns are optional but will be displayed if included.
Filter the publications by entering a keyword in the "Filter by keyword" text input field.

View the publication trends over time, represented as a bar chart based on the "Year" column in the uploaded CSV.

Contact the researcher via the displayed email for further inquiries.

Example CSV Format
The CSV file should look something like this:

csv
Copy
Title,Year,Journal
"AI for Healthcare",2022,Journal of AI Research
"Machine Learning in Education",2021,Education AI Journal
Contact
For any inquiries, you can contact Denzel Muwanazi via email: denzel.muwanazi@gmail.com.

