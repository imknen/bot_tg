START TRANSACTION;

DROP TABLE remainders;
DROP TABLE tasks;

INSERT INTO db_version(fversion, fdate, fdescription)
    values('1.2',
    CURRENT_TIMESTAMP,
    'delete tables: remainders, tasks');

COMMIT TRANSACTION;
