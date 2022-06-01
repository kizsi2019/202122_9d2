CREATE TABLE futok (
  fid int NOT NULL,
  fnev varchar(17) NOT NULL,
  szulev int NOT NULL,
  szulho int NOT NULL,
  csapat int NOT NULL,
  ffi bit NOT NULL,
  CONSTRAINT pk_futok PRIMARY KEY (fid)
);

CREATE TABLE eredmenyek (
  futo int,
  kor int NOT NULL,
  ido int NOT NULL,
  CONSTRAINT pk_eredmenyek PRIMARY KEY (futo, kor),
  CONSTRAINT fk_futoeredmenyek FOREIGN KEY (futo) REFERENCES futok(fid)
);

