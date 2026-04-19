@app.route("/book29", methods=["GET", "POST"])
def book29():

    if request.method == "POST":

        book = request.form.get("book")
        author = request.form.get("author")

        return render_template(
            "result29.html",
            book=book,
            author=author
        )

    return render_template("index29.html")
