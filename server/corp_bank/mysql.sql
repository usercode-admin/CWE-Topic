DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    fullname TEXT NOT NULL,
    balance REAL NOT NULL,
    role TEXT NOT NULL,
    last_login TEXT DEFAULT '2014-07-14 15:42:10',
    status TEXT DEFAULT 'Offline',
    avatar TEXT DEFAULT 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png',
    bio TEXT DEFAULT 'E Corp verified corporate employee.',
    is_blocked INTEGER DEFAULT 0
);

INSERT INTO users (id, username, password, fullname, balance, role, last_login, status, avatar, bio, is_blocked) VALUES 
(1, 'administrator', 'e_corp_master_key_2015', 'System Administrator', 999999999.00, 'admin', '2014-07-14 17:30:00', 'Online', 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png', 'Chief Executive Infrastructure Security Director.', 0),
(2, 'Elliot', 'fsociety2015', 'Elliot Alderson', 1337.00, 'user', '2014-07-14 14:12:05', 'Offline', 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png', 'Cybersecurity Engineer at E Corp. We are fsociety.', 0);