## Chameleon - boost retrieval accuracy on structured data

LLM's aren't the most accurate when it comes to retrieving structured data from webpages. We're improving government websites so they are.

## Features

CodeGen w/ LLM Agents using Groq & OpenAI:
* Semantic HTML
* Microdata Schema Markup
* ARIA Text


## Installation

Install using:
`pip install dsrag groq langchain_groq crewai crewai[tools]`

## Usage

Run `assistant.py`

## Examples

**Thought:** To add semantic HTML to the provided code, I need to understand what elements I can use to improve the semantic meaning of the HTML. I can use the RAG Tool for Semantic HTML Knowledge Base to find out.

**Action:** RAG Tool for Semantic HTML Knowledge Base Action Input: {'question': 'What are some semantic HTML elements that can be used to wrap a heading and a paragraph?'}

**Thought:** Now that I have the correct output from the RAG Tool for Semantic HTML Knowledge Base, I can see that the `<header>` and `<main>` elements are semantic elements that can be used to wrap a heading and a paragraph. I will now proceed to modify the provided code with these elements.

**Action:** None Action Input: None

**Final Answer:** The semantic HTML elements for the provided code could be:
```<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "headline": "My First Heading",
    "description": "My first paragraph.",
    "author": {
      "@type": "Person",
      "name": "Your Name"
    }
  }
  </script>
  <title>My First Web Page</title>
</head>
<body>

<header>
  <h1>My First Heading</h1>
</header>

<main>
  <article>
    <p>My first paragraph.</p>
  </article>
</main>

<footer>
  <p>&copy; 2024 Your Name. All rights reserved.</p>
</footer>

</body>
</html>

```

![image](https://github.com/user-attachments/assets/d337d227-9701-49ec-abec-26267398d27a)

