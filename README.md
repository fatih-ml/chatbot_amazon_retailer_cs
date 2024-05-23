in this project our aim is to build a chatbot for sellers on amazon
the topics are related various issues regarding selling on amazon such as logistics or marketing.

This is not a thorough chatbot, rather an educational study for experimental purposes.

we have visited 15 valuable pages on amazon seller central and took pdf samples of those pages, importantly we have also composed metadata such as titles, subtitles and topics for these pages.

Later, we have used LlamaParse to extract these documents into markdown format, then rearranged metadata and markdown files into a signle json format.

then we have used Llama index VectorStoreIndex to vectorize, cache and index the data for later use in our retrieval queries.

On the other hand, we have used OpenI API for GPT3.5Turbo model for text generation from the retrieved tasks. VectorStoreIndex and OpenAI made very simple to ube used together, thx for this convenience.

finaly we have used streamlit to deploy our study.

we clearly observed that accuracy of the answers are much higher because of adding relevant metadata to the documents.

Thanks for reading and visiting my repo, please dont hesitate to contribute or ask any questions.
