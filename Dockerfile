FROM python:3.11-slim
# ensures any python output is sent straight to the terminal 
# i.e the error will go straight to the command line
# we set it to one to send the data straight our way  wihtout storing it 
ENV PYTHONUNBUFFERED=1 
ENV PYTHONDONTWRITEBYTECOD=1
WORKDIR /rihalProject

COPY requirements.txt requirements.txt 

RUN apt-get update && apt-get install -y \
    postgresql-contrib \
    libpq-dev \
    gcc \
    python3-dev

RUN pip3 install -r requirements.txt 

COPY . .

# Run migrations during container build
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate


EXPOSE 8000




# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]