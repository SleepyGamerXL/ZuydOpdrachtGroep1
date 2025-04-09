
# Multiplayer WebQuiz (Flask + Socket.IO)

Deze quiz is een multiplayer webapp waarin spelers samen of tegen elkaar vragen beantwoorden — vergelijkbaar met Kahoot. Alles draait op een Apache 2-server via WSGI.

---

## 📁 Bestanden

- `app.py` — Flask Socket.IO server
- `vragen.json` — Lijst met quizvragen
- `scorebord.json` — Opslag van scores
- `quiz.wsgi` — Startbestand voor WSGI (Apache)
- `templates/index.html` — Webpagina frontend
- `static/script.js` — Real-time JS communicatie
- `requirements.txt` — Benodigde Python-pakketten

---

## 🚀 Installatie (Ubuntu/Debian)

1. **Plaats project:**
   ```bash
   sudo mkdir -p /var/www/quizweb
   cd /var/www/quizweb
   unzip multiplayer_webquiz.zip
   ```

2. **Virtualenv aanmaken:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Apache configureren:**
   ```bash
   sudo nano /etc/apache2/sites-available/quizweb.conf
   ```

   Plak dit in:
   ```
   <VirtualHost *:80>
       ServerName jouw-domein.nl

       WSGIDaemonProcess quizweb python-home=/var/www/quizweb/venv python-path=/var/www/quizweb
       WSGIScriptAlias / /var/www/quizweb/quiz.wsgi

       <Directory /var/www/quizweb>
           Require all granted
       </Directory>

       Alias /static /var/www/quizweb/static
       <Directory /var/www/quizweb/static>
           Require all granted
       </Directory>
   </VirtualHost>
   ```

4. **Activeer en herstart Apache:**
   ```bash
   sudo a2ensite quizweb
   sudo a2enmod wsgi
   sudo systemctl reload apache2
   ```

---

## 🌐 Gebruik

1. Open `http://<jouw-server-ip>/` of domeinnaam
2. Vul je naam + room in
3. Beantwoord de vragen samen met anderen in de room

---

## 🛠 Tips

- Zorg dat `vragen.json` goed gevuld is
- Pas eventueel `scorebord.json` rechten aan (of beveilig met .htaccess)
- Bekijk Apache logs bij problemen:
  ```bash
  sudo tail -f /var/log/apache2/error.log
  ```

Veel quizplezier!
