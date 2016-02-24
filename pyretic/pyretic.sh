#!/bin/bash

CURR_DIR=`dirname $0`
PYRETIC_DIR=$HOME/pyretic

if [ -d "$PYRETIC_DIR" ]; then
  echo "pyretic exists"
  exit 0
fi

cd $HOME

echo "1/4 Cloning pyretic from github"
git clone https://github.com/frenetic-lang/pyretic.git
git checkout path_queries

echo "2/4 Soft linking learning switch"
ln -s "${CURR_DIR}/learning-switch.py" "${PYRETIC_DIR}/pyretic/modules/"

echo "3/4 Modifying one line in pyretic"
sed -i -e 's/.\/frenetic/frenetic/g' "${PYRETIC_DIR}/start-frenetic.sh"

echo "4/4 Adding pox to python path if no already"
if [[ ${PYTHONPATH} != *pox* ]]
  then echo "export PYTHONPATH=${PYTHONPATH}:${HOME}/pox/" >> ${HOME}/.bash_profile
fi
