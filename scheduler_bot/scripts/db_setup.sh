#!/usr/bin/env bash

SCRIPTS_DIR="$(dirname $0)"
SQL_SCRIPTS_DIR="$SCRIPTS_DIR/sql"
psql -U postgres -d postgres -f $SQL_SCRIPTS_DIR/create_database.sql
psql -U postgres -d scheduler_bot -f $SQL_SCRIPTS_DIR/create_events_table.sql