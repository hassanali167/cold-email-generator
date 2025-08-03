import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        """Initialize the Chain class with a language model."""
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-70b-versatile"
        )

    def _invoke_chain(self, prompt_template, **kwargs):
        """Helper method to invoke a chain with the given prompt template and arguments."""
        chain = prompt_template | self.llm
        return chain.invoke(kwargs)

    def extract_jobs(self, cleaned_text):
        """Extract job postings from the given cleaned text."""
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        try:
            res = self._invoke_chain(prompt_extract, page_data=cleaned_text)
            json_parser = JsonOutputParser()
            parsed_res = json_parser.parse(res.content)
            return parsed_res if isinstance(parsed_res, list) else [parsed_res]
        except OutputParserException as e:
            raise OutputParserException(f"Error parsing jobs: {str(e)}")

    def write_mail(self, job, links):
        """Generate a cold email for the given job description and portfolio links."""
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Muhammad Ali, a Chief Executive Officer at Technik Nest. Technik Nest is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Technik Nest 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Technik Nest's portfolio: {link_list}
            Remember you are Muhammad Ali, CEO at Technik Nest. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        res = self._invoke_chain(prompt_email, job_description=str(job), link_list=links)
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))











