if [ "$#" -eq  "0" ] ; then
    echo 'Please provide a commit message.'
    exit 1
fi

cd ./assets
npm install

if npm run build; then
  git commit -m "COMPX341-22A-A3 Commiting from CI/CD Pipeline"
else
  echo 'Failed to build, did not commit.'
  exit 1
fi