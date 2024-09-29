-- verificar company dos clientes 

SELECT count(*) FROM Customer c WHERE Company IS NOT NULL;

SELECT FirstName FROM Customer c WHERE Company IS NULL;

SELECT  * FROM Employee e 

---- quais dos clientes são colaboradores?

SELECT c.FirstName, c.LastName FROM Customer c 
	WHERE Company IS NULL and c.FirstName IN 
		(SELECT e.FirstName FROM Employee e);
	
SELECT c.FirstName, c.LastName  FROM Customer c INNER JOIN Employee e WHERE c.FirstName = e.FirstName; 

SELECT * FROM Invoice i LIMIT 10;
SELECT * FROM InvoiceLine il ORDER BY UnitPrice DESC LIMIT 10;

SELECT UnitPrice, COUNT(*) AS Record FROM InvoiceLine il GROUP BY UnitPrice ;


---- clientes que possuem invoice associados e a quantidade associada para cada cliente.

SELECT c.CustomerId, c.FirstName, COUNT(*) as Record FROM Invoice i 
		INNER JOIN Customer c ON c.CustomerId = i.CustomerId 
		GROUP BY 1 ORDER BY Record;
	
SELECT * FROM Invoice i 
		INNER JOIN InvoiceLine il 
		INNER JOIN Customer c ON c.CustomerId = i.CustomerId 
		LIMIT 10;


