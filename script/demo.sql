select date, trans_id, user_id, fee
from duokan.sale_trans_data
where date=20170801


select date, user_id,
       sum(fee) as sum,
       count(trans_id) as cnt
 from duokan.sale_trans_data 
where date=20170801 
    and type!=8 and type!=13 and type!=0 
    and payment_name not in ('COUPON', 'MIPAYSANDBOX', 'CHAPTER') 
group by date, user_id

select distinct date, trans_id, user_id, fee, cast(COALESCE(get_json_object(extra, '$.deduction'), 0) as int) as de
from duokan.sale_trans_data
where date>=20170320 and date<=20170701
   and payment_name not in ('COUPON', 'MIPAYSANDBOX', 'MIPAYSANDBOX_WEB', 'BC_SANDBOX', 'DC_SANDBOX', 'CHAPTER')
and type!=8 and type!=13 and type!=0


select  date,   
        count(user_id) as pv,            -- 消费人次 
        count(distinct user_id) as uv,   -- 消费人数      
        sum(fee) as sum                  -- 消费金额 
from duokan.sale_trans_data
 where date=20170801 
      and type!=8 and type!=13 and type!=0 
      and payment_name not in ('COUPON', 'MIPAYSANDBOX', 'CHAPTER') 
group by date



select  date,
        count(user_id) as user_cnt,            -- 消费人次
        count(distinct user_id) as user_cnt,   -- 消费人数
        sum(fee) as sum                        -- 消费金额
from duokan.sale_trans_data
 where date=20170801 
    and type!=8 and type!=13 and type!=0 
    and payment_name not in ('COUPON', 'MIPAYSANDBOX', ‘CHAPTER') group by date, user_id
group by date


[WITH CommonTableExpression (, CommonTableExpression)*]   
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
  FROM table_reference
  [WHERE where_condition]
  [GROUP BY col_list]
  [ORDER BY col_list]
  [LIMIT [offset,] rows]


select date, trans_id, user_id, fee
from duokan.sale_trans_data
where date=20170801
      and type!=8 and type!=13 and type!=0
      and payment_name not in ('COUPON', 'MIPAYSANDBOX', 'CHAPTER')

select date, trans_id, user_id, fee from duokan.sale_trans_data
 where date=20170801 
      and type!=8 and type!=13 and type!=0 
      and payment_name not in ('COUPON', 'MIPAYSANDBOX', ‘CHAPTER')
order by fee desc


select date,  count(user_id) as,
sum(fee) as sum, count(trans_id) as cnt
from duokan.sale_trans_data where date=20170801       and type!=8 and type!=13 and type!=0       and payment_name not in ('COUPON', 'MIPAYSANDBOX', ‘CHAPTER') group by date, user_id
