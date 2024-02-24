/***************************************************************************************************
  D. Extract customer and payment raw data needed for the detailed section from source database   
***************************************************************************************************/
-- Source: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table-as/

CREATE TABLE all_customers AS
	SELECT
		cu.customer_id,
		cu.store_id,
		cu.first_name,
		cu.last_name,
		a.address,
		a.address2,
		ci.city,
		a.postal_code,
		co.country,
		p.payment_id,
		p.payment_date,
		p.amount
	FROM customer cu
	INNER JOIN payment p on cu.customer_id = p.customer_id
	INNER JOIN address a on cu.address_id = a.address_id
	INNER JOIN city ci on a.city_id = ci.city_id
	INNER JOIN country co on ci.country_id = co.country_id
	GROUP BY cu.customer_id, cu.store_id, a.address, a.address2, ci.city, a.postal_code, co.country, p.payment_id, p.payment_date, p.amount
	ORDER BY p.payment_date;

-- verify data
SELECT * FROM all_customers; --14,596

/***************************************************************************************************
  B. Code for function(s) in text format that perform the transformation(s) identified in part A4 
***************************************************************************************************/
-- Source: https://www.postgresqltutorial.com/postgresql-plpgsql/postgresql-create-function/
-- CONCAT source: https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-concat-function/

-- function to create address line for customer
CREATE OR REPLACE FUNCTION fn_create_customer_address(address VARCHAR, address2 VARCHAR, city VARCHAR, postal_code VARCHAR, country VARCHAR)
RETURNS VARCHAR
LANGUAGE PLPGSQL
AS
$$
DECLARE 
	customer_address VARCHAR;
BEGIN
	IF LENGTH(address2) > 0 THEN	
		customer_address := address || ', ' || address2 || ', ' || city || ', ' || postal_code || ', ' || country;
	ELSE
		customer_address := address || ', ' || city || ', ' || postal_code || ', ' || country;
	END IF;
	
	RETURN customer_address;
END;
$$

-- function to replace data in raw-data table
CREATE OR REPLACE FUNCTION fn_refresh_all_customers()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS 
$$
BEGIN
	TRUNCATE TABLE all_customers;
	INSERT INTO all_customers
		SELECT
			cu.customer_id,
			cu.store_id,
			cu.first_name,
			cu.last_name,
			a.address,
			a.address2,
			ci.city,
			a.postal_code,
			co.country,
			p.payment_id,
			p.payment_date,
			p.amount
		FROM customer cu
		INNER JOIN payment p on cu.customer_id = p.customer_id
		INNER JOIN address a on cu.address_id = a.address_id
		INNER JOIN city ci on a.city_id = ci.city_id
		INNER JOIN country co on ci.country_id = co.country_id
		GROUP BY cu.customer_id, cu.store_id, a.address, a.address2, ci.city, a.postal_code, co.country, p.payment_id, p.payment_date, p.amount
		ORDER BY p.payment_date;
	RETURN NEW;
END;
$$

-- function to replace data in detailed table
CREATE OR REPLACE FUNCTION fn_refresh_detailed_table()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS 
$$
BEGIN
	TRUNCATE TABLE detailed_table;
	INSERT INTO detailed_table
		SELECT
			store_id,
			customer_id,
			first_name,
			last_name,
			fn_create_customer_address(address, address2, city, postal_code, country) AS Address,
			SUM(amount)::MONEY AS Total_Payments,
			COUNT(payment_id) AS Transactions
		FROM all_customers 
		GROUP BY store_id, customer_id, first_name, last_name, Address, address2, city, postal_code, country
		ORDER BY Total_Payments DESC;
	RETURN NEW;
END;
$$

-- function to replace data in summary table
CREATE OR REPLACE FUNCTION fn_refresh_summary_table()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS 
$$
BEGIN
	TRUNCATE TABLE summary_table;
	INSERT INTO summary_table
		SELECT
			CONCAT(first_name, last_name) AS Customer_Name,
			Total_Payments::MONEY
		FROM detailed_table
		GROUP BY Customer_Name, Total_Payments
		ORDER BY Total_Payments DESC
		LIMIT 10;
	RETURN NEW;
END;
$$

/***************************************************************************************************
  C. Create the detailed and summary tables to hold the report table sections					   
***************************************************************************************************/
-- Source: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table-as/

-- DETAILED
CREATE TABLE detailed_table AS
	SELECT
		store_id,
		customer_id,
		first_name,
		last_name,
		fn_create_customer_address(address, address2, city, postal_code, country) AS Address,
		SUM(amount)::MONEY AS Total_Payments,
		COUNT(payment_id) AS Transactions
	FROM all_customers 
	GROUP BY store_id, customer_id, first_name, last_name, Address, address2, city, postal_code, country
	ORDER BY Total_Payments DESC;

-- verify data
SELECT * FROM detailed_table;

