FROM ubuntu-python2-7
ADD . /app_prompt
RUN pip install -r /app_prompt/requirements.txt
COPY runserver.sh /runserver.sh
CMD ["/runserver.sh"]
EXPOSE 8000
