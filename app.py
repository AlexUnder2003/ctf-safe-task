from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Секретный код сейфа
SECRET_CODE = [5, 3, 8]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем цифры от пользователя
        guess = request.form.getlist("guess")
        guess = [int(num) for num in guess]

        # Проверка на правильность
        if guess == SECRET_CODE:
            return render_template(
                "result.html",
                result="Поздравляю! Вы открыли сейф! 'flag(safe_unlocked_flag)'",
            )
        else:
            return render_template("result.html", result="Неверно, попробуйте снова!")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
