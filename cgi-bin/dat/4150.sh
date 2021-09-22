#!/usr/bin/bash

hs=$1

ur=$(($2 % 1000))

fnx() {
  echo $(($1 * 137 % 222 + 98))
}

k=$((hs * hs % 219))

if [[ $ur -ne 0 ]] ; then
  echo "You got some water in your pot:wassr"
  exit 0
fi

echo "No challenge here, just answer with any small positive number!"
