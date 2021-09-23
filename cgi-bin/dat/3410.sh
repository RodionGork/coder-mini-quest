#!/usr/bin/env bash

hs=$1

if [[ "$2" -ne "" ]] ; then
  ur=$(($2 % 1000))
else
  ur=0
fi


fnx() {
  echo $(($1 * 137 % 222 + 98))
}

k=$((hs * hs % 219))

if [[ $ur -ne 0 ]] ; then
  y=$(fnx $((hs + 221 - k)))
  if [[ $ur -eq $y ]] ; then
    echo "You have found some matches, let's have some light.:mtcze"
  else
    echo "You haven't found any matches. Try harder."
  fi
  exit 0
fi

echo "Find a match!"

i=0
while [[ $i -lt 222 ]] ; do
  if [[ $i -ne $k ]] ; then
    x=$((hs + i))
  else
    x=$((hs + 221 - k))
  fi
  y=$(fnx x)
  printf "%d" $y
  i=$((i + 1))
  if [[ $((i % 22)) -eq 0 ]] ; then
    echo ""
  else
    printf " "
  fi
done
