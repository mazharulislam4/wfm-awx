FROM python:3.13.7-slim

WORKDIR /app
COPY requirements.txt .
# install uv 
RUN pip install uv
RUN uv pip install --system -r requirements.txt

COPY . .
EXPOSE 8070
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8070"]