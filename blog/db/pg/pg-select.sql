-- insert
INSERT INTO kline_1d (ts, coinbase_id, coinquote_id, exchange_id, quote, open, close, high, low, vol)
VALUES (timestamp with time zone '2018-08-25 +0', 1000, 2392, 4, 1, '12345', '12345', '12345', '12345', '12345')
ON CONFLICT (coinbase_id, coinquote_id, exchange_id, ts)
  DO NOTHING;
-- upsert
INSERT INTO kline_1d (ts, coinbase_id, coinquote_id, exchange_id, quote, open, close, high, low, vol)
VALUES (timestamp with time zone '2018-08-25 +0', 1000, 2392, 4, 1, '12345', '12345', '12345', '12345', '12345')
ON CONFLICT (coinbase_id, coinquote_id, exchange_id, ts)
  DO update
    set quote = 1, open = '12345', close = '12345', high = '12345', low = '12345', vol = '12345';

-- select
SELECT
  time_bucket('1h', ts) at time zone ('-8') AS "period",
  first(open, ts)                           AS "open",
  last(close, ts)                           AS "close",
  max(high)                                 AS "high",
  min(low)                                  AS "low",
  sum(vol) :: numeric(15, 2)                AS "vol"
FROM "kline_1m"
WHERE ("ts" >= '2018-07-20 06:34:25') AND (("coinbase_id" = 1000) AND ("coinquote_id" = 2392) AND ("exchange_id" = 1))
GROUP BY "period"
ORDER BY "period" DESC
LIMIT 240;

show max_locks_per_transaction;
SELECT drop_chunks('2018-09-10' :: timestamptz, 'kline_1m');
