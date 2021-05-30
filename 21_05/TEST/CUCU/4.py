'''
    7 일간 사용이 가능한 장소를 찾아
    대관 비용의 평균을 구하고
    시작날짜, 끝 날짜와 함께 반환해야하는 SQL문제..
    xxxxxxxxxxx
'''
'''
SELECT S.PLACE_ID, min(S.SCHEDULED_AT) as START_AT, max(S.SCHEDULED_AT) as END_AT, sum(S.PRICE) as COST
FROM PLACES as P inner join SCHEDULES as S on P.ID = S.PLACE_ID
group by S.PLACE_ID
'''