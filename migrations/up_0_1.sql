START TRANSACTION;

CREATE TABLE db_version (
	id		serial,
	fversion 	varchar (20),
	fdate 		timestamp not null,
	fdescription	varchar(256),
	CONSTRAINT  id_record_pk PRIMARY KEY(id)
) ;

INSERT INTO db_version(fversion, fdate, fdescription)
	values('0.1',
		CURRENT_TIMESTAMP,
		'base is empty and created control version');

COMMIT TRANSACTION;
