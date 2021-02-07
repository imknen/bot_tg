BEGIN;

CREATE TABLE users (
    user_id     SERIAL,
    fname       varchar(32),
    ffemale     varchar(32),
    fpatronymic varchar(32),
    f_nick      varchar(32),
    CONSTRAINT  user_pk PRIMARY KEY(user_id)
);

INSERT INTO db_version(fversion, fdate, fdescription)
    values('1.2',
    CURRENT_TIMESTAMP,
    'create table users');
END;
