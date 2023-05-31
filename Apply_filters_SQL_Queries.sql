SELECT 
    *
FROM
    log_in_attemps
WHERE
    login_time > '18:00' AND success = FALSE;
    
SELECT 
    *
FROM
    log_in_attemps
WHERE
    login_date = '2022-05-09'
        OR login_date = '2022-05-08';

SELECT 
    *
FROM
    log_in_attemps
WHERE
    NOT country LIKE 'MEX%';

SELECT 
    *
FROM
    employees
WHERE
    department = 'Marketing'
        AND office LIKE 'EAST%';

SELECT 
    *
FROM
    employees
WHERE
    department = 'Finance'
        OR department = 'Sales';

SELECT 
    *
FROM
    employees
WHERE
    NOT department = 'Information Technology';