-- SUMMARY
CREATE TABLE summary_table AS
	SELECT
		CONCAT(first_name, last_name) AS Customer_Name,
		Total_Payments::MONEY
	FROM detailed_table
	GROUP BY Customer_Name, Total_Payments
	ORDER BY Total_Payments DESC
	LIMIT 10;

-- verify data
SELECT * from summary_table;

/***************************************************************************************************
E. SQL code that creates a trigger on the detailed table that will continually update the summary table as data is added to the detailed table  										   
***************************************************************************************************/
-- Source: https://www.postgresqltutorial.com/postgresql-triggers/creating-first-trigger-postgresql/

-- trigger for all_customers refresh
CREATE TRIGGER tr_refresh_all_customers
	AFTER INSERT
	ON payment
	FOR EACH STATEMENT
	EXECUTE PROCEDURE fn_refresh_all_customers();

-- trigger for detailed_table refresh
CREATE TRIGGER tr_refresh_detailed_table
	AFTER INSERT
	ON all_customers
	FOR EACH STATEMENT
	EXECUTE PROCEDURE fn_refresh_detailed_table();

-- trigger for summary_table refresh
CREATE TRIGGER tr_refresh_summary_table
	AFTER INSERT
	ON detailed_table
	FOR EACH STATEMENT
	EXECUTE PROCEDURE fn_refresh_summary_table();

/***************************************************************************************************
  F. Code for stored procedure that is used to refresh data in both the detailed and summary tables. The procedure clears the contents of the detailed and summary table, and perform raw data extraction from part D.
***************************************************************************************************/
-- source: https://www.postgresqltutorial.com/postgresql-plpgsql/postgresql-create-procedure/

-- stored procedure to replace data in raw-data table as a transaction
CREATE OR REPLACE PROCEDURE sp_refresh_all_customers()
LANGUAGE plpgsql
AS $$
BEGIN
	-- clear old data
	TRUNCATE TABLE all_customers;
	-- insert new data
	INSERT INTO all_customers
		SELECT
			cu.customer_id,
			cu.store_id,
			cu.first_name,
			cu.last_name,
			a.address,
			a.address2,
			ci.city,
			a.postal_code,
			co.country,
			p.payment_id,
			p.payment_date,
			p.amount
		FROM customer cu
		INNER JOIN payment p on cu.customer_id = p.customer_id
		INNER JOIN address a on cu.address_id = a.address_id
		INNER JOIN city ci on a.city_id = ci.city_id
		INNER JOIN country co on ci.country_id = co.country_id
		GROUP BY cu.customer_id, cu.store_id, a.address, a.address2, ci.city, a.postal_code, co.country, p.payment_id, p.payment_date, p.amount
		ORDER BY p.payment_date;
		
	COMMIT;
END;$$

-- stored procedure to replace data in detailed table as a transaction
CREATE OR REPLACE PROCEDURE sp_refresh_detailed_table()
LANGUAGE plpgsql
AS $$
BEGIN
	-- clear old data
	TRUNCATE TABLE detailed_table;
	-- insert new data
	INSERT INTO detailed_table
		SELECT
			store_id,
			customer_id,
			first_name,
			last_name,
			fn_create_customer_address(address, address2, city, postal_code, country) AS Address,
			SUM(amount)::MONEY AS Total_Payments,
			COUNT(payment_id) AS Transactions
		FROM all_customers 
		GROUP BY store_id, customer_id, first_name, last_name, Address, address2, city, postal_code, country
		ORDER BY Total_Payments DESC;

	COMMIT;
END;$$

-- stored procedure to replace data in summary table as a transaction
CREATE OR REPLACE PROCEDURE sp_refresh_summary_table()
LANGUAGE plpgsql
AS $$
BEGIN
	-- clear old data
	TRUNCATE TABLE summary_table;
	-- insert new data
	INSERT INTO summary_table
		SELECT
			CONCAT(first_name, last_name) AS Customer_Name,
			Total_Payments::MONEY
		FROM detailed_table
		GROUP BY Customer_Name, Total_Payments
		ORDER BY Total_Payments DESC
		LIMIT 10;	

	COMMIT;
END;$$

-- stored procedure calls
CALL sp_refresh_all_customers();
CALL sp_refresh_detailed_table();
CALL sp_refresh_summary_table();

-- clean up
DROP TABLE all_customers;
DROP TABLE detailed_table;
DROP TABLE summary_table;

DROP TRIGGER tr_refresh_all_customers;
DROP TRIGGER tr_refresh_detailed_table;
DROP TRIGGER tr_refresh_summary_table;

DROP FUNCTION fn_create_customer_address;
DROP FUNCTION fn_refresh_all_customers;
DROP FUNCTION fn_refresh_detailed_table;
DROP FUNCTION fn_refresh_summary_table;

DROP PROCEDURE sp_refresh_all_customers;
DROP PROCEDURE sp_refresh_detailed_table;
DROP PROCEDURE sp_refresh_summary_table;
