-- 开启 EXTENSION
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- 创建表
drop table kline_1m;
create table kline_1m (
  ts         TIMESTAMPTZ NOT NULL,
  coinbase_id  int         NOT NULL,
  coinquote_id int         NOT NULL,
  exchange_id  int         NOT NULL,
  quote        numeric     NOT NULL default 0,
  open         numeric     NOT NULL default 0,
  close        numeric     NOT NULL default 0,
  high         numeric     NOT NULL default 0,
  low          numeric     NOT NULL default 0,
  vol          numeric     NOT NULL default 0
);
-- SELECT create_hypertable('kline_1m', 'ts');
SELECT create_hypertable('kline_1m', 'ts', chunk_time_interval => interval '12 hour');
CREATE UNIQUE INDEX ON kline_1m (coinbase_id, coinquote_id, exchange_id, ts);
CREATE INDEX ON kline_1m (coinbase_id, coinquote_id, exchange_id);
CREATE INDEX ON kline_1m (coinbase_id);
-- CREATE INDEX ON kline_1m (ts desc);
\d kline_1m;

drop table kline_1d;
create table kline_1d (
  ts         TIMESTAMPTZ NOT NULL,
  coinbase_id  int         NOT NULL,
  coinquote_id int         NOT NULL,
  exchange_id  int         NOT NULL,
  quote        numeric     NOT NULL default 0,
  open         numeric     NOT NULL default 0,
  close        numeric     NOT NULL default 0,
  high         numeric     NOT NULL default 0,
  low          numeric     NOT NULL default 0,
  vol          numeric     NOT NULL default 0
);
SELECT create_hypertable('kline_1d', 'ts');
CREATE UNIQUE INDEX ON kline_1d (coinbase_id, coinquote_id, exchange_id, ts);
CREATE INDEX ON kline_1d (coinbase_id, coinquote_id, exchange_id);
-- CREATE INDEX ON kline_1d (ts desc);

\d kline_1m;
\d kline_1d;

SELECT count(*) from kline_1m;
SELECT count(*) from kline_1d;

SELECT * FROM chunk_relation_size_pretty('kline_1m');
SELECT * FROM chunk_relation_size_pretty('kline_1d');
-- SELECT drop_chunks('2018-09-10' :: timestamptz, 'kline_1m');
