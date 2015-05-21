# change table
for tbl in `psql -qAt -c "select tablename from pg_tables where schemaname = 'public';" dacardio` ; do  psql -c "alter table $tbl owner to dacardio" dacardio ; done
# change sequences
for tbl in `psql -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" dacardio` ; do  psql -c "alter table $tbl owner to dacardio" dacardio ; done
