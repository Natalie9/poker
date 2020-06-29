FROM node:13.12.0-alpine as frontend
WORKDIR /app
COPY package.json /app
RUN npm install --silent
COPY . .
RUN npm run build






