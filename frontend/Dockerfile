FROM node:18.6-buster

EXPOSE 3000

WORKDIR /app

COPY ./ ./

RUN npm install

RUN npm run build

CMD ["npm","run","start"]