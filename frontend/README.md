# Getting started

## Prerequisites:
 1. Install [Node](https://nodejs.org/)
 2. Install dependencies by running `npm i`
 3. For local development, you need to copy `.env.development.local.template` file to `.env.development.local` and modify `DEV_PROXY` environment variable so that it refers to API host


## Available commands:

### `npm start`

Runs the app in the development mode on 3001 port by default (can be overridden via `PORT` environment variable located in `.env.development.local`).


### `npm run build`

Builds the app for production to the `build` folder.


### `npm run test`

Run tests.


### `npm run test:watch`

Run tests in watch mode.


### `npm run lint`

Run ESLint check.

### `npm run check-ts`

Run TypeScript check.

## Quick start
```bash
docker build -t spotcity/front:latest .

# run standalone
docker run -d -p=80:80 --rm --name spotcity_front spotcity/front:latest

```