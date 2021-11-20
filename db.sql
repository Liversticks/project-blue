CREATE TABLE stage (
    id INTEGER PRIMARY KEY,
    is_hard BOOLEAN NOT NULL,
    stage VARCHAR(50) NOT NULL,
    clear_time INTEGER NOT NULL
);

-- Clear times skew slightly conservative
-- 120 sec per battle (S-rank)
INSERT INTO stage (is_hard, stage, clear_time) VALUES
    (false, '1-1', 240),
    (false, '1-2', 360),
    (false, '1-3', 360),
    (false, '1-4', 480),
    (false, '2-1', 360),
    (false, '2-2', 480),
    (false, '2-3', 480),
    (false, '2-4', 480),
    (false, '3-1', 480),
    (false, '3-2', 480),
    (false, '3-3', 480),
    (false, '3-4', 480),
    (false, '4-1', 480),
    (false, '4-2', 480),
    (false, '4-3', 480),
    (false, '4-4', 600),
    (false, '5-1', 600),
    (false, '5-2', 600),
    (false, '5-3', 600),
    (false, '5-4', 600),
    (false, '6-1', 600),
    (false, '6-2', 600),
    (false, '6-3', 600),
    (false, '6-4', 720),
    (false, '7-1', 720),
    (false, '7-2', 720),
    (false, '7-3', 720),
    (false, '7-4', 720),
    (false, '8-1', 600),
    (false, '8-2', 600),
    (false, '8-3', 600),
    (false, '8-4', 600),
    (false, '9-1', 720),
    (false, '9-2', 720),
    (false, '9-3', 720),
    (false, '9-4', 720),
    (false, '10-1', 840),
    (false, '10-2', 840),
    (false, '10-3', 840),
    (false, '10-4', 840),
    (false, '11-1', 840),
    (false, '11-2', 840),
    (false, '11-3', 840),
    (false, '11-4', 840),
    (false, '12-1', 840),
    (false, '12-2', 840),
    (false, '12-3', 840),
    (false, '12-4', 840),
    (false, 'SP-1', 600),
    (false, 'SP-2', 600),
    (false, 'SP-3', 720),
    (false, 'A-1', 480),
    (false, 'A-2', 600),
    (false, 'A-3', 600),
    (false, 'B-1', 600),
    (false, 'B-2', 720),
    (false, 'B-3', 720),
    (true, 'C-1', 600),
    (true, 'C-2', 600),
    (true, 'C-3', 720),
    (true, 'D-1', 720),
    (true, 'D-2', 840),
    (true, 'D-3', 840);
