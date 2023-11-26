from flask import Flask, render_template
import pymysql


app = Flask(__name__)

# Установка соединения с базой данных
conn = pymysql.connect(
    host='db',  # Название сервиса контейнера базы данных в Docker Compose
    user='root',
    password='Demid2019Mark2022'
)

# Создаем базу данных
create_database_query = 'CREATE DATABASE your_database;'
with conn.cursor() as cursor:
    drop_database_query = "DROP DATABASE your_database;"

    # Execute the DROP DATABASE query
    cursor.execute(drop_database_query)

    # Commit the changes
    conn.commit()
    cursor.execute(create_database_query)

    # Создаем пользователя root с паролем
    create_user_query = "CREATE USER 'root'@'db' IDENTIFIED BY 'Demid2019Mark2022';"
    grant_query = "GRANT ALL PRIVILEGES ON your_database.* TO 'root'@'db';"
    cursor.execute(create_user_query)
    cursor.execute(grant_query)

    drop_table_query = 'DROP TABLE IF EXISTS good;'
    cursor.execute(drop_table_query)
    conn.commit()

    # Создание таблицы
    create_table_query = """
    CREATE TABLE IF NOT EXISTS `good` (
      `id` int(11) NOT NULL,
      `category_id` int(11) NOT NULL,
      `name` varchar(255) DEFAULT NULL,
      `count` int(11) NOT NULL,
      `price` int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    cursor.execute(create_table_query)

    # Добавление данных в таблицу
    insert_data_query = """
    INSERT INTO `good` (`id`, `category_id`, `name`, `count`, `price`) VALUES
    (1, 3, 'Айс Ти «Инжирный персик»', 201, 157),
    (2, 3, 'Айс Ти «Черничный Прованс»', 201, 157),
    (3, 3, 'Айс Ти «Сочное манго»', 288, 157);
    """

    cursor.execute(insert_data_query)

    # Фиксация изменений
    conn.commit()

@app.route('/')
def index():
    # Выполнение запроса на получение всех данных из таблицы
    select_data_query = "SELECT * FROM `good`"
    cursor.execute(select_data_query)
    results = cursor.fetchall()

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

