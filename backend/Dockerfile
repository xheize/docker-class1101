FROM node:18.6-alpine

EXPOSE 5000

WORKDIR /app

COPY ./package.json ./package.json

RUN npm install

COPY . .

CMD ["node", "app.js"]