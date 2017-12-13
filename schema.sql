
drop table if exists twitter_stats;
create table twitter_stats (
	id integer primary key autoincrement,
	time text not null,
	username text not null,
	following_count text not null,
	follower_count text not null,
	status_count text not null,
	new_followers text not null
);
