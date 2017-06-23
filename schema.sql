drop table if exists news;
create table entries(
    id integer primary key autoincrement,
    title string not null,
    content string not null,
    auto string not null
    create_date string not null,
)