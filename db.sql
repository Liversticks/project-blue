CREATE TABLE IF NOT EXISTS stage (
    id INTEGER PRIMARY KEY,
    is_hard BOOLEAN NOT NULL,
    stage VARCHAR(50) NOT NULL,
    default_clear_time INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS attempt_history (
    id INTEGER PRIMARY KEY,
    stage VARCHAR(50) NOT NULL,
    end_time INTEGER NOT NULL, -- UNIX timestamp
    clear_time INTEGER NOT NULL, -- seconds
    FOREIGN KEY(stage) REFERENCES stage(stage)
);

CREATE TABLE IF NOT EXISTS event_history (
    id INTEGER PRIMARY KEY,
    event_name TEXT NOT NULL,
    start_time TEXT NOT NULL, -- ISO 8601
    end_time TEXT NOT NULL, -- ISO 8601
    event_type TEXT CHECK( event_type IN ('EX', 'SP', 'T')) -- EX = regular, SP = SP, T = collab
);

-- default_clear_time = 120 s (S-rank threshold) * number of fleets (from the wiki)
INSERT INTO stage (is_hard, stage, default_clear_time) VALUES
    (false, '1-1', 120 * 2),
    (false, '1-2', 120 * 3),
    (false, '1-3', 120 * 3),
    (false, '1-4', 120 * 4),
    (false, '2-1', 120 * 3),
    (false, '2-2', 120 * 4),
    (false, '2-3', 120 * 4),
    (false, '2-4', 120 * 4),
    (false, '3-1', 120 * 4),
    (false, '3-2', 120 * 4),
    (false, '3-3', 120 * 4),
    (false, '3-4', 120 * 4),
    (false, '4-1', 120 * 4),
    (false, '4-2', 120 * 4),
    (false, '4-3', 120 * 4),
    (false, '4-4', 120 * 5),
    (false, '5-1', 120 * 5),
    (false, '5-2', 120 * 5),
    (false, '5-3', 120 * 5),
    (false, '5-4', 120 * 5),
    (false, '6-1', 120 * 5),
    (false, '6-2', 120 * 5),
    (false, '6-3', 120 * 5),
    (false, '6-4', 120 * 6),
    (false, '7-1', 120 * 6),
    (false, '7-2', 120 * 6),
    (false, '7-3', 120 * 6),
    (false, '7-4', 120 * 6),
    (false, '8-1', 120 * 5),
    (false, '8-2', 120 * 5),
    (false, '8-3', 120 * 5),
    (false, '8-4', 120 * 5),
    (false, '9-1', 120 * 6),
    (false, '9-2', 120 * 6),
    (false, '9-3', 120 * 6),
    (false, '9-4', 120 * 6),
    (false, '10-1', 120 * 7),
    (false, '10-2', 120 * 7),
    (false, '10-3', 120 * 7),
    (false, '10-4', 120 * 7),
    (false, '11-1', 120 * 7),
    (false, '11-2', 120 * 7),
    (false, '11-3', 120 * 7),
    (false, '11-4', 120 * 7),
    (false, '12-1', 120 * 7),
    (false, '12-2', 120 * 7),
    (false, '12-3', 120 * 7),
    (false, '12-4', 120 * 7),
    (false, '13-1', 120 * 7),
    (false, '13-2', 120 * 7),
    (false, '13-3', 120 * 7),
    (false, '13-4', 120 * 8),
    (false, '14-1', 120 * 7),
    (false, '14-2', 120 * 7),
    (false, '14-3', 120 * 7),
    (false, '14-4', 120 * 8),
    --from Virtual Tower
    (false, 'SP-1', 120 * 5),
    (false, 'SP-2', 120 * 5),
    (false, 'SP-3', 120 * 6),
    (false, 'SP-4', 120 * 6),
    --from Aurora Noctis Rerun
    (false, 'A-1', 120 * 4),
    (false, 'A-2', 120 * 5),
    (false, 'A-3', 120 * 5),
    (false, 'A-4', 120 * 5),
    (false, 'B-1', 120 * 5),
    (false, 'B-2', 120 * 6),
    (false, 'B-3', 120 * 6),
    (true, 'C-1', 120 * 5),
    (true, 'C-2', 120 * 5),
    (true, 'C-3', 120 * 6),
    (true, 'C-4', 120 * 6),
    (true, 'D-1', 120 * 6),
    (true, 'D-2', 120 * 7),
    (true, 'D-3', 120 * 7),
    --from World-Spanning Arclight
    (false, 'T-1', 120 * 5),
    (false, 'T-2', 120 * 5),
    (false, 'T-3', 120 * 5),
    (false, 'T-4', 120 * 5),
    (false, 'T-5', 120 * 5),
    --from Alchemist and the Archipegalo of Secrets
    (false, 'TH-1', 120 * 5),
    (false, 'TH-2', 120 * 5),
    (false, 'TH-3', 120 * 5),
    (false, 'TH-4', 120 * 5),
    (false, 'TH-5', 120 * 5);    
