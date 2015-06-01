create table part (
    p_partkey       integer,
    p_name          varchar(55),
    p_mfgr          char(25),
    p_brand         char(10),
    p_type          varchar(25),
    p_size          integer,
    p_container     char(10),
    p_retailprice   decimal,
    p_comment       varchar(23)
);

create table supplier (
    s_suppkey       integer,
    s_name          char(25),
    s_address       varchar(40),
    s_nationkey     integer not null, -- references n_nationkey
    s_phone         char(15),
    s_acctbal       decimal,
    s_comment       varchar(101)
);

create table orders (
    o_orderkey      integer,
    o_custkey       integer not null, -- references c_custkey
    o_orderstatus   char(1),
    o_totalprice    decimal,
    o_orderdate     date,
    o_orderpriority char(15),
    o_clerk         char(15),
    o_shippriority  integer,
    o_comment       varchar(79)
);
