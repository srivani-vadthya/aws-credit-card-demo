# Program Analysis Reference

## Storage sizes (bytes)

| PIC / USAGE | Size |
|---|---|
| X(n), 9(n) DISPLAY, A(n) | n (sign overpunch adds no byte; SIGN SEPARATE adds 1) |
| S9(1-4) COMP/BINARY/COMP-5 | 2 |
| S9(5-9) COMP | 4 |
| S9(10-18) COMP | 8 |
| S9(n) COMP-3 / PACKED-DECIMAL | floor(n/2)+1 (n = total digits incl. decimals) |
| COMP-1 / COMP-2 | 4 / 8 |
| POINTER, INDEX | 4 (8 under 64-bit LP(64)) |
| N(n) / NATIONAL | 2n |
| Edited (Z,9,.,-,$,CR,DB,B,/) | count of edit characters |

`V` is an implied decimal and takes no storage. `P` scaling takes no
storage. REDEFINES does not add length. OCCURS multiplies; OCCURS DEPENDING
ON gives a maximum length - document both minimum and maximum.

## COBOL FILE STATUS (first digit = class)

| Code | Meaning |
|---|---|
| 00 | Success |
| 02 | Success, duplicate alternate key |
| 04 | Record length mismatch |
| 05 | Optional file not present |
| 10 | End of file |
| 21 | Sequence error (KSDS sequential write) |
| 22 | Duplicate key |
| 23 | Record not found |
| 24 | Boundary violation |
| 30 | Permanent I/O error |
| 35 | File not found at OPEN |
| 37 | OPEN mode not permitted |
| 39 | Attribute conflict at OPEN |
| 41/42 | Already open / not open |
| 46 | Read after EOF |
| 47/48/49 | Operation not permitted for OPEN mode |
| 9x | Implementor-defined (VSAM return/feedback in extended status) |

## CICS RESP (DFHRESP) common values

| Name | Value | Name | Value |
|---|---|---|---|
| NORMAL | 0 | NOTFND | 13 |
| ERROR | 1 | DUPREC | 14 |
| INVREQ | 16 | DUPKEY | 15 |
| ENDFILE | 20 | ILLOGIC | 21 |
| LENGERR | 22 | QZERO | 23 |
| ITEMERR | 26 | PGMIDERR | 27 |
| TRANSIDERR | 28 | ENDDATA | 29 |
| QIDERR | 44 | NOTOPEN | 19 |
| DISABLED | 84 | MAPFAIL | 36 |
| NOTAUTH | 70 | IOERR | 17 |

Programs often compare RESP to numeric literals (e.g. `WHEN 13`); translate
them using this table and cite both.

## SQLCODE

0 success; +100 not found / end of cursor; -803 duplicate key; -811 more
than one row; -805/-818 package/timestamp; -904 unavailable resource;
-911/-913 deadlock/timeout; -530/-532 RI violations; -180/-181 bad
date/time; -305 null without indicator.

## DL/I status codes

blank success; GE not found; GB end of database; II duplicate on ISRT;
GA/GK crossed hierarchy level/segment type (GN); AI open error; AK invalid
field; AM invalid call for PROCOPT; TG/TH PSB not scheduled / termination;
DA key changed on REPL; DJ no prior hold.

## MQ completion / reason

MQCC_OK 0, MQCC_WARNING 1, MQCC_FAILED 2. Frequent reasons: 2033
NO_MSG_AVAILABLE, 2085 UNKNOWN_OBJECT_NAME, 2009 CONNECTION_BROKEN,
2035 NOT_AUTHORIZED, 2080 TRUNCATED_MSG_FAILED.

## LE / abend services

- `CEE3ABD` - force abend with user code (record code and timing).
- `CEEDAYS`/`CEEDATE`/`CEESECS` - date conversion; record picture strings.
- `CEELOCT`, `CEEGMT` - current time.
- CICS `ABEND ABCODE('xxxx')` - record code; `HANDLE ABEND LABEL/PROGRAM`.

## Constructs to always capture

- `REDEFINES` (variant records - document each view and its discriminator).
- `OCCURS DEPENDING ON` (variable length; name the counter field).
- Level-88 with THRU ranges and multiple values.
- `INITIALIZE`, `INSPECT`, `STRING`/`UNSTRING` (format parsing, e.g. CSV
  messages), `SEARCH`/`SEARCH ALL` (table lookups = reference data rules).
- `FUNCTION` intrinsics (CURRENT-DATE, NUMVAL, UPPER-CASE, INTEGER-OF-DATE).
- `SORT`/`MERGE` with INPUT/OUTPUT PROCEDURE.
- `ENTRY` statements (alternate entry points), `GOBACK` vs `STOP RUN`.
