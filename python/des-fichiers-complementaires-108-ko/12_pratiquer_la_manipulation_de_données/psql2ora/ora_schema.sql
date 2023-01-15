DROP TABLE worklog;
CREATE TABLE worklog (
  id number(18,0) NOT NULL,
  issueid number(18,0),
  author varchar2(255),
  grouplevel varchar2(255),
  rolelevel number(18,0),
  worklogbody clob,
  created timestamp ,
  updateauthor varchar2(255),
  updated timestamp ,
  startdate timestamp ,
  timeworked number(18,0)
);

ALTER TABLE worklog ADD ( CONSTRAINT wl_id PRIMARY KEY (id));
exit


