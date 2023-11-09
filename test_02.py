-- Assuming @posno, @pd, and @careerLadder are variables holding the values from your table
DECLARE @posno VARCHAR(10) = '14101A';
DECLARE @pd VARCHAR(255) = '14101A/14103A/10405A/10407A';
DECLARE @careerLadder VARCHAR(255) = '5/7/9/11';
DECLARE @grade INT = 7;

SELECT
	 [hrspos]
	,[POSNO]
	,[PD]
	,[Career Ladder]
	,[GRADE]

FROM
	PMDAccess.dbo.view_PMD
WHERE
	HeadCountStatus = 'Filled'


DECLARE @pdTable TABLE ([Value] VARCHAR(10), [Index] INT IDENTITY(1,1));
INSERT INTO @pdTable ([Value])
SELECT [Item] FROM dbo.SplitString(@pd, '/');

DECLARE @careerLadderTable TABLE ([Value] INT, [Index] INT IDENTITY(1,1));
INSERT INTO @careerLadderTable ([Value])
SELECT CONVERT(INT, [Item]) FROM dbo.SplitString(@careerLadder, '/');

DECLARE @index INT;
DECLARE @careerLadderValue INT;

-- Step 1: Splitting the fields
-- Using dbo.SplitString function to split the fields into rows
SELECT (
    SELECT @index = [Index] FROM @pdTable WHERE [Value] = @posno;
    SELECT @careerLadderValue = [Value] FROM @careerLadderTable WHERE [Index] = @index;
    -- Step 4: Compare the Career Ladder Value with GRADE Column
    IF @careerLadderValue = @grade
        PRINT 'Match';
    ELSE
        PRINT 'Mismatch';
) AS [Match]