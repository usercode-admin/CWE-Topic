#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corp_bank - Enterprise Flask Server + SSH Tunnel + Linux Telemetry + SQLite
"""
import os
import time
import sqlite3
import platform
import subprocess
import threading
import re
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify

PARENT_DIR = "corp_bank"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, PARENT_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, PARENT_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'ecorp_enterprise_secure_session_key_2014'

DATABASE_PATH = os.path.join(BASE_DIR, PARENT_DIR, "database.db")
SCHEMA_PATH = os.path.join(BASE_DIR, PARENT_DIR, "mysql.sql")
SERVER_START_TIME = time.time()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_database():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
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
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO users (id, username, password, fullname, balance, role, last_login, status, avatar, bio, is_blocked) VALUES 
            (1, 'administrator', 'e_corp_master_key_2015', 'System Administrator', 999999999.00, 'admin', '2014-07-14 17:30:00', 'Online', 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png', 'Chief Executive Infrastructure Security Director.', 0)
        """)
        cursor.execute("""
            INSERT INTO users (id, username, password, fullname, balance, role, last_login, status, avatar, bio, is_blocked) VALUES 
            (2, 'Elliot', 'fsociety2015', 'Elliot Alderson', 1337.00, 'user', '2014-07-14 14:12:05', 'Offline', 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png', 'Cybersecurity Engineer at E Corp. We are fsociety.', 0)
        """)
        
    conn.commit()
    conn.close()
    print("[+] Database & Tables Initialized Successfully.")

@app.route('/api/system_info')
def system_info():
    """Collect real Linux host server hardware specs and metrics."""
    info = {
        "os_sys": f"{platform.system()} {platform.release()}",
        "hostname": platform.node(),
        "arch": platform.machine(),
        "python_ver": platform.python_version(),
        "cpu_count": os.cpu_count() or 1,
        "ram_total": "N/A", "ram_used": "N/A", "ram_percent": 0,
        "disk_total": "N/A", "disk_used": "N/A", "disk_free": "N/A", "disk_percent": 0,
        "uptime": "0h 0m 0s"
    }
    try:
        st = os.statvfs("/")
        total_bytes = st.f_blocks * st.f_frsize
        free_bytes = st.f_bavail * st.f_frsize
        used_bytes = total_bytes - free_bytes
        info["disk_total"] = f"{total_bytes / (1024**3):.2f} GB"
        info["disk_used"] = f"{used_bytes / (1024**3):.2f} GB"
        info["disk_free"] = f"{free_bytes / (1024**3):.2f} GB"
        info["disk_percent"] = round((used_bytes / total_bytes) * 100, 1) if total_bytes > 0 else 0
    except Exception:
        pass

    try:
        if os.path.exists("/proc/meminfo"):
            mem = {}
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    parts = line.split(":")
                    if len(parts) == 2:
                        mem[parts[0].strip()] = int(parts[1].split()[0].strip())
            total_kb = mem.get("MemTotal", 0)
            avail_kb = mem.get("MemAvailable", mem.get("MemFree", 0))
            used_kb = total_kb - avail_kb
            info["ram_total"] = f"{total_kb / (1024**2):.2f} GB"
            info["ram_used"] = f"{used_kb / (1024**2):.2f} GB"
            info["ram_percent"] = round((used_kb / total_kb) * 100, 1) if total_kb > 0 else 0
    except Exception:
        pass

    uptime_sec = int(time.time() - SERVER_START_TIME)
    hours, rem = divmod(uptime_sec, 3600)
    minutes, seconds = divmod(rem, 60)
    info["uptime"] = f"{hours}h {minutes}m {seconds}s"
    return jsonify(info)

@app.route('/api/check_username')
def check_username():
    username = request.args.get('username', '').strip()
    exists = False
    if username:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        exists = cursor.fetchone() is not None
    return jsonify({'exists': exists})

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('admin_panel' if session.get('role') == 'admin' else 'profile'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        db = get_db()
        cursor = db.cursor()
        
        user = None
        try:
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
        except Exception as ex:
            error = f"Database Error: {ex}"

        if user:
            if isinstance(user, dict) and user.get('is_blocked') == 1:
                return render_template('403.html'), 403

            session.clear()
            session['user_id'] = user['id'] if isinstance(user, sqlite3.Row) or isinstance(user, dict) else user[0]
            session['username'] = user['username'] if isinstance(user, sqlite3.Row) or isinstance(user, dict) else user[1]
            session['role'] = user['role'] if isinstance(user, sqlite3.Row) or isinstance(user, dict) else user[5]
            
            if session['role'] == 'admin':
                return redirect(url_for('admin_panel'))
            return redirect(url_for('profile'))
        else:
            if not error:
                error = "Invalid corporate credentials. Access denied."

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fullname = request.form.get('fullname')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, fullname, balance, role, last_login, status, avatar, bio, is_blocked) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (username, password, fullname, 1000.00, 'user', current_time, 'Offline', 'https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png', 'E Corp verified corporate employee.', 0)
            )
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            error = "Username already exists in the central database."
            
    return render_template('register.html', error=error)

