# Midchat Backend


## Introduction
Midchat  is based on chatgpt-document-retrieval plugine. The system architecture of Midchat included a backend service responsible for handling data-related operations such as data insertion , retrieval , deletion and update. The backend is  based on OpenAI's Document Retrieval project and is built using the FastAPI framework. FastAPI is a modern, high-performance Python web framework for quickly building APIs. It offers automatic API documentation, data validation, and strong type support based on Python's type hints.  The "description_for_model" parameter was set to "Use this tool to get up-to-date information about Midjourney," to enable Midchat to decide when to use the backend services. Bearer Token was used to prevent unauthorized operations. 


### API Endpoints


- Data Insertion (Upsert): Users can upload data via the /upsert and /upsert-file endpoints. This supports not just direct data uploads but also file-based uploads, with additional capabilities for metadata parsing,supports file formats including PDF, Text (plain or markdown), Word document (docx), CSV and PowerPoint presentation (pptx).

- Data Retrieval (Query): The /query endpoint takes in a list of queries with embeddings and filters and returns a list of query results with matching document chunks and scores

- Data Deletion (Delete): The /delete endpoint allows users to remove data either by specific IDs or by applying filter criteria or everything from the index
The entire backend service has been successfully deployed on the DigitalOcean cloud service and is accessible via the endpoint https://starfish-app-fcmbv.ondigitalocean.app/. Through these implementations, we have demonstrated that the system is not only feature-rich but also highly extensible and secure.
