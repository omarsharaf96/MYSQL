DROP TABLE IF EXISTS MAIN_${ENV}.DSS_Township_Counts ;

CREATE TABLE MAIN_${ENV}.DSS_Township_Counts (
    township VARCHAR(50),
    assistance_type VARCHAR(50),
    counts VARCHAR(50)
)  ENGINE=INNODB;