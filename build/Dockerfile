FROM python:3.10.12-slim
COPY ./requirements.txt /tmp/
#RUN pip install numpy
RUN pip install --no-cache-dir -r /tmp/requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
COPY ./check_installation.py /tmp/
RUN python /tmp/check_installation.py
EXPOSE 8888/tcp
WORKDIR /repo
ENTRYPOINT ["jupyter", "lab", "--allow-root", "--ip", "0.0.0.0"]
