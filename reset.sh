#!/bin/bash

# We delete the current database 
rm ./db.sqlite3

# We delete all the migrations made in the database
rm -R blogengine/migrations

# We delete all the changes in the repo
git reset --hard
