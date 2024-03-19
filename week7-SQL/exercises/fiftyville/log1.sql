-- Keep a log of any SQL queries you execute as you solve the mystery.

.tables
-- to see what are the available table in the DB

.schema
-- to learn about the DB schema

SELECT * FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- To learn about what crimes happened on that day
-- NOTE: Theft happened at the bakery  at 10:15 and there are 3 witness interview

SELECT name, transcript FROM interviews
WHERE month = 7 AND day = 28 AND transcript like '%bakery%';
--After reading the descriptions from the crime seen i noticed that 3 witnessess where interview and i ran this script to review their interviews
-- In interview ID = '161' Person named 'Ruth': said she saw the theif get into a car in the bakery parking log within 10min after the robbery
-- In interview ID = '162' Person named 'Eugene': said he didnt knew the theifs name but recognized him because he saw him in the morning by the ATM
--      on Leggett Street where the theif had withdrawned money
-- In interview ID = '163' Person named 'Raymond': Said the theif called someone for less than a minute. in the call he heard that they were planning
--      to take the earlist flight out of Fiftyville on next day (29) and asked for the other person to buy the flight ticket

--NOTES: Thief left between 10:15 and 10:25 by car from the parking lot
--       Thief has seen withdrawing money in the morning at 'Leggett Street'
--       Thift made a call for less than 1min, and asked for someone to buy a flight ticket to the day = 29

SELECT * FROM bakery_security_logs
WHERE month = 7 AND day = 28;
-- ran this query to see all the contents of the table in order to better understand in order to do a more specific search

SELECT license_plate FROM bakery_security_logs
WHERE activity = 'exit' AND month = 7 AND day = 28 AND HOUR = 10 AND minute >= 15 AND minute <= 25;
-- This script was based on the information from interview ID = '161' in order to find which cars left the parking lot after the theft
-- used it to get the license plate of the vehicles.

SELECT people.name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.activity = 'exit'
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <= 25;
--used to get the name of the people that exited the bakery parking lot and get my first Suspects List
--NOTE SUSPECT LIST: Vanessa | Bruce | Barry | Luca | Sofia | Iman | Diana | Kelsey

SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street';
--Ran this script based on the information from interview ID = '162' in order to find people how have withdrawn money from ATM at 'Leggett Street'

SELECT people.name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.transaction_type = 'withdraw'
AND atm_transactions.atm_location = 'Leggett Street';
-- Now i have a new suspect list of people that were on legget street withdrawing money
-- SUSPECTS: Bruce | Diana | Brooke | Kenny | Iman | Luca | Taylor | Benista
-- Now check both suspects list and see if there are matching names
-- NOTE UPDATED SUSPECT LIST: Bruce | Luca | Iman | Diana
-- As of this point i have analised 2 witness interviews and got that suspect list

SELECT * FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE phone_calls.duration <= 60
AND phone_calls.month = 7
AND phone_calls.day = 28
AND people.name IN ('Bruce', 'Luca', 'Iman', 'Diana');
-- Now i have a new suspect list that include only Bruce and Diana, both of them have made a call on the day of the robbery based on the information of 3rd interview
-- NOTE UPDATED SUSPECT LIST: Bruce | Diana
-- and based on the calls they made phone numbe

SELECT caller.name, caller.phone_number, receiver.name, receiver.phone_number FROM phone_calls
JOIN people AS caller ON caller.phone_number = phone_calls.caller
JOIN people AS receiver ON receiver.phone_number = phone_calls.receiver
WHERE phone_calls.duration <= 60
AND phone_calls.month = 7
AND phone_calls.day = 28
AND caller.name IN ('Bruce', 'Diana');
--Now i have a accomplice SUSPECT LIST: Robin | Philip

SELECT caller, caller_name, receiver, receiver_name FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

ALTER TABLE phone_calls
ADD caller_name text;
--Altering the phone_calls table to add the caller name next to the caller number

ALTER TABLE phone_calls
ADD receiver_name text;
--Altering the phone_calls table to add the reeiver name next to the receiver number


UPDATE phone_calls
SET caller_name = people.name FROM people
WHERE phone_calls.caller = people.phone_number;
--updating the caller_name value

UPDATE phone_calls
SET receiver_name = people.name FROM people
WHERE phone_calls.receiver = people.phone_number;
--updating the receiver_name value

SELECT caller, caller_name, receiver, receiver_name FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND caller_name IN('Bruce','Diana');
--i basically didnt need to do this because i already knew who my suspects accomplice might be but it was to get an easier train of thought
--NOTES:
-- SUSPECTS: Bruce | Diana
-- ACCOMPLICE: Robin | Philip


SELECT * FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour ASC
LIMIT 1;
-- Here i can find what was the earliest flight leaving the city
-- Origin airport ID = 8
-- Destination ID = 4

SELECT * FROM airports
WHERE id IN (8,4);
--Now i know that the first flight leaving Fiftyville is going to New York City with flight id 36

SELECT flights.destination_airport_id, name, phone_number, license_plate FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;
--After running this query i conclude that Bruce is the thief and ran to New York and his accomplice is Robin because he was the one that he contacted after the robery
