from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here
api_key = "sk-proj-9GLrHcFBfLEiPp7Sn7tFT3BlbkFJHAQv9GtkcblnSBBNnr6F"

# Initialize the OpenAI client with the API key
openai.api_key = api_key

html_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <script async src="https://assets.adobedtm.com/7d6e749d4118/1f2b049df95b/launch-ENdc1ca6bab15e46a5b880a2c3f9d462ab.min.js"></script>
    
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Website",
        "keywords": "US Census Bureau, Census Bureau Data",
        "text": "Census Bureau Data",
        "description": "Explore the thousands of tables we have. Build customized maps from any variable in our data tables. Learn about America's communities through our data profiles. They cover 100,000+ different geographies: states , counties , places , tribal areas , zip codes , and congressional districts. For each, we cover topics like education, employment, health, and housing just to name a few. Get record-level access to our Public Use Microdata Sample (PUMS) files. Check out our help resources, FAQs, quick start guides, and release information.",
        "countryOfOrigin": "United States Of America",
        "creator": {
          "@type": "GovernmentOrganization",
          "name": "United States Census Bureau",
          "email": "census.data@census.gov",
          "address": "4600 Silver Hill Road Washington, DC 20233",
          "department": {
            "@type": "Organization",
            "name": "Research and Methodology",
            "alternateName": "ADRM"
          },
          "logo": "https://www.census.gov/etc.clientlibs/census/clientlibs/census-pattern-library/resources/images/USCENSUS_IDENTITY_SOLO_BLACK_1.5in_R_no_padding.svg",
          "telephone": "301-763-4636",
          "slogan": "Measuring America's People, Places, and Economy",
          "description": "The Census Bureau's mission is to serve as the nation's leading provider of quality data about its people and economy."
        }
      }
    </script>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="initial-scale=1, viewport-fit=cover" />
    <meta name="author" content="U.S. Census Bureau" />
    
    <link rel="icon" href="/favicon.ico" />
    <title>Explore Census Data</title>
    <script type="module" crossorigin src="/assets/index-075a9db4.js"></script>
    <link rel="stylesheet" href="/assets/index-4b718d52.css">
  </head>
  <body>
    <noscript>
      <strong>
        We're sorry but this website doesn't work properly without JavaScript enabled. Please enable
        it to continue.
      </strong>
    </noscript>
    <div id="app"></div>
  </body>
</html>"""
researcher = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts information from HTML. Extract all links and the text content from the provided HTML that a user might want"},
        {"role": "user","content": f"I'm a researcher and academic, I want access to accurate and comprehensive data that supports high-quality research and contributes to academic advancements and policy recommendations. Extract information from the following HTML:\n{html_content}"}
    ]
)

policy = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts information from HTML. Extract all links and the text content from the provided HTML that a user might want"},
        {"role": "user","content": f"I'm a policy maker, I rely on census data to inform policy decisions, allocate resources, and plan public services. Extract information from the following HTML:\n{html_content}"}
    ]
)


businessman = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts information from HTML. Extract all links and the text content from the provided HTML that a user might want"},
        {"role": "user","content": f"I'm a businessman, I rely on census data to analyze market trends, understand consumer demographics, and make informed decisions about product development, marketing, and expansion. I want to grow my business, can you extract information from the following HTML that could be relevant to me:\n{html_content}"}
    ]
)
public = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts information from HTML. Extract all links and the text content from the provided HTML that a user might want"},
        {"role": "user","content": f"I'm a mom of 3. I want to learn about the latest news from census and data that could be relevant to me, can you extract information from the following HTML that could be relevant to me:\n{html_content}"}
    ]
)
print(researcher.choices[0].message['content'])
print(policy.choices[0].message['content'])

print(businessman.choices[0].message['content'])
print(public.choices[0].message['content'])


if __name__ == '__main__':
    app.run(debug=True)
