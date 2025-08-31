FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --production --silent
COPY . .
CMD ["npm", "run", "dev"]
