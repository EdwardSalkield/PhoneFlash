#!/bin/bash
(cd client;
echo Building client;
npm run build;
cp -r build /data/build;
echo Successful client build!)

(cd server;
echo Building server;
cp -r * . /data/server
)
