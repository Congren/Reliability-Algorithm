#change directory to your working directory
copy public.articles (title, date, source, description, emotional, political, consensus, author, pic, created_at, updated_at) 
FROM '/Users/natalyabuchwald/Downloads/Filter/outputespn.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
copy public.articles (title, date, source, description, emotional, political, consensus, author, pic, created_at, updated_at) 
FROM '/Users/natalyabuchwald/Downloads/Filter/outputhuffingtonpost.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
copy public.articles (title, date, source, description, emotional, political, consensus, author, pic, created_at, updated_at) 
FROM '/Users/natalyabuchwald/Downloads/Filter/outputbbc.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';
copy public.articles (title, date, source, description, emotional, political, consensus, author, pic, created_at, updated_at) 
FROM '/Users/natalyabuchwald/Downloads/Filter/outputnypost.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

