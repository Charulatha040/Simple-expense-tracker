{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "70ce3091-01bc-4ba1-91f4-63c35e9b3c4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "UsageError: unrecognized arguments: # Save this code as 'app.py'\n"
     ]
    }
   ],
   "source": [
    "%%writefile app.py  # Save this code as 'app.py'\n",
    "\n",
    "from flask import Flask, render_template, request, redirect, url_for\n",
    "import mysql.connector\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Database connection\n",
    "def get_db_connection():\n",
    "    return mysql.connector.connect(\n",
    "        host=\"localhost\",\n",
    "        user=\"root\",\n",
    "        password=\"Charu*2004\",\n",
    "        database=\"expense_tracker\"\n",
    "    )\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/add_expense', methods=['POST'])\n",
    "def add_expense():\n",
    "    expense_name = request.form['expenseName']\n",
    "    expense_amount = request.form['expenseAmount']\n",
    "    conn = get_db_connection()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"INSERT INTO expenses (name, amount) VALUES (%s, %s)\", (expense_name, expense_amount))\n",
    "    conn.commit()\n",
    "    cursor.close()\n",
    "    conn.close()\n",
    "    return redirect(url_for('index'))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b26d0c7b-8751-4ccd-bbda-effd8d9adf17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [30/Oct/2024 01:35:51] \"GET / HTTP/1.1\" 500 -\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 1498, in __call__\n",
      "    return self.wsgi_app(environ, start_response)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 1476, in wsgi_app\n",
      "    response = self.handle_exception(e)\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 1473, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 882, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 880, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "         ^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\app.py\", line 865, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\AppData\\Local\\Temp\\ipykernel_22820\\471209148.py\", line 23, in index\n",
      "    return render_template('index.html', expenses=expenses)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\templating.py\", line 149, in render_template\n",
      "    template = app.jinja_env.get_or_select_template(template_name_or_list)\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\jinja2\\environment.py\", line 1084, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\jinja2\\environment.py\", line 1013, in get_template\n",
      "    return self._load_template(name, globals)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\jinja2\\environment.py\", line 972, in _load_template\n",
      "    template = self.loader.load(self, name, self.make_globals(globals))\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\jinja2\\loaders.py\", line 126, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\templating.py\", line 65, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\Charurubi\\Downloads\\Lib\\site-packages\\flask\\templating.py\", line 99, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [30/Oct/2024 01:35:51] \"GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [30/Oct/2024 01:35:51] \"GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [30/Oct/2024 01:35:51] \"GET /?__debugger__=yes&cmd=resource&f=console.png&s=ekA3fYhLgwZJL0rNDzfu HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [30/Oct/2024 01:35:51] \"GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)  # disable auto-reloading for Jupyter\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49871c77-27dd-45e3-94f8-26be08bbef5f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