@app.route('/admin')
def admin_panel():
    if 'user_id' not in session or session.get('role') != 'admin':
        return render_template('403.html'), 403
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users_list = cursor.fetchall()
    return render_template('admin.html', users_list=users_list)

@app.route('/admin/info/<int:user_id>')
def admin_info(user_id):
    if 'user_id' not in session or session.get('role') != 'admin':
        return render_template('403.html'), 403
        
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    target_user = cursor.fetchone()
    if not target_user:
        return render_template('404.html'), 404
    return render_template('admin_info.html', target_user=target_user)

@app.route('/admin/block/<int:user_id>')
def block_user(user_id):
    if 'user_id' not in session or session.get('role') != 'admin':
        return render_template('403.html'), 403
    if user_id == 1:
        return redirect(url_for('admin_panel'))
        
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT is_blocked FROM users WHERE id = ?", (user_id,))
    curr = cursor.fetchone()
    if curr:
        new_status = 0 if curr['is_blocked'] == 1 else 1
        cursor.execute("UPDATE users SET is_blocked = ? WHERE id = ?", (new_status, user_id))
        db.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/delete/<int:user_id>')
def delete_user(user_id):
    if 'user_id' not in session or session.get('role') != 'admin':
        return render_template('403.html'), 403
    if user_id == 1:
        return redirect(url_for('admin_panel'))
        
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    return redirect(url_for('admin_panel'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    db = get_db()
    cursor = db.cursor()
    
    if request.method == 'POST':
        new_bio = request.form.get('bio', '').strip()
        new_avatar = request.form.get('avatar', '').strip()
        if new_avatar:
            cursor.execute("UPDATE users SET bio = ?, avatar = ? WHERE id = ?", (new_bio, new_avatar, session['user_id']))
            session['avatar'] = new_avatar
        else:
            cursor.execute("UPDATE users SET bio = ? WHERE id = ?", (new_bio, session['user_id']))
        db.commit()
        session['bio'] = new_bio

    cursor.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
    user_info = cursor.fetchone()
    return render_template('profile.html', user_info=user_info)

@app.route('/logout')
def logout():
    if 'user_id' in session:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE users SET status = 'Offline' WHERE id = ?", (session['user_id'],))
        db.commit()
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route('/api/v1/employee/search', methods=['GET'])
def corporate_employee_search():
    query_param = request.args.get('q', '')
    db = get_db()
    cursor = db.cursor()
    
    try:
        query = f"SELECT id, username, fullname, role, balance, status FROM users WHERE username = '{query_param}'"
        cursor.execute(query.encode('utf-8', 'ignore').decode('utf-8')) # đề phòng lỗi encoding trên Termux
        results = cursor.fetchall()
        
        html = "<h3>Search Results:</h3><ul>"
        for row in results:
            html += f"<li>User: {row[1]} | Role: {row[3]} | Balance: {row[4]}</li>"
        html += "</ul>"
        return html, 200
        
    except Exception as ex:
        return f"<h3>Database Exception:</h3><p style='color:red;'>{ex}</p>", 200


ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]")
URL_RE = re.compile(r"https?://([a-z0-9-]+)\.(?:lhr\.life|localhost\.run|serveo\.net|serveousercontent\.com)\b", re.I)

def find_url(line):
    for m in URL_RE.finditer(ANSI_RE.sub("", line)):
        if m.group(1).lower() not in ("admin", "www", "docs"):
            return m.group(0)
    return None

def start_tunnel(port=5000):
    try:
        proc = subprocess.Popen(
            [
                "ssh", 
                "-o", "StrictHostKeyChecking=no", 
                "-o", "ServerAliveInterval=15",
                "-o", "ServerAliveCountMax=5",
                "-R", f"80:127.0.0.1:{port}", 
                "nokey@localhost.run"
            ],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace"
        )
        for line in proc.stdout:
            clean_line = ANSI_RE.sub("", line)
            url = find_url(clean_line)
            if url:
                print(f"\n[Public URL Generated]: {url}\n", flush=True)
                break
    except Exception as e:
        print(f"[Tunnel Error]: {e}")

if __name__ == '__main__':
    init_database()
    threading.Thread(target=start_tunnel, args=(5000,), daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)
