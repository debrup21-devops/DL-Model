FROM public.ecr.aws/lambda/python:3.8

RUN python3 -m pip install --upgrade pip
RUN mkdir DL_Model
COPY ./requirements.txt .
COPY ./* ${LAMBDA_TASK_ROOT}/
RUN pwd
RUN ls -l
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD ["lambda-function.lambda_handler"]


