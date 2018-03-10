#!/bin/bash
cd client
npm run build
echo Successful build!
cp -r build /data/build
echo Done!
