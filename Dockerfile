FROM python:3.8

RUN python3 -m pip install --upgrade pip
RUN python3 -m venv venv
COPY ./* ./DL_Model
RUN cd DL_Model
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD ["lambda-function.lambda_handler"]


