FROM python:3.9-slim

WORKDIR /app

# התקנת Flask
RUN pip install flask

# העתקת הקוד פנימה
COPY app.py .

# הפעלת השרת
CMD ["python", "app.py"]