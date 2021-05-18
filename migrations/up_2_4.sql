START TRANSACTION;

CREATE TABLE tasks ( 
    id_task         serial,
    ftask           varchar(256),
    fdescription    varchar(999),
    fdata           timestamp not NULL,
    fparent         integer,
    fcompleted      timestamp,
    CONSTRAINT      pk_task PRIMARY KEY(id_task)
);

CREATE TABLE remainders (
    id_remainder     serial,
    ftask	      integer REFERENCES tasks not NULL,
    fmessage         varchar(999),
    fdata_remainder  timestamp not NULL,
    CONSTRAINT       pk_remainder PRIMARY KEY(id_remainder)
);


INSERT INTO db_version(fversion, fdate, fdescription)
    values('2.4',
           CURRENT_TIMESTAMP,
           'add tables: tasks, remainders');

COMMIT TRANSACTION;
