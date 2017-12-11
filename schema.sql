drop table if exists twitter_stats;
create table twitter_stats (
id integer primary key autoincrement,
time text not null,
username text not null,
follower_count text not null,
status_count text not nulls
);