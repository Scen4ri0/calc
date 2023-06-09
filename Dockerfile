FROM python:3

WORKDIR /usr/src/app

COPY calc.py ./ 
	
COPY requirements.txt ./ 

RUN pip install --upgrade pip  

RUN pip install --no-cache-dir -r requirements.txt \
	flask \
	bandit

EXPOSE 8000

CMD ["python", "calc.py"]

