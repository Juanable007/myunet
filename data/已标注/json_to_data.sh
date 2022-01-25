#!/bin/sh
for i in *.json
  do
      labelme_json_to_dataset "$i"
done

